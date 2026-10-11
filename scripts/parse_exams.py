#!/usr/bin/env python3
"""Extrae cuestionarios oficiales y los cruza con las plantillas correctoras."""

import json
import re
import unicodedata
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
EXAMS = ROOT / "EXAMANES ANTERIORES"
OUT = ROOT / "data" / "official-questions.json"

SOURCES = [
    {
        "id": "tm-2025-06-18pl",
        "file": "18plCuestionario.pdf",
        "key": "18plPlantillaDef.pdf",
        "title": "Técnico/a Medio TIC, acceso libre, 1 de junio de 2025",
        "category": "tecnico-medio",
        "key_style": "rows",
    },
    {
        "id": "tm-2023-11-2pl",
        "file": "2plCuestionarioPreguntas.pdf",
        "key": "2plPlantRespuestDef.pdf",
        "title": "Técnico/a Medio TIC, acceso libre, 19 de noviembre de 2023",
        "category": "tecnico-medio",
        "key_style": "columns",
    },
    {
        "id": "tm-modelo-b",
        "file": "20plCuesMODELOB.pdf",
        "key": "20plPlantillaB.pdf",
        "title": "Técnico/a Medio TIC, primer ejercicio, modelo B",
        "category": "tecnico-medio",
        "key_style": "pr",
    },
    {
        "id": "tm-pi-2025-02",
        "file": "20plCuadernillo.pdf",
        "key": "20plPlantRespDef.pdf",
        "title": "Técnico/a Medio TIC, promoción interna, 19 de febrero de 2025",
        "category": "tecnico-medio",
        "key_style": "columns",
    },
    {
        "id": "tm-pi-2023-06",
        "file": "43plCuestionario.pdf",
        "key": "43plPlantDefResp1Ej.pdf",
        "title": "Técnico/a Medio TIC, promoción interna, 26 de junio de 2023",
        "category": "tecnico-medio",
        "key_style": "inline",
    },
    {
        "id": "aux-teo-2023",
        "file": "8plCuestionarioParteTeórica.pdf",
        "key": "8plAuxiliarTICParteTeoricaPlantilla.pdf",
        "title": "Auxiliar TIC, parte teórica, 24 de junio de 2023",
        "category": "auxiliar",
        "key_style": "dotted",
    },
    {
        "id": "aux-prac-2023",
        "file": "8plCuestionarioPartePráctica.pdf",
        "key": "8plAuxiliarTICPartePracticaPlantilla.pdf",
        "title": "Auxiliar TIC, parte práctica tipo test, 24 de junio de 2023",
        "category": "auxiliar",
        "key_style": "dotted",
    },
]


def pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    chunks = []
    for page in reader.pages:
        chunks.append(page.extract_text() or "")
    return "\n".join(chunks)


def clean_block(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
    text = re.sub(r"P\s*á\s*g\s*i\s*n\s*a\s+\d+\s*\|\s*\d+", " ", text, flags=re.I)
    text = re.sub(r"Página\s+\d+\s+de\s+\d+", " ", text, flags=re.I)
    text = re.sub(r"economía,\s*innovación\s*y\s*hacienda", " ", text, flags=re.I)
    text = re.sub(r"BOAM núm\..*", " ", text)
    text = re.sub(r"CSV:\s*\S+", " ", text)
    text = re.sub(r"Verificable en https://\S+", " ", text)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if re.fullmatch(r"\d{1,3}", stripped):
            continue
        lines.append(stripped)
    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", text)
    text = repair_word_splits(text)
    return text


def parse_questions(text: str) -> list[dict]:
    text = clean_block(text)
    matches = list(
        re.finditer(
            r"(?:(?<=^)|(?<=\s))(\d{1,3})[.)](?=\s*[¿¡A-ZÁÉÍÓÚÑ\"«])",
            text,
        )
    )
    questions = []
    for index, match in enumerate(matches):
        number = int(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        if number < 1 or number > 120:
            continue
        options = split_options(body)
        if not options:
            continue
        stem = options["stem"]
        choices = options["choices"]
        if len(choices) < 3 or len(stem) < 12:
            continue
        questions.append(
            {
                "number": number,
                "stem": stem,
                "choices": choices[:3],
            }
        )
    # Quédate con la primera aparición de cada número consecutivo razonable.
    by_number = {}
    for question in questions:
        by_number.setdefault(question["number"], question)
    ordered = [by_number[n] for n in sorted(by_number)]
    return ordered


def split_options(body: str) -> dict | None:
    marks = list(re.finditer(r"(?:(?<=^)|(?<=\s))([abc])\s*[.)]\s+", body, flags=re.I))
    if len(marks) < 3:
        return None
    # Usa la primera secuencia a, b, c.
    sequence = []
    expected = "a"
    for mark in marks:
        letter = mark.group(1).lower()
        if letter == expected:
            sequence.append(mark)
            expected = chr(ord(expected) + 1)
            if expected == "d":
                break
    if len(sequence) < 3:
        return None
    stem = body[: sequence[0].start()].strip(" .-")
    choices = []
    for index, mark in enumerate(sequence):
        start = mark.end()
        end = sequence[index + 1].start() if index + 1 < len(sequence) else len(body)
        choice = body[start:end].strip(" ;")
        choice = re.sub(r"\s+", " ", choice).strip()
        choices.append(choice)
    stem = re.sub(r"\s+", " ", stem).strip()
    if any(len(choice) < 1 for choice in choices):
        return None
    return {"stem": stem, "choices": choices}


def repair_word_splits(text: str) -> str:
    """Cierra cortes típicos del PDF: 'p or' o 'opin ión'."""
    text = re.sub(
        r"\b([bcdfghjklmnpqrstvxz]) ([a-záéíóúñ]{2,})\b",
        r"\1\2",
        text,
    )
    text = re.sub(
        r"\b([a-záéíóúñ]{3,}) (ción|sión|ión|miento)\b",
        r"\1\2",
        text,
    )
    return text


def parse_key(text: str, style: str) -> dict[int, str | None]:
    raw = clean_block(text).upper()
    raw = raw.replace("ANULADA", "ANULAR").replace("ANULADO", "ANULAR")
    key = {}
    pattern = r"(?:RESERVA\s+)?(\d{1,3})\s+(ANULAR|A|B|C)\b"
    if style == "pr":
        pattern = r"PR\s*(\d{1,3})\s+(ANULAR|A|B|C)\b"
    elif style == "dotted":
        pattern = r"(\d{1,3})\s*[.)]\s*(ANULAR|A|B|C)\b"
    for number, answer in re.findall(pattern, raw):
        key[int(number)] = None if answer == "ANULAR" else answer
    return key


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


RULES = [
    (1, ["constitucion", "derechos fundamentales", "defensor del pueblo", "recurso de amparo", "corona", "cortes generales"]),
    (2, ["comunidad autonoma", "comunidades autonomas", "administracion local", "municipio", "competencias municipales", "articulo 137", "articulo 140", "articulo 148", "articulo 149"]),
    (3, ["pleno", "alcalde", "junta de gobierno", "teniente de alcalde", "tenientes de alcalde"]),
    (4, ["intervencion general", "tesoreria", "tribunal economico", "agencia tributaria madrid", "asesoria juridica"]),
    (5, ["area de gobierno", "areas de gobierno", "organos superiores", "coordinador general", "director general"]),
    (6, ["distrito", "junta municipal", "concejal presidente", "coordinador del distrito"]),
    (7, ["estatuto basico", "empleado publico", "funcionario de carrera", "situaciones administrativas", "regimen disciplinario", "carrera profesional", "permisos", "retributiv"]),
    (8, ["transparencia", "buen gobierno", "consejo de transparencia", "ordenanza de transparencia"]),
    (9, ["procedimiento administrativo", "ley 39/2015", "recurso de alzada", "recurso potestativo", "silencio administrativo", "notificacion"]),
    (10, ["ley 40/2015", "abstencion", "recusacion", "responsabilidad patrimonial", "sector publico", "delegacion de competencias"]),
    (11, ["contrato", "lcsp", "ley 9/2017", "adjudicacion", "licitacion", "sector publico"]),
    (12, ["hacienda local", "tasa", "precio publico", "contribucion especial", "impuesto municipal", "ibi", "iae", "ivtm"]),
    (13, ["prevencion de riesgos", "delegado de prevencion", "comite de seguridad y salud", "riesgos laborales"]),
    (14, ["igualdad efectiva", "acoso sexual", "ley organica 3/2007", "personas trans", "lgtbi", "plan de igualdad"]),
    (15, ["proteccion de datos", "lopdgdd", "delegado de proteccion", "tratamiento", "rgpd", "derechos digitales", "aepd"]),
    (16, ["esquema nacional de seguridad", "esquema nacional de interoperabilidad", "ens", "eni", "documento electronico", "expediente electronico", "categorizacion"]),
    (17, ["sede electronica", "clave", "dni electronico", "dnie", "interoperabilidad", "red sara", "punto de acceso"]),
    (18, ["arquitectura de hardware", "multiprocesador", "grid", "cluster", "smp", "multinucleo", "superordenador"]),
    (19, ["sistema operativo", "linux", "windows", "unix", "kernel", "proceso", "hilo"]),
    (20, ["paradigma", "programacion orientada", "lenguaje de programacion", "compilador", "interprete"]),
    (21, ["oltp", "data warehouse", "almacen de datos", "dss", "mis "]),
    (22, ["sql", "base de datos relacional", "odbc", "jdbc", "jpa", "nosql", "clave primaria", "normalizacion"]),
    (23, ["cliente-servidor", "cliente servidor", "soap", "rest", "servicio web", "microservicio"]),
    (24, ["tcp/ip", "tcp ip", "direccion ip", "enrutamiento", "encaminamiento", "mascara de red", "puerto"]),
    (25, ["html", "css", "javascript", "ecmascript", "xml", "sgml", "ruby on rails"]),
    (26, ["itil", "iso 20000", "iso 19770", "centro de sistemas", "gobierno de las ti"]),
    (27, ["magerit", "plan de contingencias", "plan de recuperacion", "plan de seguridad", "salvaguarda"]),
    (28, ["seguridad logica", "seguridad fisica", "vulnerabilidad", "amenaza", "cifrado", "malware"]),
    (29, ["auditoria informatica", "auditoria"]),
    (30, ["crm", "ivr", "voice xml", "centro de contacto", "call center"]),
    (31, ["software libre", "codigo abierto", "licencia gpl", "licencia", "propiedad intelectual del software"]),
    (32, ["viabilidad", "presupuesto", "coste de un proyecto", "analisis de alternativas"]),
    (33, ["gestion documental", "gestor de contenidos", "seo", "sindicacion", "workflow", "documatica"]),
    (34, ["ciclo de vida", "modelo en cascada", "modelo en espiral", "prototipado"]),
    (35, ["metrica", "metodologia de desarrollo"]),
    (36, ["requisitos", "entrevista", "prototipo"]),
    (37, ["diagrama de flujo", "flujograma", "dfd"]),
    (38, ["modelo entidad", "entidad relacion", "modelizacion conceptual", "atributo"]),
    (39, ["ansi/sparc", "concurrencia", "diseño logico", "diseno logico", "diseno fisico"]),
    (40, ["estructura de datos", "arbol", "grafo", "ordenacion", "algoritmo de busqueda", "lista enlazada"]),
    (41, ["inteligencia artificial", "aprendizaje automatico", "devops"]),
    (42, ["cohesion", "acoplamiento", "diagrama estructurado"]),
    (43, ["manual de usuario", "manual tecnico", "puesta en produccion", "formacion de usuarios"]),
    (44, ["caja negra", "caja blanca", "prueba de software", "tdd", "desarrollo dirigido"]),
    (45, ["mantenimiento", "puesta en produccion", "post-implementacion"]),
    (46, ["uml", "orientado a objetos", "patron de diseño", "patron de diseno", "proceso unificado"]),
    (47, ["java ee", "jakarta", "jee"]),
    (48, ["aplicacion web", "accesibilidad web", "internacionalizacion", "i18n"]),
    (49, ["php", "ruby", "javascript"]),
    (50, ["android", "ios", "aplicacion movil", "aplicaciones moviles"]),
    (51, ["sistema de informacion geografica", "sig ", "gis", "ide ", "bim"]),
    (52, ["calidad del software", "iso 25010", "metrica de calidad", "cmmi"]),
    (53, ["accesibilidad", "usabilidad", "rd 1112", "real decreto 1112", "wcag", "diseño universal"]),
    (54, ["mineria de datos", "olap", "big data", "aprendizaje automatico"]),
    (55, ["administracion del sistema", "control de cambios"]),
    (56, ["administracion de bases", "dba", "administrador de la base"]),
    (57, ["mantenimiento preventivo", "mantenimiento correctivo", "monitorizacion", "capacidad"]),
    (58, ["libreria de programas", "lenguaje de control", "jcl"]),
    (59, ["rendimiento", "planificacion de la capacidad", "carga del sistema"]),
    (60, ["san", "nas", "das", "almacenamiento"]),
    (61, ["centro de proceso", "cpd", "sala tecnica"]),
    (62, ["virtualizacion", "cloud", "nube", "particion logica"]),
    (63, ["red de area local", "lan", "ethernet", "topologia"]),
    (64, ["ipv6", "calidad de servicio", "qos"]),
    (65, ["mpls", "conmutacion", "voip", "encaminamiento"]),
    (66, ["cortafuegos", "firewall", "vpn", "firma digital", "criptograf"]),
    (67, ["internet", "iot", "internet de las cosas", "dns", "http"]),
    (68, ["voip", "fijo-movil", "multimedia"]),
    (69, ["inalambric", "tetra", "wifi", "lte", "5g", "lmts", "lm ds", "trunking"]),
]


def classify(stem: str, choices: list[str]) -> int:
    blob = f" {normalize(stem + ' ' + ' '.join(choices))} "
    best_topic = 0
    best_score = 0
    for topic, words in RULES:
        score = 0
        for word in words:
            token = normalize(word).strip()
            if len(token) < 3:
                continue
            if re.search(rf"(?<![a-z0-9]){re.escape(token)}(?![a-z0-9])", blob):
                score += 3 if len(token) > 12 else 2
        if score > best_score:
            best_score = score
            best_topic = topic
    return best_topic


def main() -> None:
    all_questions = []
    report = []
    for source in SOURCES:
        exam_text = pdf_text(EXAMS / source["file"])
        key_text = pdf_text(EXAMS / source["key"])
        parsed = parse_questions(exam_text)
        key = parse_key(key_text, source["key_style"])
        kept = 0
        annulled = 0
        missing = 0
        for question in parsed:
            answer = key.get(question["number"], "MISSING")
            if answer == "MISSING":
                missing += 1
                continue
            if answer is None:
                annulled += 1
                continue
            letter = answer
            index = "ABC".index(letter)
            if index >= len(question["choices"]):
                missing += 1
                continue
            all_questions.append(
                {
                    "id": f"{source['id']}-{question['number']:03d}",
                    "sourceId": source["id"],
                    "source": source["title"],
                    "category": source["category"],
                    "number": question["number"],
                    "stem": question["stem"],
                    "choices": question["choices"],
                    "answer": index,
                    "topic": classify(question["stem"], question["choices"]),
                    "origin": "examen-oficial",
                }
            )
            kept += 1
        report.append(
            f"{source['id']}: parsed={len(parsed)} key={len(key)} kept={kept} annulled={annulled} missing={missing}"
        )

    seen = set()
    unique = []
    duplicates = 0
    for question in all_questions:
        signature = normalize(question["stem"])[:180]
        if signature in seen:
            duplicates += 1
            continue
        seen.add(signature)
        unique.append(question)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(unique, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(report))
    print(f"total={len(all_questions)} unique={len(unique)} duplicates={duplicates}")
    from collections import Counter

    counts = Counter(q["topic"] for q in unique)
    for topic in range(0, 70):
        print(f"T{topic:02d} {counts.get(topic, 0)}")


if __name__ == "__main__":
    main()

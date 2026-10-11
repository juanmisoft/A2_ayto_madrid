# -*- coding: utf-8 -*-
"""Fusiona exámenes oficiales, banco de refuerzo, temario y supuestos."""

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
JS = ROOT / "js"

SYLLABUS = [
    (1, "I", "La Constitución Española: estructura, derechos fundamentales, Gobierno y Administración."),
    (2, "I", "Organización territorial del Estado. Administración Local. Municipio."),
    (3, "I", "Ayuntamiento de Madrid: Pleno, Alcalde, Tenientes de Alcalde y Junta de Gobierno."),
    (4, "I", "Administración municipal: Intervención, Tesorería, TEAM, Agencia Tributaria y Asesoría Jurídica."),
    (5, "I", "Reglamento Orgánico: Áreas de Gobierno, órganos superiores y directivos."),
    (6, "I", "Distritos: Concejal Presidente y estructura administrativa."),
    (7, "I", "Estatuto Básico del Empleado Público."),
    (8, "I", "Transparencia, acceso a la información y Ordenanza de la Ciudad de Madrid."),
    (9, "I", "Ley 39/2015: procedimiento administrativo y recursos."),
    (10, "I", "Ley 40/2015: órganos, abstención, recusación y responsabilidad patrimonial."),
    (11, "I", "Ley 9/2017, de Contratos del Sector Público."),
    (12, "I", "Haciendas locales: tasas, precios públicos e impuestos municipales."),
    (13, "I", "Prevención de riesgos laborales y Acuerdo-Convenio municipal."),
    (14, "I", "Igualdad, derechos LGTBI y Plan de Igualdad municipal."),
    (15, "II", "Protección de datos personales y garantía de los derechos digitales."),
    (16, "II", "Esquema Nacional de Seguridad, interoperabilidad, documento y expediente electrónicos."),
    (17, "II", "Sedes electrónicas, Cl@ve, DNI electrónico y servicios comunes."),
    (18, "II", "Arquitecturas de hardware: móviles, clusters, SMP y multinúcleo."),
    (19, "II", "Sistemas operativos: Windows, Linux, Unix y móviles."),
    (20, "II", "Lenguajes y paradigmas de programación."),
    (21, "II", "Entornos de datos: OLTP, MIS, DSS y almacenes de datos."),
    (22, "II", "Bases de datos relacionales, SQL, JDBC/ODBC/JPA y NoSQL."),
    (23, "II", "Arquitectura cliente-servidor. SOAP y REST."),
    (24, "II", "Modelo TCP/IP: capas, direccionamiento y encaminamiento."),
    (25, "II", "Desarrollo web: HTML, XML, HTML5, CSS3, ECMAScript y Rails."),
    (26, "II", "Gobierno TIC: ITIL v3, ISO 20000 e ISO 19770-1."),
    (27, "II", "Planes de seguridad, contingencia, recuperación y MAGERIT."),
    (28, "II", "Seguridad física y lógica: riesgos, amenazas y salvaguardas."),
    (29, "II", "Auditoría informática: objetivos, alcance y metodología."),
    (30, "II", "Atención a la ciudadanía: CRM, IVR y VoiceXML."),
    (31, "II", "Software libre, licencias y protección jurídica de los programas."),
    (32, "II", "Evaluación de alternativas, viabilidad y control de costes."),
    (33, "II", "Gestión documental, contenidos, flujos, búsqueda y SEO."),
    (34, "II", "Ciclo de vida de los sistemas y sus modelos."),
    (35, "II", "Gestión del desarrollo y metodología Métrica."),
    (36, "II", "Estrategias de determinación de requisitos."),
    (37, "II", "Diagramas de flujo de datos y flujogramas."),
    (38, "II", "Modelización conceptual: entidades, atributos y relaciones."),
    (39, "II", "Diseño de bases de datos, normalización y concurrencia."),
    (40, "II", "Estructuras de datos, algoritmos y organizaciones de ficheros."),
    (41, "II", "Inteligencia artificial aplicada al ciclo de desarrollo."),
    (42, "II", "Diseño estructurado: cohesión y acoplamiento."),
    (43, "II", "Construcción, documentación y formación."),
    (44, "II", "Pruebas de caja negra, caja blanca y desarrollo dirigido por pruebas."),
    (45, "II", "Instalación, cambio, recepción y mantenimiento."),
    (46, "II", "Orientación a objetos, Proceso Unificado, UML y patrones."),
    (47, "II", "Arquitectura Java EE."),
    (48, "II", "Aplicaciones web multiplataforma, servicios web e internacionalización."),
    (49, "II", "Tecnologías de programación: JavaScript, PHP y Ruby."),
    (50, "II", "Aplicaciones móviles iOS y Android."),
    (51, "II", "Sistemas de información geográfica, BIM e IDE."),
    (52, "II", "Calidad del software: modelos, métricas y estándares."),
    (53, "II", "Accesibilidad (RD 1112/2018), diseño universal y usabilidad."),
    (54, "II", "Minería de datos, OLAP, big data y aprendizaje automático."),
    (55, "II", "Administración del sistema operativo y control de cambios."),
    (56, "II", "Administración de bases de datos y administración de datos."),
    (57, "II", "Mantenimiento de equipos, monitorización y capacidad."),
    (58, "II", "Librerías de programas, soportes y lenguajes de control de trabajos."),
    (59, "II", "Control de la ejecución, rendimiento y planificación de la capacidad."),
    (60, "II", "Almacenamiento SAN, NAS y DAS."),
    (61, "II", "Planificación física de un centro de tratamiento de la información."),
    (62, "II", "Virtualización, cloud y particiones lógicas."),
    (63, "II", "Redes de área local."),
    (64, "II", "Redes IP, calidad de servicio e IPv6."),
    (65, "II", "Conmutación, voz sobre IP, encaminamiento y MPLS."),
    (66, "II", "Seguridad en redes: cifrado, firma, cortafuegos y VPN."),
    (67, "II", "Internet, servicios y sensorización."),
    (68, "II", "Comunicaciones sobre IP: VoIP y multimedia."),
    (69, "II", "Redes inalámbricas, TETRA y telefonía móvil."),
]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def main() -> None:
    official = json.loads((DATA / "official-questions.json").read_text(encoding="utf-8"))
    extra = json.loads((DATA / "extra-questions.json").read_text(encoding="utf-8"))
    practicals = json.loads((DATA / "practicals.json").read_text(encoding="utf-8"))

    for question in official:
        question.setdefault(
            "explanation",
            "Respuesta según la plantilla oficial de esa prueba. Contrasta el precepto o el concepto con el tema del programa y anota por qué caen las otras dos opciones.",
        )

    seen = {normalize(q["stem"])[:180] for q in official}
    merged = list(official)
    for question in extra:
        signature = normalize(question["stem"])[:180]
        if signature in seen:
            continue
        seen.add(signature)
        merged.append(question)

    syllabus = [
        {"id": number, "group": group, "title": title}
        for number, group, title in SYLLABUS
    ]
    bank = {
        "meta": {
            "title": "Técnico/a Medio TIC del Ayuntamiento de Madrid",
            "convocatoria": "Bases específicas aprobadas por resolución de 24 de febrero de 2026 (BOAM núm. 10.075).",
            "questions": 100,
            "reserve": 7,
            "options": 3,
            "minutes": 107,
            "pass": 5,
            "penalty": "1/3",
        },
        "syllabus": syllabus,
        "questions": merged,
        "practicals": practicals,
    }
    JS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(bank, ensure_ascii=False, separators=(",", ":"))
    (JS / "bank.js").write_text("window.BANK = " + payload + ";\n", encoding="utf-8")
    print(f"questions={len(merged)} practicals={len(practicals)} bytes={len(payload)}")


if __name__ == "__main__":
    main()

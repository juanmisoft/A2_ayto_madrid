# -*- coding: utf-8 -*-
"""Preguntas de refuerzo alineadas con el programa de las bases de 2026.

Cubren huecos del temario con normativa estatal y organización del Ayuntamiento
de Madrid. No incorporan particularidades de otras comunidades autónomas.
"""

ITEMS = []


def add(topic, stem, choices, answer, why):
    ITEMS.append(
        {
            "topic": topic,
            "stem": stem,
            "choices": choices,
            "answer": answer,
            "explanation": why,
        }
    )


# 1 Constitución
add(1, "Según el artículo 1.1 de la Constitución Española, España se constituye en un Estado:", [
    "Social y democrático de Derecho, que propugna como valores superiores la libertad, la justicia, la igualdad y el pluralismo político.",
    "Federal y democrático de Derecho, que propugna como valores superiores la libertad, la seguridad y la propiedad.",
    "Autonómico de Derecho, que propugna como valores superiores la eficacia, la jerarquía y la coordinación.",
], 0, "Artículo 1.1 CE. Los valores superiores son libertad, justicia, igualdad y pluralismo político.")

add(1, "El recurso de amparo ante el Tribunal Constitucional procede, con carácter general, para la tutela de:", [
    "Cualquier derecho reconocido en el título preliminar.",
    "Los derechos y libertades del artículo 14 y la sección primera del capítulo segundo del título I, además de la objeción de conciencia del artículo 30.",
    "Únicamente los derechos del capítulo tercero, relativos a los principios rectores de la política social y económica.",
], 1, "Artículo 53.2 CE: amparo para el art. 14, la sección 1.ª del capítulo II y el art. 30.2.")

add(1, "Los estados de alarma, de excepción y de sitio se regulan en la Constitución y se caracterizan porque:", [
    "El estado de sitio lo declara el Gobierno mediante decreto, sin intervención de las Cortes.",
    "El estado de alarma lo declara el Gobierno y el estado de sitio lo declara el Congreso por mayoría absoluta, a propuesta del Gobierno.",
    "Los tres los declara el Rey, a propuesta del Presidente del Gobierno.",
], 1, "Artículo 116 CE: alarma por el Gobierno; sitio por el Congreso por mayoría absoluta a propuesta del Gobierno.")

# 2 Organización territorial
add(2, "El artículo 137 de la Constitución dispone que el Estado se organiza territorialmente en:", [
    "Municipios, provincias y Comunidades Autónomas.",
    "Municipios, comarcas y diputaciones.",
    "Provincias, cabildos y áreas metropolitanas.",
], 0, "Artículo 137 CE. Todas gozan de autonomía para la gestión de sus respectivos intereses.")

add(2, "Conforme al artículo 140 de la Constitución, el gobierno y la administración municipal corresponden:", [
    "Al Delegado del Gobierno y a la Diputación Provincial.",
    "A los respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales.",
    "Exclusivamente al Alcalde, como órgano unipersonal.",
], 1, "Artículo 140 CE: Ayuntamientos integrados por Alcaldes y Concejales, elegidos por los vecinos.")

add(2, "En el régimen local español, el municipio:", [
    "Carece de personalidad jurídica y actúa por delegación de la Comunidad Autónoma.",
    "Es entidad local básica de la organización territorial del Estado, con personalidad jurídica y autonomía.",
    "Solo existe en los territorios que no están integrados en una provincia.",
], 1, "Artículo 11 de la Ley 7/1985, de Bases del Régimen Local, en conexión con el artículo 140 CE.")

# 3 Gobierno municipal de Madrid
add(3, "En el Ayuntamiento de Madrid, la presidencia de las sesiones del Pleno corresponde:", [
    "Al Secretario General del Pleno.",
    "Al Concejal de mayor edad.",
    "Al Alcalde.",
], 2, "El Alcalde preside el Pleno. El Secretario General asiste y levanta acta, pero no preside.")

add(3, "Los Tenientes de Alcalde del Ayuntamiento de Madrid:", [
    "Son elegidos directamente por el Pleno entre todos los vecinos.",
    "Son nombrados y cesados libremente por el Alcalde de entre los miembros de la Junta de Gobierno.",
    "Coinciden necesariamente con los titulares de todas las Áreas de Gobierno y los Coordinadores de Distrito.",
], 1, "Los nombra el Alcalde entre los miembros de la Junta de Gobierno. Sustituyen al Alcalde por el orden de su nombramiento.")

add(3, "El Pleno del Ayuntamiento de Madrid es:", [
    "El órgano de máxima representación política de los ciudadanos en el gobierno municipal.",
    "Un órgano de apoyo administrativo de la Junta de Gobierno, sin potestad normativa.",
    "El órgano encargado de la función interventora y del control financiero.",
], 0, "El Pleno representa políticamente a la ciudadanía y ejerce las competencias que le atribuyen la legislación de régimen local y el Reglamento Orgánico.")

# 4 Administración municipal
add(4, "La función pública de control interno de la gestión económica del Ayuntamiento de Madrid corresponde a:", [
    "La Tesorería municipal.",
    "La Intervención General.",
    "El Tribunal Económico-Administrativo Municipal.",
], 1, "La Intervención General ejerce la función interventora, el control financiero y el control de eficacia. El TEAM resuelve reclamaciones económico-administrativas.")

add(4, "La Agencia Tributaria Madrid es:", [
    "Un órgano desconcentrado del Ministerio de Hacienda sin personalidad propia.",
    "Un organismo autónomo del Ayuntamiento de Madrid para la gestión de los tributos municipales.",
    "Una sociedad mercantil estatal que recauda solo el IVA en la ciudad.",
], 1, "La Agencia Tributaria Madrid es el organismo autónomo municipal de gestión, inspección y recaudación tributaria.")

add(4, "El Tribunal Económico-Administrativo Municipal:", [
    "Fiscaliza en vía jurisdiccional las ordenanzas fiscales, como última instancia.",
    "Resuelve las reclamaciones económico-administrativas que se interpongan contra los actos de gestión tributaria municipal.",
    "Aprueba el presupuesto municipal y las bases de ejecución.",
], 1, "El TEAM es el órgano municipal que resuelve reclamaciones económico-administrativas, distinto de la Intervención y de la Tesorería.")

# 5 Áreas de Gobierno
add(5, "Conforme a la Ley 22/2006, de Capitalidad y de Régimen Especial de Madrid, el número, la denominación y las competencias de las Áreas de Gobierno:", [
    "Los fija el Pleno en el reglamento orgánico y no pueden modificarse durante el mandato.",
    "Los establece el Alcalde al inicio del mandato, en el marco de las normas orgánicas aprobadas por el Pleno.",
    "Los determina la Comunidad de Madrid mediante decreto del Consejo de Gobierno.",
], 1, "Artículo 14.3.h) de la Ley 22/2006: compete al Alcalde establecer, al inicio del mandato, número, denominación y competencias de las áreas.")

add(5, "El Decreto del Alcalde de 17 de junio de 2023, aún vigente como estructura del mandato y recogido en la recopilación normativa municipal de 2026, organiza la Administración ejecutiva en:", [
    "Cinco Áreas de Gobierno y veintiún gerencias de distrito.",
    "Siete Áreas de Gobierno.",
    "Una única Área de Gobierno de Economía, Innovación y Hacienda, de la que dependen el resto de concejalías.",
], 1, "El decreto establece siete áreas, entre ellas Vicealcaldía, Urbanismo, Cultura, Economía, Obras, Políticas Sociales y Vivienda.")

add(5, "En el Reglamento Orgánico del Gobierno y de la Administración del Ayuntamiento de Madrid, los órganos directivos de las Áreas de Gobierno incluyen, entre otros:", [
    "A los Secretarios Generales Técnicos y a los Directores Generales.",
    "Únicamente al Alcalde y a los Tenientes de Alcalde.",
    "A los Concejales Presidentes de los distritos, que sustituyen a los directores generales.",
], 0, "Los órganos superiores dirigen políticamente el área; Secretarios Generales Técnicos y Directores Generales son órganos directivos.")

# 6 Distritos
add(6, "El término municipal de Madrid se divide, a efectos de gestión desconcentrada, en:", [
    "10 distritos y 21 barrios.",
    "21 distritos.",
    "17 distritos, uno por cada junta de distrito histórica anterior a 1987.",
], 1, "Madrid tiene 21 distritos. Cada uno cuenta con una Junta Municipal presidida por un Concejal Presidente.")

add(6, "El Coordinador del Distrito del Ayuntamiento de Madrid ostenta, a todos los efectos, el rango de:", [
    "Director General.",
    "Titular de Área de Gobierno.",
    "Interventor delegado.",
], 0, "El Reglamento Orgánico atribuye al Coordinador del Distrito el rango de Director General. Es el órgano directivo del distrito.")

add(6, "El Concejal Presidente del distrito:", [
    "Es nombrado por el Pleno a propuesta de la oposición.",
    "Preside la Junta Municipal de Distrito y es nombrado por el Alcalde.",
    "Ejerce la función interventora de los gastos del distrito con independencia de la Intervención General.",
], 1, "El Alcalde nombra al Concejal Presidente, que preside la Junta Municipal de Distrito.")

# 7 EBEP
add(7, "El texto refundido del Estatuto Básico del Empleado Público clasifica al personal al servicio de las Administraciones Públicas en:", [
    "Funcionarios de carrera, funcionarios interinos, personal laboral y personal eventual.",
    "Únicamente funcionarios de carrera y personal directivo profesional.",
    "Funcionarios, contratados administrativos y personal de confianza política, sin personal laboral.",
], 0, "Artículo 8 del TREBEP. El personal directivo se regula aparte y no sustituye a estas cuatro clases.")

add(7, "Conforme al artículo 97 del TREBEP, las infracciones muy graves, graves y leves prescriben, respectivamente, a los:", [
    "Tres años, dos años y seis meses.",
    "Seis años, tres años y un año.",
    "Dos años, un año y un mes.",
], 0, "Artículo 97 TREBEP. Las sanciones prescriben a los tres años, dos años y un año, según sean muy graves, graves o leves.")

add(7, "La plaza de Técnico/a Medio TIC del Ayuntamiento de Madrid se encuadra en:", [
    "El subgrupo C1.",
    "El subgrupo A2.",
    "El subgrupo A1.",
], 1, "Las bases específicas la sitúan en el grupo A, subgrupo A2, Escala de Administración Especial.")

# 8 Transparencia
add(8, "La Ley 19/2013, de transparencia, acceso a la información pública y buen gobierno, se aplica:", [
    "Solo a la Administración General del Estado.",
    "A todas las Administraciones Públicas y a otros sujetos previstos en su artículo 2, incluidos determinados entes del sector público.",
    "Exclusivamente a las entidades locales de más de 50.000 habitantes.",
], 1, "El ámbito subjetivo del artículo 2 incluye AGE, CCAA, entidades locales y otros sujetos públicos y determinados privados.")

add(8, "El Consejo de Transparencia y Buen Gobierno es:", [
    "Un órgano municipal adscrito a la Junta de Gobierno del Ayuntamiento de Madrid.",
    "El organismo público estatal que vela por el cumplimiento de las obligaciones de publicidad activa y conoce de reclamaciones de acceso en su ámbito.",
    "La sala del Tribunal Constitucional competente en materia de publicidad de las normas.",
], 1, "Lo crea la Ley 19/2013. En el ámbito municipal hay que completar con la Ordenanza de Transparencia de la Ciudad de Madrid.")

add(8, "La Ordenanza de Transparencia de la Ciudad de Madrid:", [
    "Deroga en el término municipal la Ley 19/2013.",
    "Regula la transparencia de la actividad pública municipal, su ámbito de aplicación y sus principios generales.",
    "Se aplica solo a las empresas privadas que no contratan con el Ayuntamiento.",
], 1, "La Ordenanza concreta, en el ámbito del Ayuntamiento y sus organismos, las obligaciones de transparencia y los principios de la publicidad activa y del acceso.")

# 9 Ley 39/2015
add(9, "Las fases del procedimiento administrativo común son:", [
    "Iniciación, ordenación, instrucción y finalización.",
    "Alegaciones, prueba, recurso de casación y ejecución forzosa.",
    "Información pública, contrato, adjudicación y recepción.",
], 0, "Título IV de la Ley 39/2015. La terminación puede ser resolución, desistimiento, renuncia o caducidad.")

add(9, "Están obligados a relacionarse por medios electrónicos con las Administraciones Públicas, entre otros:", [
    "Solo las personas físicas, en todo caso.",
    "Las personas jurídicas y quienes ejerzan una actividad profesional que exija colegiación obligatoria, para los trámites de esa actividad.",
    "Únicamente los empleados públicos cuando actúan como interesados.",
], 1, "Artículo 14.2 de la Ley 39/2015. Las personas físicas pueden elegir el medio, salvo que una norma les imponga el electrónico.")

add(9, "Son recursos administrativos ordinarios o extraordinarios previstos en la Ley 39/2015:", [
    "Alzada, potestativo de reposición y extraordinario de revisión.",
    "Amparo, súplica y queja.",
    "Reposición, casación y unificación de doctrina.",
], 0, "Artículos 112 y siguientes. El de revisión es extraordinario y solo cabe por los motivos tasados del artículo 125.")

# 10 Ley 40/2015
add(10, "No pueden ser objeto de delegación, conforme a la Ley 40/2015:", [
    "Las competencias que una ley permita desconcentrar.",
    "La adopción de disposiciones de carácter general.",
    "Las competencias de trámite de los órganos directivos.",
], 1, "Artículo 9.2. Tampoco las competencias que se ejerzan por delegación, salvo autorización, ni las que una norma con rango de ley lo prohíba.")

add(10, "La recusación se distingue de la abstención porque:", [
    "La abstención la plantea el interesado y la recusación la decide el propio autoridad incursa en la causa.",
    "La abstención la promueve la autoridad o el personal en quien concurre la causa, y la recusación la promueve el interesado.",
    "Ambas las declara de oficio el orden jurisdiccional contencioso-administrativo.",
], 1, "Artículos 23 y 24 de la Ley 40/2015. Las causas son las mismas.")

add(10, "La responsabilidad patrimonial de la Administración exige, entre otros requisitos:", [
    "Un daño efectivo, evaluable económicamente e individualizado, antijurídico y causado por el funcionamiento del servicio, con relación de causalidad.",
    "Únicamente dolo o culpa grave del funcionario, declarada en sentencia penal.",
    "Que el perjudicado sea otro poder público.",
], 0, "Artículos 32 y siguientes de la Ley 40/2015. El daño es antijurídico cuando el particular no tiene el deber jurídico de soportarlo.")

# 11 LCSP
add(11, "Los contratos del sector público pueden estar sometidos a un régimen jurídico de:", [
    "Exclusivamente Derecho administrativo.",
    "Derecho administrativo o Derecho privado, según su calificación.",
    "Exclusivamente Derecho mercantil, aunque los celebre un ayuntamiento.",
], 1, "La LCSP distingue contratos administrativos y contratos privados, con regímenes jurídicos distintos.")

add(11, "Son principios de la contratación pública recogidos en la Ley 9/2017, entre otros:", [
    "Libertad de acceso a las licitaciones, publicidad y transparencia, no discriminación e igualdad de trato.",
    "Adjudicación directa como regla general y reserva de contratos a empresas locales.",
    "Secreto de los pliegos y preferencia por el precio más alto.",
], 0, "Artículo 1 LCSP. También la integridad, la eficiencia del gasto y la salvaguarda de la libre competencia.")

add(11, "La perfección del contrato del sector público se produce, con carácter general:", [
    "Con la publicación del anuncio de licitación.",
    "Con su formalización.",
    "Con la aprobación del expediente de contratación.",
], 1, "Artículo 36 LCSP: los contratos se perfeccionan con su formalización, salvo las excepciones legales.")

# 12 Haciendas locales
add(12, "Conforme al texto refundido de la Ley Reguladora de las Haciendas Locales, son ingresos de Derecho público de las entidades locales, entre otros:", [
    "Los tributos y los demás ingresos de Derecho público previstos en la ley.",
    "Únicamente las transferencias privadas y las donaciones.",
    "Solo los precios públicos, que tienen naturaleza tributaria.",
], 0, "El TRLRHL distingue ingresos de Derecho público e ingresos de Derecho privado. Los tributos propios son tasas, contribuciones especiales e impuestos.")

add(12, "La tasa municipal se diferencia del precio público porque la tasa:", [
    "Retribuye un servicio que el particular solicita voluntariamente y que el sector privado también presta en régimen de mercado.",
    "Se exige por la prestación de un servicio público o la realización de una actividad administrativa que se refiera, afecte o beneficie de modo particular al obligado, cuando concurre solicitud o recepción obligatoria, o por el uso privativo o el aprovechamiento especial del dominio público.",
    "Es siempre un impuesto indirecto sobre la renta de los vecinos.",
], 1, "Artículos 20 y siguientes del TRLRHL. El precio público no tiene naturaleza tributaria y responde a solicitudes voluntarias no impuestas.")

add(12, "Son impuestos municipales de exacción obligatoria:", [
    "El impuesto sobre bienes inmuebles, el impuesto sobre actividades económicas y el impuesto sobre vehículos de tracción mecánica.",
    "El IVA, el impuesto sobre sociedades y el IRPF.",
    "Únicamente el impuesto sobre construcciones, instalaciones y obras.",
], 0, "IBI, IAE e IVTM son obligatorios. ICIO e IIVTNU son potestativos.")

# 13 PRL
add(13, "Se constituirá un Comité de Seguridad y Salud en las empresas o centros de trabajo que cuenten con:", [
    "50 o más trabajadores.",
    "10 o más trabajadores.",
    "250 o más trabajadores.",
], 0, "Artículo 38 de la Ley 31/1995. Es el órgano paritario y colegiado de participación en materia de prevención.")

add(13, "Los Delegados de Prevención son:", [
    "Los técnicos del servicio de prevención ajeno designados por la mutua.",
    "Los representantes de los trabajadores con funciones específicas en materia de prevención de riesgos laborales.",
    "Los miembros del comité de empresa que hayan superado una oposición de la Inspección de Trabajo.",
], 1, "Artículo 35 LPRL. Son designados por y entre los representantes del personal, con las garantías de ese artículo.")

add(13, "En el Ayuntamiento de Madrid, la prevención de riesgos del personal funcionario y laboral se completa con:", [
    "El Acuerdo-Convenio sobre condiciones de trabajo comunes al personal funcionario y laboral del Ayuntamiento y sus organismos autónomos.",
    "El convenio colectivo único de la Comunidad de Madrid, aplicado de forma supletoria obligatoria.",
    "Únicamente el estatuto de los trabajadores, sin norma municipal específica.",
], 0, "El tema 13 remite de forma expresa a ese Acuerdo-Convenio y a la representación de los empleados públicos.")

# 14 Igualdad
add(14, "A los efectos de la Ley Orgánica 3/2007, constituye acoso sexual:", [
    "Cualquier comportamiento, verbal o físico, de naturaleza sexual que tenga el propósito o produzca el efecto de atentar contra la dignidad de una persona, en particular si crea un entorno intimidatorio, degradante u ofensivo.",
    "Cualquier comportamiento realizado en función del sexo de una persona, aunque no tenga naturaleza sexual.",
    "Solo la conducta tipificada como delito, nunca la conducta laboral que no llegue a los tribunales penales.",
], 0, "Artículo 7.1. El apartado 2 define el acoso por razón de sexo, que no exige naturaleza sexual.")

add(14, "Las obligaciones de la Ley Orgánica 3/2007 se aplican a:", [
    "Toda persona, física o jurídica, que se encuentre o actúe en territorio español, cualquiera que fuese su nacionalidad, domicilio o residencia.",
    "Solo a las personas físicas de nacionalidad española.",
    "Solo a las Administraciones Públicas, con exclusión de las empresas.",
], 0, "Artículo 2 de la Ley Orgánica 3/2007.")

add(14, "La Ley 4/2023, de 28 de febrero, tiene por objeto:", [
    "Regular exclusivamente el matrimonio igualitario.",
    "Garantizar la igualdad real y efectiva de las personas trans y los derechos de las personas LGTBI.",
    "Sustituir el Plan de Igualdad entre mujeres y hombres del Ayuntamiento de Madrid.",
], 1, "Así la define su objeto. El temario la estudia junto al Plan de Igualdad municipal entre mujeres y hombres.")

# 15 Protección de datos
add(15, "Según la Ley Orgánica 3/2018, el tratamiento de los datos personales de un menor de edad puede fundarse en su consentimiento cuando sea mayor de:", [
    "Catorce años.",
    "Dieciséis años.",
    "Dieciocho años, sin excepción.",
], 0, "Artículo 7 LOPDGDD. Por debajo de esa edad se requiere el consentimiento del titular de la patria potestad o tutela, con las excepciones de la norma.")

add(15, "Es un derecho de la persona afectada por un tratamiento de datos personales:", [
    "El derecho a la limitación del tratamiento.",
    "El derecho de reposición administrativa.",
    "El derecho a obtener siempre una resolución del Alcalde.",
], 0, "Junto al acceso, la rectificación, la supresión, la portabilidad y la oposición. Están en el RGPD y se desarrollan en la LOPDGDD.")

add(15, "El registro de actividades de tratamiento corresponde mantenerlo a:", [
    "Los responsables y los encargados del tratamiento.",
    "Exclusivamente a la Agencia Española de Protección de Datos, de oficio.",
    "Al delegado de protección de datos, que sustituye al responsable.",
], 0, "Artículo 30 RGPD y artículo 31 LOPDGDD. El DPD supervisa, pero no sustituye esa obligación del responsable y del encargado.")

# 16 ENS y ENI
add(16, "El Esquema Nacional de Seguridad vigente para las bases de esta convocatoria es el aprobado por:", [
    "El Real Decreto 311/2022, de 3 de mayo.",
    "El Real Decreto 3/2010, de 8 de enero, sin modificaciones posteriores.",
    "La Ley Orgánica 3/2018.",
], 0, "El RD 311/2022 aprueba el ENS actual y deroga el marco anterior del RD 3/2010.")

add(16, "Las dimensiones de seguridad del Esquema Nacional de Seguridad son:", [
    "Confidencialidad, integridad, trazabilidad, autenticidad y disponibilidad.",
    "Confidencialidad, integridad y disponibilidad, exclusivamente.",
    "Economía, eficacia y eficiencia.",
], 0, "La categoría del sistema es la de la dimensión de nivel más alto. Los niveles son bajo, medio y alto.")

add(16, "El Esquema Nacional de Interoperabilidad y las normas técnicas que lo desarrollan sirven para:", [
    "Fijar solo la política de copias de seguridad de los ayuntamientos.",
    "Asegurar la interoperabilidad de los sistemas y el intercambio de información entre Administraciones, incluido el documento y el expediente electrónicos.",
    "Sustituir a la Ley 39/2015 en materia de recursos administrativos.",
], 1, "El ENI se aprobó por el Real Decreto 4/2010. El documento y el expediente electrónicos forman parte de ese ciclo de vida.")

# 17 Sedes, Cl@ve, DNIe
add(17, "La sede electrónica es:", [
    "Cualquier página web municipal, aunque no identifique al titular ni los canales de acceso.",
    "La dirección electrónica disponible para la ciudadanía cuya titularidad, gestión y administración corresponden a una Administración Pública en el ejercicio de sus competencias.",
    "El registro interno de personal del departamento de recursos humanos.",
], 1, "Artículo 38 de la Ley 40/2015. La sede del Ayuntamiento es sede.madrid.es.")

add(17, "Cl@ve es:", [
    "Un sistema estatal de identificación y firma electrónica para relacionarse con las Administraciones, que el Ayuntamiento de Madrid admite junto al certificado y el DNI electrónico.",
    "La red privada de los distritos, sin salida a internet.",
    "Un certificado de sello de órgano que solo pueden usar los notarios.",
], 0, "Cl@ve es un servicio común de la Administración General del Estado. Madrid lo incorpora en su política de identificación y firma.")

add(17, "La Red SARA es:", [
    "Un conjunto de infraestructuras de comunicaciones que conecta las Administraciones españolas para prestar servicios compartidos e intercambiar información.",
    "El bus de interoperabilidad interno de un único ministerio, cerrado al resto de Administraciones.",
    "Una red social de participación ciudadana del Ayuntamiento.",
], 0, "SARA da soporte a servicios comunes y a la interconexión. No es una sede ni un sistema de identificación.")

# 18 Hardware
add(18, "Una arquitectura SMP se caracteriza porque:", [
    "Varios procesadores comparten la memoria principal y el sistema operativo gestiona esa memoria de forma común.",
    "Cada procesador tiene su propia memoria no compartida y no existe espacio de direcciones común.",
    "Solo puede existir un núcleo, aunque se virtualice.",
], 0, "SMP es multiprocesamiento simétrico con memoria compartida. MPP reparte memoria entre nodos. El cluster agrupa máquinas coordinadas.")

add(18, "Un cluster de computación, a diferencia de un único servidor SMP, se basa en:", [
    "Nodos relativamente independientes interconectados que colaboran y pueden ofrecer alta disponibilidad o alto rendimiento.",
    "Un único bus de memoria al que se conectan todos los núcleos sin red de interconexión.",
    "La prohibición de escalar horizontalmente.",
], 0, "El temario pide distinguir grid, cluster, MPP, SMP y arquitecturas multinúcleo. El cluster escala añadiendo nodos.")

# 19 Sistemas operativos
add(19, "El núcleo o kernel de un sistema operativo se encarga, entre otras funciones, de:", [
    "Gestionar procesos, memoria, dispositivos y llamadas al sistema.",
    "Sustituir al navegador en la capa de presentación.",
    "Definir el modelo entidad-relación de las aplicaciones de negocio.",
], 0, "El kernel es la parte privilegiada del sistema. Linux, Windows y los sistemas móviles organizan de forma distinta el espacio de usuario, pero comparten esa idea.")

add(19, "Un proceso y un hilo se diferencian porque:", [
    "El hilo es la unidad de planificación que comparte el espacio de direcciones del proceso, y el proceso es el contenedor de recursos.",
    "El proceso comparte siempre la memoria con el resto de procesos del sistema y el hilo no puede ejecutarse.",
    "En Linux no existen procesos, solo hilos de usuario sin kernel.",
], 0, "Varios hilos de un mismo proceso comparten memoria y archivos. Procesos distintos están aislados, salvo mecanismos expresos de comunicación.")

# 20 Paradigmas
add(20, "La programación orientada a objetos se caracteriza por:", [
    "Encapsulación, herencia y polimorfismo.",
    "La ausencia de estado y la prohibición de definir tipos.",
    "Escribir únicamente instrucciones de salto no estructurado.",
], 0, "Son los tres pilares clásicos. El paradigma funcional enfatiza funciones puras e inmutabilidad; el declarativo describe el qué, no el cómo.")

add(20, "Un lenguaje compilado se diferencia de uno interpretado porque, de forma típica:", [
    "Traduce el código fuente a código máquina o bytecode antes de la ejecución, en lugar de interpretarlo línea a línea en cada arranque.",
    "No puede distribuirse en binario y solo funciona dentro de una hoja de cálculo.",
    "Carece de sistema de tipos en todos los casos.",
], 0, "La frontera es práctica: Java compila a bytecode y una máquina virtual lo ejecuta. Python se compila a bytecode en tiempo de carga, pero se estudia como interpretado.")

# 21 Entornos de datos
add(21, "Un sistema OLTP está orientado a:", [
    "Registrar operaciones transaccionales del día a día, con muchas transacciones cortas y datos actualizados.",
    "Analizar series históricas agregadas, con consultas pesadas y datos normalmente no volátiles.",
    "Sustituir al plan de continuidad de negocio.",
], 0, "OLTP sirve a la operación. El almacén de datos y los sistemas DSS/OLAP sirven al análisis. MIS apoya la información de gestión.")

add(21, "Un almacén de datos o data warehouse se caracteriza por ser:", [
    "Orientado a temas, integrado, no volátil y con histórico.",
    "Un registro transaccional que se borra al cerrar cada jornada.",
    "Un fichero de log del cortafuegos.",
], 0, "Definición clásica de Inmon. Se alimenta por procesos de integración y se explota con OLAP o cuadros de mando.")

# 22 SGBD
add(22, "En el modelo relacional, una clave primaria:", [
    "Identifica de forma unívoca cada tupla y no admite nulos.",
    "Puede repetirse en varias filas si así lo decide el usuario en tiempo de consulta.",
    "Es siempre un campo de texto libre sin restricción.",
], 0, "La clave ajena referencia una clave candidata de otra relación y materializa la asociación.")

add(22, "JDBC, ODBC y JPA son:", [
    "Protocolos de encaminamiento de nivel de red.",
    "Estándares o especificaciones de conectividad y persistencia para acceder a bases de datos desde aplicaciones.",
    "Niveles de la categoría ENS.",
], 1, "ODBC y JDBC son APIs de acceso. JPA es la especificación Java de mapeo objeto-relacional.")

add(22, "Una base de datos documental NoSQL, frente a una relacional, organiza habitualmente la información en:", [
    "Documentos semiestructurados, por ejemplo JSON, y no exige un esquema fijo idéntico para todos los registros.",
    "Únicamente tablas en primera forma normal, sin posibilidad de anidar datos.",
    "Grafos de conmutación MPLS.",
], 0, "Otros paradigmas NoSQL son clave-valor, columnar y de grafos. No sustituyen siempre al relacional: se eligen por el modelo de acceso.")

# 23 Cliente-servidor y servicios web
add(23, "En la arquitectura cliente-servidor clásica:", [
    "El cliente inicia las peticiones y el servidor espera y las procesa.",
    "Los clientes se comunican entre sí de forma obligatoria y el servidor no responde.",
    "El servidor inicia siempre la conexión y el cliente solo escucha.",
], 0, "El cliente tiene rol activo y el servidor rol pasivo. El acoplamiento y el reparto de lógica dan lugar a clientes pesados o ligeros.")

add(23, "SOAP y REST se diferencian, de forma típica, porque:", [
    "SOAP es un protocolo basado en XML con contrato formal, y REST es un estilo de arquitectura que usa los métodos y los recursos de HTTP.",
    "REST exige siempre un WSDL y SOAP no puede ir sobre HTTP.",
    "Ambos impiden usar JSON.",
], 0, "Un servicio REST se organiza en recursos identificables por URI. SOAP describe operaciones en un sobre XML.")

# 24 TCP/IP
add(24, "El modelo TCP/IP se organiza, de abajo arriba, en las capas:", [
    "Acceso a red, internet, transporte y aplicación.",
    "Sesión, presentación y físico, únicamente.",
    "Negocio, datos y vista, al estilo MVC.",
], 0, "IP encamina en la capa de internet. TCP y UDP son la capa de transporte. HTTP o DNS viven en aplicación.")

add(24, "TCP se diferencia de UDP porque TCP:", [
    "Es orientado a conexión y ofrece control de flujo, orden y retransmisión.",
    "No tiene puertos y no puede multiplexar aplicaciones.",
    "Se usa únicamente para resolver nombres, nunca para transferir datos.",
], 0, "UDP es no orientado a conexión y no garantiza entrega ni orden. Por eso se usa en consultas DNS simples o en tráfico en tiempo real.")

# 25 Lenguajes web
add(25, "La separación estricta entre HTML, CSS y JavaScript aporta sobre todo:", [
    "Mantenimiento, reutilización, adaptación a distintos dispositivos y una estructura semántica que favorece la accesibilidad.",
    "Que el HTML se ejecute como código máquina nativo en el procesador.",
    "Eliminar la necesidad de un protocolo de transporte.",
], 0, "HTML marca la estructura, CSS la presentación y JavaScript el comportamiento. Es la base del diseño web multiplataforma del tema 48.")

add(25, "Un documento XML bien formado:", [
    "Cumple las reglas sintácticas de XML, con un único elemento raíz y etiquetas correctamente anidadas y cerradas.",
    "Es el que además ha sido firmado con el DNI electrónico.",
    "Es sinónimo de documento válido frente a cualquier DTD, aunque le falten etiquetas de cierre.",
], 0, "Bien formado es sintaxis. Válido es conformidad con un esquema, DTD o XSD. HTML5 no exige ser XML, salvo cuando se usa XHTML.")

# 26 ITIL e ISO
add(26, "ITIL v3 organiza la gestión del servicio, en su modelo de ciclo de vida, en:", [
    "Estrategia, diseño, transición, operación y mejora continua del servicio.",
    "Iniciación, ordenación, instrucción y finalización.",
    "Captura, procesado, almacenamiento y borrado.",
], 0, "El temario cita ITIL v3. ITIL 4 habla de sistema de valor del servicio y de prácticas, pero el programa pide la versión 3.")

add(26, "ISO/IEC 20000 e ISO/IEC 19770-1 se orientan, respectivamente, a:", [
    "La gestión de servicios de TI y la gestión de activos de software.",
    "La calidad de agua potable y la seguridad alimentaria.",
    "El diseño de circuitos impresos y el cableado eléctrico de sedes.",
], 0, "ISO 20000 es el estándar de gestión de servicios. ISO 19770-1 es el de gestión de activos de TI, con foco en software.")

# 27 MAGERIT y continuidad
add(27, "MAGERIT es:", [
    "La metodología española de análisis y gestión de riesgos de los sistemas de información.",
    "Un lenguaje de programación para dispositivos iOS.",
    "El registro municipal de animales potencialmente peligrosos.",
], 0, "MAGERIT trabaja con activos, amenazas, salvaguardas e impacto. Alimenta el plan de seguridad y las decisiones de continuidad.")

add(27, "Un plan de recuperación ante desastres se distingue de una simple copia de seguridad porque:", [
    "Define cómo restablecer los servicios en un tiempo y con una pérdida de datos aceptables, no solo cómo copiar ficheros.",
    "Sustituye al Esquema Nacional de Seguridad y hace innecesaria la categorización.",
    "Consiste únicamente en apagar los equipos los fines de semana.",
], 0, "La salvaguarda copia la información. El plan de contingencia mantiene el negocio y el de recuperación reconstruye el servicio. RTO y RPO concretan ese objetivo.")

# 28 Seguridad física y lógica
add(28, "En seguridad, una vulnerabilidad es:", [
    "Una debilidad que puede ser explotada por una amenaza.",
    "El daño ya materializado sobre un activo.",
    "La persona que ataca el sistema.",
], 0, "La amenaza es el evento potencial, la vulnerabilidad es la debilidad y el riesgo combina probabilidad e impacto.")

add(28, "Son medidas de seguridad lógica, a diferencia de las físicas:", [
    "El control de acceso mediante credenciales, el cifrado y el registro de auditoría.",
    "El cerramiento de la sala, el control de climatización y la detección de incendios.",
    "El peso máximo de la losa del centro de proceso de datos.",
], 0, "La seguridad física protege instalaciones y soportes. La lógica protege el acceso, la confidencialidad y la trazabilidad de la información.")

# 29 Auditoría
add(29, "La auditoría informática tiene como objetivo principal:", [
    "Verificar, con independencia, que los controles cumplen la normativa y los objetivos de la organización, y proponer mejoras.",
    "Sustituir a la explotación diaria de los sistemas.",
    "Redactar las ordenanzas fiscales.",
], 0, "El alcance puede ser de sistemas, de seguridad, de desarrollo o de explotación. La metodología fija criterios, evidencias e informe.")

add(29, "Una auditoría se diferencia del control interno permanente porque:", [
    "Es un examen puntual, con alcance definido e independencia respecto del área auditada.",
    "La ejecuta cada día el mismo operador que administra el sistema.",
    "No deja informe ni recomendaciones.",
], 0, "El control interno es continuo. La auditoría contrasta ese control y reporta a un nivel que preserve la independencia.")

# 30 CRM e IVR
add(30, "Un CRM es:", [
    "Un sistema para gestionar la relación con la ciudadanía o la clientela a lo largo de los canales de contacto.",
    "Un protocolo de encaminamiento interior de sistemas autónomos.",
    "Un formato de firma electrónica reconocida.",
], 0, "Centraliza interacciones. En un ayuntamiento soporta la atención multicanal: sede, teléfono, oficinas y redes.")

add(30, "Un IVR basado en VoiceXML permite:", [
    "Que la persona usuaria interactúe por teléfono con una aplicación, mediante voz o marcación, según un diálogo definido.",
    "Sustituir el cortafuegos perimetral.",
    "Cifrar discos duros de los portátiles municipales.",
], 0, "VoiceXML describe diálogos de voz. El IVR es el sistema de respuesta interactiva del centro de contacto.")

# 31 Software libre
add(31, "El software libre, en la acepción usual de las licencias, garantiza las libertades de:", [
    "Usar, estudiar, redistribuir y mejorar el programa.",
    "Usar el programa solo dentro de la Administración que lo compró, sin acceso al código.",
    "Patentarlo de forma automática en todos los países.",
], 0, "El código abierto se solapa, pero sus definiciones no son idénticas. Una licencia con copyleft, como la GPL, exige mantener esas libertades en las obras derivadas.")

add(31, "Los programas de ordenador se protegen jurídicamente, con carácter general, como:", [
    "Obras literarias, por la legislación de propiedad intelectual, sin perjuicio de otras protecciones.",
    "Marcas registradas, nunca como obras.",
    "Bienes de dominio público desde el momento de su creación.",
], 0, "El texto refundido de la Ley de Propiedad Intelectual protege el programa. El temario añade las tecnologías de protección de derechos digitales y los tipos de licencia.")

# 32 Viabilidad y costes
add(32, "El análisis de viabilidad de un proyecto informático debe contemplar, al menos:", [
    "La viabilidad técnica, económica y organizativa, incluidos personal, procedimientos, datos, software y hardware.",
    "Únicamente el color de la interfaz.",
    "La prohibición de estimar costes hasta que el sistema esté en producción.",
], 0, "El tema 32 pide evaluar alternativas y controlar el coste. Una alternativa técnicamente brillante puede ser inviable por coste o por encaje organizativo.")

add(32, "El control de costes de un proyecto informático sirve para:", [
    "Comparar lo planificado con lo realmente consumido y corregir desviaciones durante la ejecución.",
    "Sustituir la adjudicación del contrato por un convenio verbal.",
    "Eliminar la necesidad de un presupuesto.",
], 0, "Presupuestar sin controlar la ejecución no detecta desviaciones de plazo, alcance o dinero.")

# 33 Documática
add(33, "Un sistema de gestión documental se diferencia de un gestor de contenidos web porque el primero está orientado, sobre todo, a:", [
    "Capturar, clasificar, conservar y recuperar documentos a lo largo de su ciclo de vida, con evidencias y archivo.",
    "Posicionar palabras clave en buscadores públicos.",
    "Balancear peticiones HTTP entre servidores.",
], 0, "El gestor de contenidos publica y compone sitios. El documental gestiona el documento y su archivo. El workflow orquesta los trámites.")

add(33, "El posicionamiento en buscadores (SEO) consiste en:", [
    "Mejorar la visibilidad de un sitio en los resultados orgánicos, actuando sobre contenidos, estructura técnica y enlaces.",
    "Pagar siempre por el primer anuncio, sin cambios en el sitio.",
    "Cifrar el correo corporativo.",
], 0, "La sindicación, por ejemplo RSS, distribuye novedades. Los robots y spiders recorren la web para indexarla.")

# 34 Ciclo de vida
add(34, "En el modelo en cascada, las fases:", [
    "Se suceden de forma secuencial y cada una parte de lo aprobado en la anterior.",
    "Se repiten en espiral incorporando análisis de riesgos en cada ciclo, como rasgo definitorio de este modelo y no del de Boehm.",
    "Entregan software funcionando cada pocos días como regla del propio modelo.",
], 0, "El modelo en espiral incorpora riesgo e iteraciones. El incremental y el ágil entregan por partes. El cascada es secuencial.")

add(34, "Un modelo iterativo e incremental se caracteriza porque:", [
    "Construye el sistema en partes utilizables y va refinando el resultado en sucesivas vueltas.",
    "Impide enseñar nada al usuario hasta el último día del proyecto.",
    "No admite cambios de requisitos una vez firmado el arranque.",
], 0, "Reduce el riesgo frente a un único entregable final. El prototipado se usa para aclarar requisitos, no sustituye por sí solo a todo el ciclo.")

# 35 Métrica
add(35, "Métrica v3 estructura el desarrollo de sistemas de información en procesos entre los que están:", [
    "Planificación, desarrollo —con estudio de viabilidad, análisis, diseño, construcción e implantación— y mantenimiento.",
    "Únicamente la codificación y la puesta en producción, sin análisis.",
    "La licitación, la fiscalización y el recurso de alzada.",
], 0, "Los procesos de desarrollo son EVS, ASI, DSI, CSI e IAS. PSI es planificación y MSI es mantenimiento. Hay interfaces de gestión de proyectos, calidad y seguridad.")

add(35, "Las interfaces de Métrica v3 sirven para:", [
    "Incorporar de forma transversal la gestión de proyectos, la calidad y la seguridad en los procesos de desarrollo.",
    "Sustituir el lenguaje SQL.",
    "Definir la topología física de la red local.",
], 0, "No son fases sucesivas: acompañan a los procesos principales.")

# 36 Requisitos
add(36, "Entre las estrategias de determinación de requisitos que cita el programa están:", [
    "Entrevistas, derivación a partir de sistemas existentes, análisis y prototipos.",
    "Solo la adjudicación del contrato menor.",
    "La categorización ENS, con exclusión de cualquier contacto con las personas usuarias.",
], 0, "La entrevista recoge conocimiento tácito. El sistema existente muestra la práctica real. El prototipo valida que se ha entendido el requisito.")

add(36, "Un prototipo de requisitos es útil sobre todo para:", [
    "Comprobar con las personas usuarias que la interfaz y las reglas entendidas son las que necesitan, antes de construir el sistema definitivo.",
    "Sustituir las pruebas de aceptación y el mantenimiento.",
    "Calcular la categoría alta del ENS sin analizar activos.",
], 0, "El prototipo puede ser desechable o evolutivo. No conviene confundirlo con el sistema en producción si no se ha decidido así.")

# 37 Diagramas de flujo
add(37, "En un diagrama de flujo de datos, los elementos básicos son:", [
    "Procesos, flujos, almacenes y entidades externas.",
    "Clases, atributos y mensajes, exclusivamente.",
    "Routers, switches y VLAN.",
], 0, "El DFD muestra cómo se mueven los datos. No detalla el algoritmo interno: eso corresponde al flujograma de programa.")

add(37, "Un flujograma de sistema se diferencia de un flujograma de programa porque el primero:", [
    "Describe el recorrido de la información entre procesos, soportes y departamentos, con menos detalle algorítmico.",
    "Contiene el código fuente línea a línea.",
    "Solo puede dibujarse en UML.",
], 0, "El flujograma de programa baja al detalle de decisiones y bucles de un módulo.")

# 38 Modelización conceptual
add(38, "En la modelización conceptual, una entidad es:", [
    "Un objeto distinguible del mundo real del que se quiere guardar información.",
    "Una clave ajena ya implementada en el motor.",
    "Un índice físico de tipo árbol B.",
], 0, "Los atributos describen la entidad. El identificador la distingue. La relación asocia entidades y el rol explica cómo participa cada una.")

add(38, "La cardinalidad de una relación expresa:", [
    "Cuántas ocurrencias de una entidad se asocian con cuántas de otra.",
    "El coste en euros del proyecto.",
    "El número de servidores físicos del CPD.",
], 0, "Uno a uno, uno a muchos o muchos a muchos. La validación del modelo comprueba que esas reglas responden al negocio y no a un capricho de implementación.")

# 39 Diseño de bases de datos
add(39, "La arquitectura ANSI/SPARC de bases de datos distingue los niveles:", [
    "Externo, conceptual e interno.",
    "Físico, de enlace y de red, como en OSI.",
    "Estratégico, táctico y operativo.",
], 0, "El nivel externo son las vistas de usuario, el conceptual el esquema global y el interno la implementación física. La independencia de datos separa esos niveles.")

add(39, "La tercera forma normal exige, además de las anteriores, que:", [
    "No existan dependencias transitivas de atributos no clave respecto de la clave.",
    "Todas las tablas tengan exactamente tres columnas.",
    "Se duplique la clave primaria en cada atributo.",
], 0, "1FN: valores atómicos. 2FN: dependencia completa de la clave. 3FN: sin dependencias transitivas. La concurrencia se resuelve con bloqueos, versiones o niveles de aislamiento.")

# 40 Estructuras y algoritmos
add(40, "Una pila es una estructura de datos de tipo:", [
    "LIFO: el último elemento en entrar es el primero en salir.",
    "FIFO: el primero en entrar es el primero en salir.",
    "De acceso exclusivamente por clave hash.",
], 0, "La cola es FIFO. La lista permite inserciones según la política elegida. El árbol organiza nodos con relación padre-hijo y el grafo, nodos y aristas.")

add(40, "La búsqueda binaria sobre un vector ordenado tiene un coste típico de:", [
    "O(log n).",
    "O(n²) en el mejor caso, siempre.",
    "O(1) aunque el vector no esté ordenado.",
], 0, "Exige datos ordenados. Una búsqueda lineal es O(n). Los algoritmos de ordenación eficientes de comparación, como mergesort, son O(n log n).")

# 41 IA aplicada al software
add(41, "Aplicar inteligencia artificial al desarrollo de software puede apoyar:", [
    "El análisis de requisitos, el diseño, la estimación, la generación de pruebas y la documentación, siempre con revisión humana.",
    "La derogación de la normativa de protección de datos cuando el código lo sugiere un modelo.",
    "La sustitución automática de la firma electrónica del órgano administrativo.",
], 0, "El temario cita todo el ciclo, incluido DevOps. El resultado hay que verificarlo: el modelo puede inventar requisitos o ignorar el ENS y la protección de datos.")

add(41, "Un riesgo propio de usar modelos generativos en la construcción de software para una Administración es:", [
    "Incorporar datos personales o código de procedencia no controlada en las peticiones, o aceptar una salida incorrecta sin pruebas.",
    "Que el compilador deje de existir.",
    "La imposibilidad técnica de escribir pruebas.",
], 0, "Hay que acotar los datos que salen de la organización, revisar licencias y mantener las pruebas y la responsabilidad del equipo.")

# 42 Diseño estructurado
add(42, "Un buen diseño estructurado persigue:", [
    "Alta cohesión dentro de cada módulo y bajo acoplamiento entre módulos.",
    "Máximo acoplamiento para que cualquier cambio en un módulo obligue a reescribir el resto.",
    "Cohesión casual, mezclando en un módulo funciones sin relación.",
], 0, "La cohesión mide cuánto se relacionan las partes internas. El acoplamiento mide la dependencia entre módulos. Conviene cohesión alta y acoplamiento bajo.")

add(42, "El análisis de transformación y el análisis de transacción son técnicas para:", [
    "Derivar la estructura del programa a partir del diagrama de flujo de datos, según el tipo de problema.",
    "Calcular la categoría ENS.",
    "Elegir el impuesto municipal aplicable.",
], 0, "La transformación se usa cuando hay un flujo de entrada, un proceso central y un flujo de salida. La transacción, cuando el flujo se ramifica en varios caminos de procesamiento.")

# 43 Construcción
add(43, "Los manuales de usuario y los manuales técnicos se distinguen porque:", [
    "El de usuario explica cómo utilizar el sistema y el técnico documenta instalación, operación y mantenimiento para el personal especialista.",
    "Ambos se redactan exclusivamente en código fuente.",
    "El manual técnico se entrega a la ciudadanía en la sede y el de usuario se archiva en secreto.",
], 0, "La construcción incluye estándares de documentación, preparación de la instalación y formación, con métodos y materiales distintos para usuarios y técnicos.")

add(43, "La formación de las personas usuarias antes de la puesta en producción debe:", [
    "Adaptar el método y los materiales al perfil, y apoyarse en el manual de usuario y en casos reales del procedimiento.",
    "Limitarse a enviar el modelo de datos relacional.",
    "Sustituir las pruebas de aceptación.",
], 0, "Sin formación, un sistema bien construido fracasa en la adopción. La formación técnica del personal de explotación es otro público distinto.")

# 44 Pruebas
add(44, "Las pruebas de caja negra se diseñan:", [
    "A partir de la especificación, sin necesidad de conocer la estructura interna del código.",
    "Recorriendo cada camino del código fuente y midiendo la cobertura de sentencias.",
    "Apagando la alimentación eléctrica del CPD.",
], 0, "La caja blanca usa la estructura interna. La caja negra usa entradas y salidas esperadas. El desarrollo dirigido por pruebas escribe primero la prueba que falla.")

add(44, "El ciclo básico del desarrollo dirigido por pruebas es:", [
    "Escribir una prueba que falla, implementar lo mínimo para que pase y refactorizar.",
    "Poner el sistema en producción y, si hay quejas, escribir entonces la especificación.",
    "Generar datos reales de producción y probar solo en el entorno definitivo.",
], 0, "Rojo, verde, refactorizar. Los datos de prueba deben ser representativos y, si proceden de producción, anonimizados.")

# 45 Instalación y mantenimiento
add(45, "Una estrategia de sustitución en paralelo consiste en:", [
    "Mantener el sistema antiguo y el nuevo funcionando a la vez durante un periodo, comparando resultados.",
    "Apagar el antiguo el mismo día y quedar sin retorno.",
    "No llegar a instalar el sistema nuevo.",
], 0, "Otras estrategias son la directa, la piloto y la progresiva por fases. El paralelo reduce riesgo a costa de coste.")

add(45, "El mantenimiento perfectivo se orienta a:", [
    "Mejorar cualidades o prestaciones sin que haya una avería ni un cambio normativo que lo imponga.",
    "Corregir un defecto que impide operar.",
    "Adaptar el sistema a una norma nueva.",
], 0, "Correctivo repara fallos. Adaptativo responde a cambios del entorno. Preventivo evita fallos futuros. Perfectivo mejora.")

# 46 OO y UML
add(46, "UML es:", [
    "Un lenguaje de modelado, no una metodología completa de desarrollo.",
    "Un sustituto legal del Esquema Nacional de Interoperabilidad.",
    "Un protocolo de transporte de la capa internet.",
], 0, "El Proceso Unificado es la metodología que usa UML y se organiza en inicio, elaboración, construcción y transición. Los patrones de diseño recogen soluciones repetibles, como Observer o Factory.")

add(46, "En UML, un diagrama de secuencia muestra:", [
    "Cómo colaboran los objetos a lo largo del tiempo mediante mensajes.",
    "La topología de cableado de una VLAN.",
    "El presupuesto del contrato.",
], 0, "El diagrama de clases muestra estructura. El de casos de uso, funcionalidad visible. El de estados, el ciclo de vida de un objeto.")

# 47 Java EE
add(47, "La plataforma Java EE, hoy continuada como Jakarta EE, se caracteriza por:", [
    "Componentes gestionados por un contenedor, como aplicaciones web, lógica de negocio y persistencia, con especificaciones estándar.",
    "Ser un sistema operativo de tiempo real para centrales nucleares, sin APIs de aplicación.",
    "Impedir el uso de servicios web.",
], 0, "Servlets, JSP o equivalentes, EJB o sus sucesores, JPA y JMS son piezas clásicas. El contenedor aporta transacciones, seguridad y ciclo de vida.")

add(47, "En una aplicación Java EE clásica de tres capas, la capa de presentación web, la de negocio y la de datos se separan para:", [
    "Poder evolucionar y escalar cada una con distinta cadencia y distinto criterio de despliegue.",
    "Obligar a que la base de datos contenga el HTML de las páginas.",
    "Eliminar la necesidad de un protocolo entre navegador y servidor.",
], 0, "Es el patrón habitual de los supuestos municipales que piden servlets o servicios Java delante de una base relacional.")

# 48 Aplicaciones web
add(48, "El diseño web multiplataforma o multidispositivo implica:", [
    "Que la misma información sea utilizable en distintos tamaños de pantalla y modalidades de interacción, sin depender de un único equipo de escritorio.",
    "Publicar una imagen fija capturada en un ordenador de sobremesa.",
    "Bloquear el acceso desde teléfonos.",
], 0, "Se apoya en HTML semántico, CSS adaptable y mejora progresiva. La internacionalización separa los textos y formatos culturales del código.")

add(48, "La internacionalización y la localización se diferencian porque:", [
    "La internacionalización prepara el producto para adaptarse a idiomas y convenciones, y la localización realiza esa adaptación a un idioma o región concretos.",
    "Son sinónimos exactos.",
    "La localización consiste en geolocalizar servidores mediante GPS.",
], 0, "Se abrevian i18n y l10n. En un ayuntamiento importan el castellano y los formatos de fecha, moneda y documentos administrativos.")

# 49 JavaScript, PHP, Ruby
add(49, "JavaScript ejecutado en el navegador:", [
    "Corre en el cliente y puede manipular el documento, con las restricciones de la seguridad del navegador.",
    "Sustituye al sistema gestor de base de datos en el servidor, por definición del lenguaje.",
    "Solo puede ejecutarse si el servidor es Ruby on Rails.",
], 0, "PHP se ejecuta de forma típica en el servidor y genera la respuesta. Ruby es el lenguaje sobre el que se construyó el framework Rails, citado en el tema 25.")

add(49, "PHP se utiliza habitualmente para:", [
    "Generar páginas y servicios en el servidor, accediendo a datos y devolviendo HTML o JSON.",
    "Sustituir el protocolo IP.",
    "Definir topologías de red de área local.",
], 0, "El temario agrupa JavaScript, PHP y Ruby como tecnologías de programación web, cada una con su entorno de ejecución.")

# 50 Móviles
add(50, "El desarrollo nativo para iOS y para Android se diferencia porque:", [
    "Cada plataforma tiene sus lenguajes, kits y tiendas, y el nativo accede de forma directa a las capacidades del dispositivo.",
    "Un único binario nativo se instala sin cambios en ambos sistemas.",
    "Ninguna de las dos plataformas permite conexion en red.",
], 0, "iOS se desarrolla de forma típica con Swift y Android con Kotlin o Java. Las aproximaciones híbridas o multiplataforma comparten código a costa de depender de una capa intermedia.")

add(50, "Al elegir una aplicación móvil municipal frente a una web adaptable, un criterio decisivo es:", [
    "Si se necesitan capacidades del dispositivo, notificaciones en segundo plano o uso intensivo offline que la web no cubra con la calidad exigida.",
    "El color corporativo, exclusivamente.",
    "La prohibición legal de usar la sede electrónica.",
], 0, "La web multidispositivo cubre muchos trámites. La app nativa se justifica cuando aporta capacidades que la sede no resuelve.")

# 51 SIG, BIM, IDE
add(51, "Un sistema de información geográfica permite:", [
    "Capturar, almacenar, analizar y representar información georreferenciada.",
    "Sustituir el registro de entrada de documentos, sin componente espacial.",
    "Gestionar únicamente nóminas.",
], 0, "Los modelos vectorial y ráster son los clásicos. Una IDE publica esos datos y servicios conforme a estándares, en Europa bajo la directiva INSPIRE.")

add(51, "BIM, en relación con la información geográfica municipal, es:", [
    "Una metodología de modelado de información de la construcción, que puede integrarse con el territorio y las infraestructuras.",
    "Un protocolo de voz sobre IP.",
    "El comité de seguridad y salud.",
], 0, "BIM modela el activo construido. El SIG modela el territorio. En infraestructuras urbanas los dos se complementan.")

# 52 Calidad
add(52, "ISO/IEC 25010 define un modelo de calidad del producto software que incluye, entre otras características:", [
    "Adecuación funcional, eficiencia de desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad.",
    "Únicamente el precio del contrato.",
    "La prescripción de las faltas disciplinarias.",
], 0, "Es la referencia actual de calidad de producto. Las métricas miden esas características; no bastan las líneas de código.")

add(52, "Una métrica de software es útil cuando:", [
    "Está definida, es medible de forma repetible y se interpreta para tomar decisiones, no como un número aislado.",
    "Solo la conoce quien programa y no se registra.",
    "Sustituye las pruebas y la aceptación.",
], 0, "El tema pide modelos, métricas, normas y estándares. Medir sin umbral ni acción no mejora el producto.")

# 53 Accesibilidad y usabilidad
add(53, "El Real Decreto 1112/2018 obliga a los sitios web y aplicaciones móviles del sector público a respetar:", [
    "Los requisitos de accesibilidad de la norma armonizada, basada en las WCAG, según el nivel y el calendario que el propio real decreto fija.",
    "Únicamente una guía de estilo gráfica interna, sin exigencia legal.",
    "La prohibición de publicar sedes electrónicas.",
], 0, "La norma de referencia práctica es la EN 301 549, alineada con WCAG. Los principios son perceptible, operable, comprensible y robusto.")

add(53, "Para satisfacer el principio «comprensible» de las WCAG, una acción adecuada en un formulario municipal es:", [
    "Identificar los errores de entrada con texto claro y asociar las etiquetas a cada campo.",
    "Mostrar el error solo cambiando un borde de color rojo, sin texto.",
    "Limitar el tiempo de sesión a tres segundos sin aviso.",
], 0, "El color no puede ser el único medio. La etiqueta, las instrucciones y los mensajes de error hacen el formulario comprensible.")

# 54 Minería, OLAP, big data
add(54, "OLAP se diferencia de OLTP porque OLAP:", [
    "Consulta datos históricos y agregados para el análisis, a menudo organizados en cubos multidimensionales.",
    "Registra cada alta de un expediente en tiempo real como carga principal.",
    "Es un protocolo de encaminamiento.",
], 0, "El cubo organiza hechos y dimensiones. La minería busca patrones. El aprendizaje automático construye modelos a partir de datos.")

add(54, "En aprendizaje automático, un algoritmo supervisado se distingue de uno no supervisado porque:", [
    "Aprende a partir de ejemplos etiquetados con el resultado que se quiere predecir.",
    "No usa datos.",
    "Solo puede ejecutarse en una hoja de cálculo sin variables.",
], 0, "Clasificación y regresión son supervisadas. El agrupamiento es el ejemplo típico no supervisado. Big data añade volumen, variedad y velocidad, entre otras características.")

# 55 Administración del sistema
add(55, "La administración del sistema operativo incluye, entre otras responsabilidades:", [
    "Usuarios, parches, servicios, monitorización y control de cambios sobre el software de base.",
    "La aprobación de las ordenanzas fiscales.",
    "La representación jurídica del Ayuntamiento en los pleitos.",
], 0, "El control de cambios evita que un parche o una configuración se apliquen sin registro, prueba y posibilidad de retorno.")

add(55, "Un control de cambios eficaz sobre el software de base exige:", [
    "Registro de la petición, evaluación, prueba, autorización, implantación y verificación posterior.",
    "Aplicar el cambio directamente en producción el viernes sin dejar constancia.",
    "Que cualquier persona usuaria pueda modificar el kernel.",
], 0, "Es la misma disciplina que en la explotación de trabajos y en la gestión de configuraciones.")

# 56 Administración de BBDD
add(56, "La persona administradora de la base de datos es responsable, entre otras funciones, de:", [
    "Disponibilidad, rendimiento, seguridad de acceso, copias y recuperación del gestor.",
    "Redactar las noticias de la portada web institucional.",
    "Firmar las resoluciones de alcaldía.",
], 0, "La administración de datos, distinta de la del gestor, cuida el significado, el modelo corporativo y la calidad. Las dos aparecen en el tema 56.")

add(56, "Separar la administración de datos de la administración del gestor sirve para:", [
    "Distinguir el gobierno del significado y del modelo corporativo respecto de la operación técnica del motor.",
    "Duplicar las mismas tareas sin criterio.",
    "Evitar hacer copias de seguridad.",
], 0, "El DBA opera el SGBD. Quien administra los datos define estándares, catálogo y reglas de compartición.")

# 57 Mantenimiento de equipos
add(57, "El mantenimiento preventivo de equipos e instalaciones busca:", [
    "Reducir la probabilidad de fallo mediante revisiones y sustituciones planificadas.",
    "Actuar solo cuando el equipo ya está parado.",
    "Añadir funciones nuevas solicitadas por el negocio.",
], 0, "El correctivo repara. El perfectivo mejora. La monitorización y la gestión de capacidad anticipan saturación de CPU, memoria, disco o sala técnica.")

add(57, "La gestión de la capacidad, apoyada en la monitorización, permite:", [
    "Prever cuándo un recurso se agotará y decidir ampliaciones o cambios de arquitectura con datos.",
    "Eliminar la necesidad de copias de seguridad.",
    "Sustituir el inventario de licencias.",
], 0, "Sin línea base de uso no hay previsión. El tema enlaza con la planificación de capacidad del tema 59.")

# 58 Librerías, soportes y JCL
add(58, "Una librería de programas, en explotación, es:", [
    "El repositorio controlado de programas ejecutables y de sus versiones, desde el que se lanza la operación.",
    "La biblioteca pública de un distrito.",
    "El cajón donde se guardan los manuales en papel, sin relación con la ejecución.",
], 0, "La gestión de librerías evita ejecutar una versión no autorizada. Se complementa con el control de cambios y con los lenguajes de control de trabajos.")

add(58, "Un lenguaje de control de trabajos sirve para:", [
    "Describir al sistema qué programas ejecutar, con qué datos y en qué condiciones, de forma repetible.",
    "Diseñar el modelo entidad-relación.",
    "Sustituir el reglamento orgánico.",
], 0, "El ejemplo clásico es JCL. Las herramientas de operación automática encadenan esos trabajos y reaccionan ante incidencias.")

# 59 Control de trabajos y rendimiento
add(59, "La planificación de la capacidad se apoya en:", [
    "Medir la carga actual, proyectar la demanda y dimensionar recursos para cumplir el nivel de servicio.",
    "Comprar el doble de equipos cada mes, sin mediciones.",
    "Apagar la monitorización para no consumir CPU.",
], 0, "El análisis de la carga identifica picos, cuellos de botella y trabajos que compiten. Las herramientas de rendimiento aportan las medidas.")

add(59, "Evaluar el rendimiento de un trabajo batch consiste en:", [
    "Observar consumo de recursos, duración y cumplimiento de la ventana de ejecución, y compararlo con lo esperado.",
    "Contar solo las líneas de los comentarios del código.",
    "Revisar la ortografía del manual de usuario.",
], 0, "Si se sale de la ventana, puede afectar a la apertura del servicio en línea del día siguiente.")

# 60 Almacenamiento
add(60, "SAN, NAS y DAS se distinguen porque:", [
    "SAN ofrece almacenamiento por bloques en red, NAS ofrece ficheros en red y DAS conecta el almacenamiento directamente al servidor.",
    "Los tres son protocolos de correo.",
    "DAS es siempre un servicio de nube pública y SAN un disco USB.",
], 0, "SAN usa Fibre Channel o iSCSI. NAS usa NFS o SMB. La virtualización del almacenamiento desacopla el volumen lógico del disco físico.")

add(60, "La virtualización del almacenamiento permite:", [
    "Presentar volúmenes lógicos con independencia de los discos físicos y facilitar copias, ampliación y migración.",
    "Eliminar la necesidad de cualquier copia de seguridad.",
    "Sustituir la categorización del ENS.",
], 0, "La gestión de volúmenes agrupa discos, crea RAID lógico y asigna espacio a los sistemas sin rehacer el cableado.")

# 61 CPD
add(61, "Al planificar físicamente un centro de tratamiento de la información hay que considerar, entre otros factores:", [
    "Energía, climatización, protección contra incendios, control de acceso y dimensionamiento de la sala y de los equipos.",
    "Únicamente el color de las paredes.",
    "La cercanía a un restaurante, como único criterio.",
], 0, "Las vulnerabilidades físicas —inundación, calor, acceso no autorizado, corte eléctrico— condicionan el emplazamiento y las medidas.")

add(61, "El dimensionamiento de un CPD debe dejar margen para:", [
    "El crecimiento previsto de potencia, refrigeración y espacio, no solo para el equipo instalado el primer día.",
    "Llenar la sala al cien por cien de potencia desde el arranque, sin reserva.",
    "Eliminar los pasillos de servicio.",
], 0, "Un diseño al límite impide crecer y complica el mantenimiento. La redundancia de acometidas y de clima depende de la criticidad.")

# 62 Virtualización y cloud
add(62, "Un hipervisor de tipo 1 se ejecuta:", [
    "Directamente sobre el hardware, y sobre él corren las máquinas virtuales.",
    "Como una aplicación más de un sistema operativo de escritorio, necesariamente.",
    "Dentro de la base de datos relacional.",
], 0, "El tipo 2 se apoya en un sistema operativo anfitrión. Las particiones lógicas son otra forma de dividir un equipo, típica de plataformas grandes.")

add(62, "En un modelo de nube, IaaS se diferencia de SaaS porque en IaaS el proveedor aporta sobre todo:", [
    "Infraestructura —cómputo, red y almacenamiento— y quien contrata administra el sistema y las aplicaciones.",
    "La aplicación completa lista para usar, sin controlar el sistema operativo.",
    "Únicamente el personal de atención ciudadana de un distrito.",
], 0, "PaaS aporta la plataforma de ejecución. SaaS aporta la aplicación. La virtualización es la base habitual de estos modelos, no un sinónimo.")

# 63 LAN
add(63, "Una red de área local se caracteriza, frente a una red de área extensa, por:", [
    "Cubrir un edificio o un campus, con alta velocidad y administración propia de los equipos de acceso.",
    "Unir necesariamente continentes mediante operadores de tránsito.",
    "No poder segmentarse.",
], 0, "Topologías física y lógica no siempre coinciden. Ethernet conmutada es la base actual. La administración incluye usuarios, dispositivos, monitorización y control.")

add(63, "Segmentar una red local con VLAN sirve para:", [
    "Separar dominios de difusión y aplicar políticas distintas a colectivos o servicios que comparten el mismo cableado.",
    "Aumentar obligatoriamente el dominio de colisión de toda la organización.",
    "Sustituir el cifrado de los datos en reposo.",
], 0, "La VLAN es separación lógica. El cortafuegos entre VLAN aporta el control de qué tráfico puede pasar. No sustituye otras medidas del ENS.")

# 64 Redes IP
add(64, "IPv6 se distingue de IPv4 porque, entre otros rasgos:", [
    "Utiliza direcciones de 128 bits y no depende de NAT como mecanismo habitual de escasez de direcciones.",
    "Utiliza direcciones de 32 bits, las mismas que IPv4.",
    "Elimina la capa de transporte.",
], 0, "El temario pide técnicas y protocolos IP, calidad de servicio e IPv6. QoS prioriza tráficos, por ejemplo voz, frente a transferencias masivas.")

add(64, "La calidad de servicio en una red IP permite:", [
    "Tratar de forma distinta los flujos según su criticidad, mediante clasificación, marcado y políticas de cola.",
    "Aumentar la velocidad de la luz en la fibra.",
    "Sustituir la dirección IP de origen por el DNI de la persona usuaria.",
], 0, "DiffServ marca el tráfico en la cabecera. Sin QoS, la voz y la señalización compiten en igualdad con las copias masivas.")

# 65 Conmutación
add(65, "La conmutación de paquetes se diferencia de la conmutación de circuitos porque:", [
    "Los paquetes pueden seguir caminos y compartir enlaces, sin reservar un circuito dedicado de extremo a extremo durante toda la comunicación.",
    "Reserva un circuito físico exclusivo durante toda la llamada, como la telefonía clásica.",
    "Impide integrar voz y datos.",
], 0, "La telefonía tradicional era de circuitos. La voz sobre IP y MPLS van sobre paquetes. MPLS reenvía según etiquetas y puede ofrecer clases de servicio.")

add(65, "MPLS permite:", [
    "Conmutar tráfico según etiquetas y construir caminos con calidad de servicio, independientemente del enrutamiento IP salto a salto en cada paquete.",
    "Sustituir el protocolo HTTP en el navegador.",
    "Eliminar la necesidad de direcciones en los equipos finales.",
], 0, "Los protocolos de encaminamiento, como OSPF o BGP, siguen siendo necesarios para construir la inteligencia de la red. Ethernet conmutada es la tecnología de acceso habitual.")

# 66 Seguridad en redes
add(66, "Una firma electrónica basada en criptografía asimétrica aporta, cuando se aplica correctamente:", [
    "Autenticidad del firmante, integridad del contenido y apoyo al no repudio.",
    "Confidencialidad del documento frente a todo el mundo, incluido el destinatario.",
    "Disponibilidad del CPD ante un corte eléctrico.",
], 0, "La firma no cifra el contenido para ocultarlo: eso lo hace el cifrado. La confidencialidad y la firma se combinan cuando hace falta las dos.")

add(66, "Un cortafuegos perimetral y una VPN se complementan porque:", [
    "El cortafuegos filtra qué comunicaciones se permiten y la VPN crea un túnel cifrado para atravesar redes no confiables.",
    "Los dos sirven para lo mismo y basta con apagar uno de ellos.",
    "La VPN sustituye al control de acceso de las personas usuarias.",
], 0, "La seguridad del puesto añade otra capa: parches, antimalware, mínimo privilegio y cifrado del disco. Ninguna medida aislada cubre el tema.")

# 67 Internet e IoT
add(67, "El sistema de nombres de dominio (DNS) sirve para:", [
    "Resolver nombres legibles en direcciones y otros datos necesarios para localizar servicios en internet.",
    "Cifrar el disco del puesto de trabajo.",
    "Sustituir el registro mercantil.",
], 0, "Internet se apoya en IP, encaminamiento, DNS y protocolos de aplicación como HTTP. Comprometer el DNS desvía a la ciudadanía a sitios falsos.")

add(67, "La sensorización y el internet de las cosas añaden, frente a la informática de oficina clásica:", [
    "Gran número de dispositivos con capacidad limitada, a menudo distribuidos físicamente, que capturan datos y amplían la superficie de ataque.",
    "La desaparición de las direcciones de red.",
    "Que ya no haga falta autenticar los equipos.",
], 0, "En una ciudad, sensores de tráfico, riego o calidad del aire son IoT. Hay que inventariarlos, actualizarlos y segmentarlos.")

# 68 Comunicaciones sobre IP
add(68, "La voz sobre IP transporta la conversación:", [
    "En paquetes IP, normalmente señalizada con protocolos como SIP y con medios en tiempo real.",
    "Exclusivamente por conmutación de circuitos analógicos, sin paquetes.",
    "Mediante cartas certificadas en papel.",
], 0, "La convergencia fijo-móvil integra extensiones y terminales móviles en el mismo servicio. Los servicios multimedia añaden vídeo y datos a esa red de paquetes.")

add(68, "Para que una llamada de voz sobre IP tenga calidad aceptable hace falta, entre otras cosas:", [
    "Controlar retardo, variación del retardo y pérdida, a menudo con calidad de servicio en la red.",
    "Maximizar el retardo para que los paquetes lleguen más separados.",
    "Desactivar cualquier priorización y saturar el enlace con copias de seguridad en el mismo horario.",
], 0, "La voz es sensible al retardo y al jitter. Por eso se separa del tráfico masivo o se marca con QoS.")

# 69 Inalámbricas
add(69, "TETRA es:", [
    "Un estándar de radio troncal digital usado de forma habitual por servicios de emergencia y seguridad.",
    "Un formato de hoja de cálculo.",
    "Un impuesto municipal potestativo.",
], 0, "El temario cita la radiotelefonía móvil privada, el trunking y TETRA, distintos de la telefonía móvil pública comercial.")

add(69, "Las generaciones de telefonía móvil se suceden, de forma simplificada, como:", [
    "2G, 3G, 4G y 5G, cada una con mayor capacidad de datos y distintos servicios, desde la voz digital hasta la banda ancha móvil.",
    "Una única generación llamada LMDS, que sustituye a todas las demás.",
    "IPv4, IPv6 y SMTP.",
], 0, "LMDS, MMDS y MVDS son sistemas de acceso inalámbrico de distribución, no generaciones de telefonía móvil. Wi-Fi es una red de acceso local distinta de la red celular.")


def build():
    questions = []
    for index, item in enumerate(ITEMS, start=1):
        questions.append(
            {
                "id": f"propio-{item['topic']:02d}-{index:03d}",
                "sourceId": "banco-propio",
                "source": "Banco de refuerzo alineado con las bases de 2026",
                "category": "propio",
                "number": index,
                "stem": item["stem"],
                "choices": item["choices"],
                "answer": item["answer"],
                "topic": item["topic"],
                "origin": "elaborado",
                "explanation": item["explanation"],
            }
        )
    return questions


if __name__ == "__main__":
    from collections import Counter
    from pathlib import Path
    import json

    questions = build()
    counts = Counter(q["topic"] for q in questions)
    missing = [n for n in range(1, 70) if counts[n] < 2]
    print(f"extra={len(questions)} topics={len(counts)} missing={missing}")
    out = Path(__file__).resolve().parents[1] / "data" / "extra-questions.json"
    out.write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")

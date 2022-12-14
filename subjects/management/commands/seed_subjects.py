from django.core.management.base import BaseCommand

from reticules.models import Reticule
from subjects.models import Subject

RETICULES = [
    {
        "code": "ISIC-2010-224",
        "subjects": [
            {
                "name": "Cálculo Diferencial",
                "code": "ACF-0901",
                "semester": 1,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Fundamentos de Programación",
                "code": "AED-1285",
                "semester": 1,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Taller de Ética",
                "code": "ACA-0907",
                "semester": 1,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Matemáticas Discretas",
                "code": "AEF-1041",
                "semester": 1,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Taller de Administración",
                "code": "SCH-1024",
                "semester": 1,
                "theoretical_hours": 1,
                "practical_hours": 3,
            },
            {
                "name": "Fundamentos de Investigación",
                "code": "ACC-0906",
                "semester": 1,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Cálculo Integral",
                "code": "ACF-0902",
                "semester": 2,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Programación Orientada a Objetos",
                "code": "AED-1286",
                "semester": 2,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Contabilidad Financiera",
                "code": "AEC-1008",
                "semester": 2,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Química",
                "code": "AEC-1058",
                "semester": 2,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Álgebra Lineal",
                "code": "ACF-0903",
                "semester": 2,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Probabilidad y Estadística",
                "code": "AEF-1052",
                "semester": 2,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Cálculo Vectorial",
                "code": "ACF-0904",
                "semester": 3,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Estructura de Datos",
                "code": "AED-1026",
                "semester": 3,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Cultura Empresarial",
                "code": "SCC-1005",
                "semester": 3,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Investigación de Operaciones",
                "code": "SCC-1013",
                "semester": 3,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Desarrollo Sustentable",
                "code": "ACD-0908",
                "semester": 3,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Física General",
                "code": "SCF-1006",
                "semester": 3,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Ecuaciones Diferenciales",
                "code": "ACF-0905",
                "semester": 4,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Métodos Numéricos",
                "code": "SCC-1017",
                "semester": 4,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Tópicos Avanzados de Programación",
                "code": "SCD-1027",
                "semester": 4,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Fundamentos de Base de Datos",
                "code": "AEF-1031",
                "semester": 4,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Simulación",
                "code": "SCD-1022",
                "semester": 4,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Principios Eléctricos y Aplicaciones Digitales",
                "code": "SCD-1018",
                "semester": 4,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Graficación",
                "code": "SCC-1010",
                "semester": 5,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Fundamentos de Telecomunicaciones",
                "code": "AEC-1034",
                "semester": 5,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Sistemas Operativos",
                "code": "AEC-1061",
                "semester": 5,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Taller de Base de Datos",
                "code": "SCA-1025",
                "semester": 5,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Fundamentos de Ingeniería de Software",
                "code": "SCC-1007",
                "semester": 5,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Arquitectura de Computadoras",
                "code": "SCD-1003",
                "semester": 5,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Lenguajes y Autómatas I",
                "code": "SCD-1015",
                "semester": 6,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Redes de Computadoras",
                "code": "SCD-1021",
                "semester": 6,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Taller de Sistemas Operativos",
                "code": "SCA-1026",
                "semester": 6,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Administración de Base de Datos",
                "code": "SCB-1001",
                "semester": 6,
                "theoretical_hours": 1,
                "practical_hours": 4,
            },
            {
                "name": "Inegniería de Software",
                "code": "SCD-1011",
                "semester": 6,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Lenguajes de Interfaz",
                "code": "SCC-1014",
                "semester": 6,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Lenguajes y Autómatas II",
                "code": "SCD-1016",
                "semester": 7,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Conmutación y Enrutamiento en Redes de Datos",
                "code": "SCD-1004",
                "semester": 7,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Taller de Investigación I",
                "code": "ACA-0909",
                "semester": 7,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Gestión de Proyectos de Software",
                "code": "SCG-1009",
                "semester": 7,
                "theoretical_hours": 3,
                "practical_hours": 3,
            },
            {
                "name": "Sistemas Programables",
                "code": "SCC-1023",
                "semester": 7,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Programación Lógica y Funcional",
                "code": "SCC-1019",
                "semester": 8,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Administración de Redes",
                "code": "SCA-1002",
                "semester": 8,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Taller de Investigación II",
                "code": "ACA-0910",
                "semester": 8,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Programación Web",
                "code": "AEB-1055",
                "semester": 8,
                "theoretical_hours": 1,
                "practical_hours": 4,
            },
            {
                "name": "Inteligencia Artificial",
                "code": "SCC-1012",
                "semester": 9,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Residencia Profesional",
                "code": "None",
                "semester": 9,
                "theoretical_hours": 0,
                "practical_hours": 0,
            },
            {
                "name": "Especialidad",
                "code": "None",
                "semester": 9,
                "theoretical_hours": 0,
                "practical_hours": 0,
            },
        ],
    },
    {
        "code": "ITIC-2010-225",
        "subjects": [
            {
                "name": "Cálculo Diferencial",
                "code": "ACF-0901",
                "semester": 1,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Fundamentos de Programación",
                "code": "AED-1285",
                "semester": 1,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Matemáticas Discretas I",
                "code": "TIF-1019",
                "semester": 1,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Introducción a las TIC's",
                "code": "TIP-1017",
                "semester": 1,
                "theoretical_hours": 3,
                "practical_hours": 0,
            },
            {
                "name": "Taller de Ética",
                "code": "ACA-0907",
                "semester": 1,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Fundamentos de investigación",
                "code": "ACC-0906",
                "semester": 1,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Cálculo Integral",
                "code": "ACF-0902",
                "semester": 2,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Programación Orientada a Objetos",
                "code": "AEB-1054",
                "semester": 2,
                "theoretical_hours": 1,
                "practical_hours": 4,
            },
            {
                "name": "Matemáticas Discretas II",
                "code": "TIF-1020",
                "semester": 2,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Álgebra Lineal",
                "code": "ACF-0903",
                "semester": 2,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Probabilidad y Estadística",
                "code": "AEF-1052",
                "semester": 2,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Contabilidad y Costos",
                "code": "TIF-1009",
                "semester": 2,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Estructuras y Optimización de Datos",
                "code": "TIF-1012",
                "semester": 3,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Matemáticas praa la Toma de Decisiones",
                "code": "TIF-1021",
                "semester": 3,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Fundamentos de Base de Datos",
                "code": "AEF-1031",
                "semester": 3,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Electricidad y Magnetísmo",
                "code": "TIC-1011",
                "semester": 3,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Administración Gerencial",
                "code": "TIC-1002",
                "semester": 3,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Matemáticas Aplicadas a Comunicaciones",
                "code": "TIE-1018",
                "semester": 4,
                "theoretical_hours": 3,
                "practical_hours": 1,
            },
            {
                "name": "Programación II",
                "code": "TIB-1024",
                "semester": 4,
                "theoretical_hours": 1,
                "practical_hours": 4,
            },
            {
                "name": "Fundamentos de Redes",
                "code": "TIF-1013",
                "semester": 4,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Taller de Base de Datos",
                "code": "AEA-1063",
                "semester": 4,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Circuitos Eléctricos y Electrónicos",
                "code": "TID-1008",
                "semester": 4,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Ingeniería de Software",
                "code": "TIC-1014",
                "semester": 4,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Análisis de Señales y Sistemas de Comunicación",
                "code": "TID-1004",
                "semester": 5,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Administración de Proyectos",
                "code": "TIF-1001",
                "semester": 5,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Redes de Computadoras",
                "code": "TIF-1025",
                "semester": 5,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Base de Datos Distribuidas",
                "code": "TIF-1007",
                "semester": 5,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Arquitectura de Computadoras",
                "code": "TIC-1005",
                "semester": 5,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Taller de Inegniería de Software",
                "code": "TIC-1027",
                "semester": 5,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Telecomunicaciones",
                "code": "TIF-1029",
                "semester": 6,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Programación Web",
                "code": "AEB-1055",
                "semester": 6,
                "theoretical_hours": 1,
                "practical_hours": 4,
            },
            {
                "name": "Desarrollo de Emprendedores",
                "code": "TID-1010",
                "semester": 6,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Sistemas Operativos I",
                "code": "AEC-1061",
                "semester": 6,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Desarrollo Sustentable",
                "code": "ACD-0908",
                "semester": 6,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Tecnologías Inalámbricas",
                "code": "TIC-1028",
                "semester": 6,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Redes Emergentes",
                "code": "TIF-1026",
                "semester": 7,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Desarrollo de Aplicaciones para Dispositivos Móviles",
                "code": "AEB-1011",
                "semester": 7,
                "theoretical_hours": 1,
                "practical_hours": 4,
            },
            {
                "name": "Taller de Investigación I",
                "code": "ACA-0909",
                "semester": 7,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Sistemas Operativos II",
                "code": "AED-1062",
                "semester": 7,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
            {
                "name": "Negocios Eletrónicos I",
                "code": "TIC-1022",
                "semester": 7,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Interacción Humano Computadora",
                "code": "TIH-1016",
                "semester": 7,
                "theoretical_hours": 1,
                "practical_hours": 3,
            },
            {
                "name": "Administración y Seguridad de Redes",
                "code": "TIB-1003",
                "semester": 8,
                "theoretical_hours": 1,
                "practical_hours": 4,
            },
            {
                "name": "Auditoría en Tecnologías de la Información",
                "code": "TIC-1006",
                "semester": 8,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Taller de Investigación II",
                "code": "ACA-0910",
                "semester": 8,
                "theoretical_hours": 0,
                "practical_hours": 4,
            },
            {
                "name": "Ingeniería del Conocimiento",
                "code": "TIC-1015",
                "semester": 8,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Negocios Electrónicos II",
                "code": "TIC-1023",
                "semester": 8,
                "theoretical_hours": 2,
                "practical_hours": 2,
            },
            {
                "name": "Residencia Profesional",
                "code": "None",
                "semester": 9,
                "theoretical_hours": 0,
                "practical_hours": 0,
            },
            {
                "name": "Especialidad",
                "code": "None",
                "semester": 9,
                "theoretical_hours": 0,
                "practical_hours": 0,
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed reticules"

    def handle(self, *args, **options):
        for reticule_data in RETICULES:
            reticule = Reticule.objects.filter(code=reticule_data["code"]).first()

            if not reticule:
                continue

            for subject in reticule_data["subjects"]:
                Subject.objects.get_or_create(reticule=reticule, **subject)

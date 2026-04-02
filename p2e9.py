students = [
    {"name": " Ana García ", "grade": "8", "status": "aprobado"},
    {"name": "pedro lópez", "grade": "4", "status": "DESAPROBADO"},
    {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status": "Aprobado"},
    {"name": "ana garcía", "grade": "9", "status": "aprobado"},
    {"name": None, "grade": "7", "status": "aprobado"},
    {"name": "Luis Martínez ", "grade": None, "status": "aprobado"},
    {"name": " carlos RUIZ", "grade": "6", "status": "aprobado"},
    {"name": "PEDRO LÓPEZ ", "grade": "3", "status": "desaprobado"},
    {"name": " ", "grade": "5", "status": "aprobado"},
    {"name": "María Fernández", "grade": "7", "status": "APROBADO"},
    {"name": "Sofía Torres", "grade": "9", "status": "Aprobado"},
    {"name": " sofía torres ", "grade": "8", "status": "aprobado"},
    {"name": "Carlos Ruiz", "grade": "6", "status": "APROBADO"},
    {"name": "Roberto Díaz", "grade": "absent", "status": "ausente"},
    {"name": "roberto díaz", "grade": "", "status": "Ausente"},
    {"name": None, "grade": None, "status": None},
    {"name": "Laura Méndez", "grade": "7", "status": "aprobado"},
    {"name": " laura méndez", "grade": "8", "status": "Aprobado"},
    {"name": "GABRIELA RÍOS", "grade": "5", "status": "aprobado"},
    {"name": "gabriela ríos ", "grade": "4", "status": "Desaprobado"},
]

alumnos = {}

for est in students:
    nombre = est["name"]
    nota = est["grade"]
    estado = est["status"]

    #validar nombre
    if not nombre or nombre.strip() == "":
        continue

    # Validar nota
    if not nota or not nota.isdigit():
        continue

    # normalizar
    nombre = nombre.strip().title()
    estado = estado.strip().title()
    nota = int(nota)

    #  Eliminar los dupicados
    if nombre not in alumnos or nota > alumnos[nombre]["grade"]:
        alumnos[nombre] = {"grade": nota, "status": estado}

# Ordenar
ordenados = sorted(alumnos.items())

# salida
print("Registros limpios de alumnos:")
print("Nombre              Nota Estado")
print("------------------------------------------")

for nombre, datos in ordenados:
    print(f"{nombre} {datos['grade']}    {datos['status']}")



print(f" Total de alumnos válidos: {len(ordenados)}")
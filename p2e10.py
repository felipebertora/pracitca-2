rounds = [
{
'theme': 'Entrada',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Santiago': {'judge_1': 6, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 8},
}
},
{
'theme': 'Plato principal',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Mateo': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Camila': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Lucía': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
}
},
{
'theme': 'Postre',
'scores': {
'Valentina': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Mateo': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Santiago': {'judge_1': 7, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
}
},
{
'theme': 'Cocina internacional',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 9,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Santiago': {'judge_1': 8, 'judge_2': 9,
'judge_3': 7},
'Lucía': {'judge_1': 7, 'judge_2': 7,
'judge_3': 8},
}
},
{
'theme': 'Final libre',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 8,
'judge_3': 9},
'Mateo': {'judge_1': 8, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 7, 'judge_2': 7,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 7},
}
}
]


estadisticas = {}

for i, ronda in enumerate(rounds, start=1):
    print(f" Ronda {i} - {ronda['theme']}:")

    puntajes_ronda = {}

    for nombre, jueces in ronda["scores"].items():
        total = sum(jueces.values())
        puntajes_ronda[nombre] = total

    ganador = max(puntajes_ronda, key=puntajes_ronda.get)
    print(f"Ganador: {ganador} ({puntajes_ronda[ganador]} pts)")

    for nombre, puntos in puntajes_ronda.items():

        if nombre not in estadisticas:
            estadisticas[nombre] = {
                "total": 0,
                "ganadas": 0,
                "mejor": 0,
                "rondas": 0
            }

        estadisticas[nombre]["total"] += puntos
        estadisticas[nombre]["rondas"] += 1

        if puntos > estadisticas[nombre]["mejor"]:
            estadisticas[nombre]["mejor"] = puntos

    estadisticas[ganador]["ganadas"] += 1

    # tabla parcial
    ordenados = sorted(estadisticas.items(), key=lambda x: x[1]["total"], reverse=True)
    for nombre, datos in ordenados:
        print(nombre, datos["total"])

# tabla final
print("\nTabla final:\n")

ordenados = sorted(estadisticas.items(), key=lambda x: x[1]["total"], reverse=True)

for nombre, datos in ordenados:
    promedio = datos["total"] / datos["rondas"]
    print(f"{nombre} {datos['total']} {datos['ganadas']} {datos['mejor']} {promedio:.1f}")
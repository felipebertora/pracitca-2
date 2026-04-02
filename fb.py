playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

max = 0
min = 9999
total = 0

for tema in playlist:
    duration_str = tema["duration"]
    minutos = duration_str.split(":")
    segundos = int(minutos[0]) * 60 + int(minutos[1])

    total  = total + segundos
    
    if(segundos > max):
        max = segundos
        cmax = tema["title"]
    else:
        if segundos< min:
            min = segundos
            cmin = tema["title"]


seg_adicionales = total % 60
total = total // 60
print(f"duracion total: {total}m {seg_adicionales}s")

seg_adicionales = max % 60
max = max // 60
print("cancion con mayor duracion: ", cmax, f"con {max}m {seg_adicionales}s" )
seg_adicionales = min % 60
min = min // 60
print("cancion con mayor duracion: ", cmin, f"con {min}m {seg_adicionales}s" )

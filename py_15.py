#se decea saber que grupo de primero obtuvo el mejor promedio, cada grupo puede tener distinta cantidad de alumnos
#al final diga que carrera es y el promedio que obtuvo cada salon y sus carreras.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def resultado():
    global promax, grumax, carmax
    mejor=f"el grupo con mejor promedio fue: {grumax}\n de la carrera: {carmax}\n con un promedio de: {str(promax)}\n"
    engine.say(mejor)
    engine.runAndWait()
    result2.value=mejor

promax=0.0
grumax=""
carmax=""
conca=""
def agg():
    global promax, grumax, carmax, promedio, i, conca
    promedio=promedio/int(nal.value)
    if promedio>promax:
        promax=promedio
        grumax=str(gru.value)
        carmax=str(car.value)

    conca=conca+f"grupo: {gru.value}, carrera: {car.value}, promedio: {str(promedio)}\n"
    i=1
    gru.value=""
    car.value=""
    nal.value=""
    calf.value=""
    message4.value=f"calificacion {i}:"
    result.value=conca
    promedio=0.0

promedio=0.0
def calis():
    global promedio, i
    promedio = promedio + float(calf.value)
    i=i+1
    calf.value=""
    if i>int(nal.value):
        message4.value="presiona \"Agg grupo\""
    else:
        message4.value=f"calificacion {i}:"

def mensaje():
    cadena="ingresa los datos del grupo y las calificaciones de los alumnos y guardalos uno por uno"
    engine.say(cadena)
    engine.runAndWait()

i=1
app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text="grupo:")
gru = TextBox(app, width=20,)
message2 = Text(app, text="carrera:")
car = TextBox(app, width=20,)
message3 = Text(app, text="numero de alumnos:")
nal = TextBox(app, width=20,)
message4 = Text(app, text=f"calificacion {i}:")
calf = TextBox(app, width=20,)

button2=PushButton(app,text="Agg calificacion", command=calis)
button3=PushButton(app,text="Agg grupo", command=agg)
button4=PushButton(app,text="terminar:", command=resultado)
result= Text(app,text="")
result2= Text(app,text="")
app.display()
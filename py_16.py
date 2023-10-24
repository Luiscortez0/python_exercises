#se desea conocer: -calificacion mayor, calificacion menor, cuantos reprobaron (<6), cuantos pasaron (>=6)
#de n alumnos en un grupo.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def resultado():
    global promax,promin,aprovados,reprobados
    cadena=f"-calificacion mayor: {promax}\n -calificacion menor: {promin}\n -aprobaron: {aprovados}\n -reprobaron: {reprobados}"
    engine.say(cadena)
    engine.runAndWait()
    result.value=cadena

promax:float=0.0
promin:float=100
aprovados:int=0
reprobados:int=0
def agg():
    global promax,promin,aprovados,reprobados,i,promedio
    if float(calf.value) >promax:
        promax=float(calf.value)
    if float(calf.value) <promin:
        promin=float(calf.value)  
    if float(calf.value)>=6:
        aprovados+=1
    if float(calf.value)<6:
        reprobados+=1
        
    i+=1
    message.value=f"alumno {i}:"
    calf.value=""

def mensaje():
    cadena="ingresa la calificacion de cada uno de los estudiantes uno por uno"
    engine.say(cadena)
    engine.runAndWait()

i=1
app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text=f"alumno {i}:")
message2 = Text(app, text="calificacion:")
calf = TextBox(app, width=20,)

button2=PushButton(app,text="Guardar calificacion", command=agg)
button3=PushButton(app,text="terminar:", command=resultado)
result= Text(app,text="")
app.display()
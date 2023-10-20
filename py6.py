#se desea saber la cantidad de alumnos que aprobaron una materia la calificacion aprobatoria es de 7.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

ap:int=0
rp:int=0
def suma():
    global ap,rp
    if int(calf.value)>=7:
        ap+=1
    else:
        rp+=1

    calf.value=""

def aprobados():
    cadena=f"aprobaron: {ap} alumnos y {rp} reprobaron"
    engine.say(cadena)
    engine.runAndWait()
    result.value=cadena

def mensaje():
    cadena="ingresa n calficaciones y guardalas una por una"
    engine.say(cadena)
    engine.runAndWait()


app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message2 = Text(app, text="ingresa una calificacion:")
calf= TextBox(app, width=20,)
button2=PushButton(app,text="Agg otra calificacion", command=suma)
button3=PushButton(app,text="aprobados:", command=aprobados)
result= Text(app,text="")
app.display()
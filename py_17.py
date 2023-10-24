#la cafeteria de la escuela debe de vender productos a n numeros de alumnos, ofrece:
#tacos, tortas, hotdogs, pizzas; se desea saber las vendas durante el dia.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def ventas():
    global to,ta,ho,pi
    if int(n.value)==1:
        to+=1
    elif int(n.value)==2:
        ta+=1
    elif int(n.value)==3:
        ho+=1
    elif int(n.value)==4:
        pi+=1
    elif int(n.value)==5:
        result.value=f"ventas hasta el momento:\n -tortas:{to}\n -tacos:{ta}\n -hotdogs:{ho} \n -pizzas:{pi}"
        engine.say(result.value)
        engine.runAndWait()
    elif int(n.value)==6:
        result.value=f"ventas totales del dia:\n -tortas:{to}\n -tacos:{ta}\n -hotdogs:{ho} \n -pizzas:{pi}"
        engine.say(result.value)
        engine.runAndWait()
    else:
        result.value="Opcion no valida"
        engine.say(result.value)
        engine.runAndWait()
        n.value=""
    
    n.value=""

def mensaje():
    cadena="ingresa un numero del 1 al 6 acorde a la opcion que deseas seleccionar"
    engine.say(cadena)
    engine.runAndWait()

to=0
ta=0
ho=0
pi=0
app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
memu = Text(app, text="MENU:\n 1.tortas\n 2.tacos\n 3.hotdogs\n 4.pizzas\n 5.reporte de ventas\n 6.terminar")
message = Text(app, text="numero de opcion deseada:")
n = TextBox(app, width=20,)
button2=PushButton(app,text="seleccionar", command=ventas)
result= Text(app,text="")
app.display()
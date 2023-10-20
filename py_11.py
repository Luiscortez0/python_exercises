# una empresa desea calcular el sueldo total de una persona bajo los siguientes rubros,
#persepciones: sueldo base, 5% canasta basica, 3% prima de antiguedad, y deduciones;
#si el salario base exede los $10,000 el isr es de 30% y menos de  $10,000 es 20%;
#indique cuanto es el total de nomina a pagar y el total de impuestos a pagar al sat.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

a=1
tnomina=0
timpuesto=0
def calcular():
    global tnomina, timpuesto ,a
    isr=0
    if a<=int(n.value):
        if int(sal.value)>10000:
            timpuesto = timpuesto + (int(sal.value)*0.30)
        else:
            timpuesto = timpuesto + (int(sal.value)*0.20)
            canasta = int(sal.value)*0.05
            prima = int(sal.value)*0.03
            nomina = int(sal.value) + canasta + prima
            tnomina = tnomina + nomina

        a=a+1
        message2.value=f"salario del empleado {a}:"
        sal.value=""
    else:
         cadena=f"el total de la nomina de empleados es: {str(tnomina)} y el total de impuestos es: {str(timpuesto)}"
         engine.say(cadena)
         engine.runAndWait()
         result.value=f"total nomina: {str(tnomina)}, total impuestos: {str(timpuesto)}"

def mensaje():
    cadena="ingresa los salarios de tus empleados y guardalos uno por uno"
    engine.say(cadena)
    engine.runAndWait()

app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text=f"cuantos empleados son:")
n = TextBox(app, width=20,)
message2 = Text(app, text=f"salario del empleado {a}:")
sal = TextBox(app, width=20,)
button2=PushButton(app,text="siguiente empleado / terminar", command=calcular)
result= Text(app,text="")
app.display()
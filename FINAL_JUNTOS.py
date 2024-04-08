from tkinter import *
from tkinter import ttk
from FuncionesProyecto import *
import math

###############################################      funciones programa      #################################################
def conjeturaGoldbach():
    n=valor0.get()
    enseñarValor.config(text="El número ingresado es: "+str(n))

    if n>2 and n%2==0:
        respuesta.config(text=str(sumaPrimosPar(n)))
    else:
        respuesta.config(text="¡¡Debes de digitar un número entero mayor a 2 y que sea par!!")

def numTriangular():
    num = valor2.get()  
    num_label.config(text=num)
    Result = NumeroTriangular(num)
    ResultG = triangulo(num)
    Respuesta = str(Result)
    Respuesta2 = str(ResultG)
    
    respuestaC.config(text=Respuesta)
    respuesta2C.config(text=Respuesta2)

def TrianguloPascal():
    Filas = NF.get()   
    n=0
    m=0
    res="" 
    F = "" 
    if Filas <1 :
        res="La cantidad de filas debe ser mayor a 0"
    else:
        for i in range(0, Filas):
            F=""
            while m<=n:
                val = int(math.factorial(n)/((math.factorial(m))*math.factorial(n-m)))
                m+=1
            
                F+= str(val) + " "       
            res += F +"\n"            
            n+=1
            m=0
    Respuesta1.config(text= res)


###############################################      ventana principal      #################################################

root = Tk()
root.title("Curiosidades numéricas")
root.geometry("1400x500+50+50")

notebook = ttk.Notebook(root)
notebook.grid()

pes0 = ttk.Frame(notebook)
pes1 = ttk.Frame(notebook)
pes2 = ttk.Frame(notebook)
pes3 = ttk.Frame(notebook)
pes4 = ttk.Frame(notebook)
notebook.config(width=1400, height=1100)
notebook.add(pes0, text="Conjetura de Goldbach")
notebook.add(pes1, text="Triangulo de Pascal")
notebook.add(pes2, text="Número Triangular")
notebook.add(pes3, text="Números amigos")
notebook.add(pes4, text="El 153")




###################################################      pestaña 0      #####################################################

Label(pes0, text="Bienvenido al programa para verificar la conjetura de goldbach\nIngrese un número entero mayor a 2 y par: \n").grid(row=0, column=0, sticky="NS")

Label(pes0, text="    Número:").grid(row=1, column=0, sticky=W)

valor0=IntVar()
txtValor=Entry(pes0, textvariable=valor0, width=8).grid(row=1, column=0, sticky=NS)
valor0.get()

boton=Button(pes0, text="MOSTRAR", command=conjeturaGoldbach).grid(row=1, column=0, sticky=E)

Label(pes0).grid(row=2)

enseñarValor=Label(pes0, text="")
enseñarValor.grid(row=3, column=0)

respuesta=Label(pes0, text="")
respuesta.grid(row=4, column=0)




###################################################      pestaña 1      #####################################################

Label(pes1, text="Triangulo de Pascal", foreground="Blue").grid(row=0 ,column=0 )
Label(pes1, text="Ingrese la cantidad de filas a mostrar: \n").grid(row=1,column=0)

NF=IntVar()
txtNC=Entry(pes1, textvariable=NF, width=5).grid(row=2, column=0, sticky=N+W)
NF.get()

Button(pes1, text="Ver triangulo", command=TrianguloPascal).grid(row=2, column=0, sticky=N+E)
Respuesta1=Label(pes1, text="")
Respuesta1.grid(row=2, column=0, sticky=S)

Label(pes1, text="El triangulo de Pascal es un árbol invertido donde todos sus bordes son 1 y los valores internos son la suma de los dos valores que se encuentren justo\n por encima de él.", borderwidth=2, relief=SOLID, justify=LEFT).grid(row=1, column=2, columnspan=2)

Label(pes1, text="             ").grid(row=1, column=1)
Codigo=Label(pes1, text="""Codigo: 
      def TrianguloPascal():
    Filas = NF.get()   
    n=0
    m=0
    res="" 
    F = "" 
    if Filas <1 :
        res="La cantidad de filas debe ser mayor a 0"
    else:
        for i in range(0, Filas):
            F=""
            while m<=n:
                val = int(math.factorial(n)/((math.factorial(m))*math.factorial(n-m)))
                m+=1
            
                F+= str(val) + " "       
            res += F +"/n "            
            n+=1
            m=0
    Respuesta.config(text= res)
             

             
      """, borderwidth=2, relief=SOLID, justify=LEFT, height=25 )
Codigo.grid(row=2,column=2, sticky=W)
Label(pes1, text="""Explicación: 
      La función TrianguloPascal() recibe el valor introducido 
      por el usuario, esta función tiene un ciclo que va desde 0 
      hasta el numero ingresado y va generando en cada iteración 
      una nueva fila del triangulo,

      dentro de cada una de estas iteraciones hay un while que se 
      repetirá hasta que se capturen todos los valores de la fila actual, 
      estos se van guardando en la variable "F",

      finalmente la variable res se va actualizando en cada iteracion y 
      va guardando cada una de las filas por medio de la variable "F".

      

      








      """, anchor=W, borderwidth=2, relief=SOLID, height=25, justify=LEFT ).grid(row=2,column=3,sticky=E)




###################################################      pestaña 2      #####################################################

Label(pes2, text="Número Triangular\n--------------------------------------------------------------------------------------------------------", foreground="Blue").grid(row=0, column=3)
Label(pes2, text="ingrese un número entre 2 y 20:").grid(row=1, column=0, sticky=W)

valor2=IntVar()
txtValor = Entry(pes2, textvariable=valor2, width=8)
txtValor.grid(row=2, column=0,)

boton = Button(pes2, text="Mostrar", command=numTriangular)
boton.grid(row=2, column=1)

num_label = Label(pes2, text="")

respuestaC = Label(pes2, text="")
respuestaC.grid(row=3, column=0, sticky=N)

respuesta2C = Label(pes2, text="")
respuesta2C.grid(row=4, column=0, sticky=N)

Label(pes2, text="Es aquel que puede recomponerse en la forma de un triángulo equilátero\n(por convención, el primer número triangular es el 1).", borderwidth=2, relief=SOLID, justify=LEFT).grid(row=1, column=3, columnspan=2)

Label(pes2, text="             ").grid(row=2, column=3)
CodigoT=Label(pes2, text="""Codigo: 
def NumeroTriangular (n):
    if 2 <= n and n <= 20:
        x=int(0)
        sum=int(1)
        resultado=bool()
        respuesta=""
        while x < n:
                x += sum
                if x == n:
                    resultado==True
                    respuesta = str("El número " + str(n) + " es un número triangular, debido a que con este se puede contruir un trángulo equilátero")
                    return respuesta
                sum += 1
        if resultado != True:
            respuesta = str("El número " + str(n) + " NO es un número triangular, debido a que con este NO se puede contruir un trángulo equilátero")
            return respuesta
    else:
        novalido=""
        novalido="Número no válido, el número debe estar entre 2 y 20"
        return novalido

             
      """, borderwidth=2, relief=SOLID, justify=LEFT, height=25 )
CodigoT.grid(row=4,column=3, sticky=SW)
Label(pes2, text=
      
      
      
      """Explicación: 
      
      
      La Función "NumeroTriangular()" recibe el valor introducido 
      por el usuario (solo permite los números enteros entre 2 y 20).
      
      Posee un while que va sumando un valor "x" que es cero y en cada
      repetición suma 1+ que en la anterior, eso lo hace mientras "x" sea 
      menor al número ingresado por el usuario

      finalmente si alguna de las sumas a la "x" llega a ser igual al
      número, significa que el número es triangular y retorna esa respuesta.

      -------------------------------------------------------------------------

      La función triangulo() recibe el valor introducido por el
      usuario (solo permite los números enteros entre 2 y 20).
      
      Usa un "for" que va desde 0 hasta el numero ingresado y va
      agregando a una variable "resultado" un punto + por cada fila
      y la cantidad de puntos agragados, debe ser la misma cantidad del
      número de entrada
      

      """, anchor=W, borderwidth=2, relief=SOLID, height=25, justify=LEFT ).grid(row=4,column=3,sticky=SE)







###################################################      pestaña 3      #####################################################

Label(pes3, text="Bienvenido al programa para verificar si 2 números son amigos\nIngrese un número entero mayor a 0: \n").grid(row=0, column=0, sticky="NS")

Label(pes3, text="    Número 1:").grid(row=1, column=0, sticky=W)

valor3=IntVar()
txtValor=Entry(pes3, textvariable=valor3, width=8).grid(row=1, column=0, sticky=NS)
valor3.get()

boton=Button(pes3, text="MOSTRAR", command=conjeturaGoldbach).grid(row=1, column=0, sticky=E)



Label(pes3, text="    Número 2:").grid(row=2, column=0, sticky=W)

valor3b=IntVar()
txtValor=Entry(pes3, textvariable=valor3, width=8).grid(row=2, column=0, sticky=NS)
valor3b.get()

boton=Button(pes3, text="MOSTRAR", command=conjeturaGoldbach).grid(row=2, column=0, sticky=E)


###################################################      pestaña 4      #####################################################




root.mainloop()
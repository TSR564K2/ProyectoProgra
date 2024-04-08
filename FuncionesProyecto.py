#Funciones para conjetura de Goldbach
def esPrimo(n):
    resultado=False
    if n!=2:
        if n%2 !=0:
            divisor=3
            resultado=True
            while divisor <= n//2 and resultado!=False:
                if n % divisor ==0:
                    resultado=False
                divisor+=2
        else:
            resultado=False
    else:
        resultado=True
    return resultado

def sumaPrimosPar(num):
    resultado=False
    encontrado=False
    primo1=int(num/2)
    resultado=esPrimo(primo1)
    factores="Este número se puede escribir como:\n\n"
    if resultado:
        primo2=num-primo1
        factores+=str(primo1,"+",primo2)+ " \n"
        encontrado=True
    impar=3
    while impar <= num/2:
        if esPrimo(impar):
            primo1=int(num-impar)
            resultado= esPrimo(primo1)
            if resultado:
                primo2=num-primo1
                factores+=str(primo2)+ "+"+str(primo1)+ " \n"
                encontrado=True
        impar+=2
    if encontrado==True:
        factores+="\nLos cuales son todos números primos.\nPor lo tanto, el número "+str(num)+" cumple la conjetura de Goldbach\n"
        return factores
    else:
        return "El número ingresado no cumple la conjetura"


#Función para números amigos

def sumaDivisores(Numero):
    suma=0
    for divisor in range(1,Numero+1):
        if Numero%divisor==0:
            suma+=divisor
    suma-=Numero
    return suma

# Funcion Triangulo de Pascal





#Función Numero triangular
def triangulo(num):
    if 2 <= num and num <= 20: 
        numdepuntos = 0
        resultado = ""
        for x in range(1, num):
            numdepuntos += x
            if numdepuntos > num:
                break
            puntos = x
            resultado += "*" * puntos + "\n"
        return resultado
    else:
        novalido=""
        novalido="digite otro número"
        return novalido

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
                    respuesta = str("El número " + str(n) + " es un número triangular")
                    return respuesta
                sum += 1
        if resultado != True:
            respuesta = str("El número " + str(n) + " NO es un número triangular")
            return respuesta
    else:
        novalido=""
        novalido="Número no válido, el número debe estar entre 2 y 20"
        return novalido
    


cantidad=int(input("Ingrese la cantidad de temperaturas: "))
lista_temperatura=[]
for i in range (cantidad):
    temperatura=float(input(f"Ingrese la temperatura # {i+1}: "))
    lista_temperatura.append(temperatura)
suma=sum(lista_temperatura)
media=suma/cantidad
contador=0
for temperatura in lista_temperatura:
    if temperatura >= media:
        contador +=1
print(f"La media de las temperaturas es {media}")
print(f"las temperaturas que superan la media son {contador}")

lst=[1,20,15,10]

try:
    print(lst[10])
except IndexError:
    print("El indice no existe")
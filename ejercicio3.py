while True:
    try:
        num = float(input("Ingrese un numero: "))
        rst = "IMPAR"
        if num % 2 == 0:
            rst = "PAR"
        print("El numero {} es {}".format(num,rst))
        break
    
    except:
        print("OCURRIO UN ERROR!!")
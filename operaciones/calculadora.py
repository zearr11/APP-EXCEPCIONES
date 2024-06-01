def sumar(n1,n2):
    try:
        rpt= int(n1) + int(n2)
    except:
        print("INGRESE SOLO NUMEROS")
    else:
        return rpt

def restar(n1,n2):
    try:
        rpt= int(n1) - int(n2)
    except:
        print("INGRESE SOLO NUMEROS")
    else:
        return rpt

def multiplicar(n1,n2):
    try:
        rpt= int(n1) * int(n2)
    except:
        print("INGRESE SOLO NUMEROS")
    else:
        return rpt

def divi(n1,n2):
    try:
        rpt= int(n1) / int(n2)
    except ValueError:
        print("INGRESE SOLO NUMEROS")
    except ZeroDivisionError:
        print("NO SE PUEDE DIVIDIR ENTRE CERO")
    else:
        return rpt
        
        


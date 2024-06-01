while True:
    try:
        num = int(input("INGRESE UN AÑO: "))
        rst = "NO ES BISIESTO"
        if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
            rst= "ES BISIESTO"
    except:
        print("ERROR AL INGRESAR EL AÑO")
    else:
        print("EL AÑO {} ES {}".format(num, rst))
        break
    finally:
        print("FIN DE BUSQUEDA")
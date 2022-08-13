UNIDADES = ["CERO", "UNO", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE", "DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE"]
DECENAS = ["", "DIEZ", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
CENTENAS = ["", "CIEN", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]

n = int(input("Escriba un número entre 0 y 999: "))

if n < 0 or n > 999:
    print ("El número ingresado no es valido")
else:
    unid = n % 10
    dec = n % 100
    dece = (n // 10) % 10
    cen = n // 100

    if cen != 0:
        if cen == 1:
            if dec == 0:
                print ("CIEN", end="")
            else:
                print ("CIENTO", end="")
        else:
            print (CENTENAS[cen], end="")

        if dec != 0:
            print (" ", end="")

    if dec <= 15:
        if dec != 0 or cen == 0:
            print (UNIDADES[dec], end="")
    else:
        if dece == 1:
            print ("DIECI", end="")
        elif dece == 2:
            if unid == 0:
                print ("VEINTE", end="")
            else:
                print ("VEINTI", end="")
        else:
            print (DECENAS[dece], end="")

            if unid != 0:
                print (" Y ", end="")

        if unid != 0:
            print (UNIDADES[unid], end="")

print ("")

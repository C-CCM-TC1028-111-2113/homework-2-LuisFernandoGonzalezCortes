def main():
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    k=(peso) / (altura * altura)

    if (k < 20):
        print ("PESO BAJO")

    elif (20 <= k < 25):
        print ("NORMAL")

    elif (25 <= k < 30):
        print ("SOBREPESO")

    elif (30 <= k < 40):
        print ("OBESIDAD")

    elif (k >= 40):
        print ("OBESIDAD MORBIDA")
    

if __name__ == '__main__':
    main()

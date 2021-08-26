def main():
    # Escribe el código adecuado para completar el programa
    
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    if (x > y):
        
            if (x > z):

                if (z > y):

                    print ("", x, z, y)

                elif (y > z):
                    
                    print ("", x, y, z)
                

              
            
    elif (y > x):
       
            if (y > z):

                if (x > z):
                    
                    print ("",  y, x, z)

                elif (z > x):
                    
                    print ("",  y, x, z)
                

             

    elif (z > x):
        
            if (z > y):

                if (x > y):
                    
                    print ("",  z, x, y)

                elif (y > x):
                    
                    print ("",  z, y, x)

                

if __name__ == '__main__':
    main()

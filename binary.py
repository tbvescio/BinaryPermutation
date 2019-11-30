
entrada = int(input("Ingrese numero de variables: "))


def binary(x):
    s = bin(x)
    return s[2:]


def main():

	vector = []
	numero = 0
	for i in range(2**entrada): #se repite la cantidad de combinaciones
	    numero = str(binary(i)) 
	    numero = list(numero)
	    for x in range(entrada-len(numero)): #en los espacios que sobran pone 0
	        numero.insert(0, '0')
	    
	    print(list(numero))

main()





#hoja de trabajo 4
#ejercicio 1
frutas ={'Platano':135, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('que fruta quieres? ').title()
peso = float (input('cuantos kilos? '))

if fruta in frutas:
    print(peso, 'kilos de', fruta ,' total' , frutas[fruta]*peso)
else:
    print("la fruta no se encontro", fruta, " no esta disponible")



#ejercicio 2

numero = int(input('Que numero base quiere su tabla de multiplicar? '))
archivo = open("tabla.txt", "w")
for i in range(0, 11):
    resultado  = i * numero
    #print(("%d x %d = %d" )%(numero,i,resultado))
    archivo.write(("%d x %d = %d" )%(numero,i,resultado)) 
archivo.close()
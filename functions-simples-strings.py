nombreUsuario=input("Introduzca su nombre de usuario")

print("El nombre es: ",nombreUsuario.upper())

print("El nombre es: ",nombreUsuario.lower())

print("El nombre es: ",nombreUsuario.capitalize())

edad=input("Introduce la edad ")

print(edad.isdigit())

while(edad.isdigit()==False):

    print("Por favor, introduce un valor numérico")

    edad = input("Introduce la edad: ")

if(int(edad)<18):

    print("No puedes pasar")

else: 

    print("Puedes pasar")

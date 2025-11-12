#Datos del usuario
nombre = input ("Ingresa tu nombre")
año_nacimiento = int (input("Ingresa tu año de nacimiento"))

#Calculadora de año (Año actual = 2025)
año_actual = 2025
edad = año_actual-año_nacimiento

#Resultado por computadora
print (f"Hola {nombre} tienes {edad} años de edad")

if edad >= 18:
    print(f"{nombre} eres mayor de edad")
else:
    print(f"{nombre} eres menor de edad")

print(f"\nGracias {nombre} por usar nuestra calculadora")

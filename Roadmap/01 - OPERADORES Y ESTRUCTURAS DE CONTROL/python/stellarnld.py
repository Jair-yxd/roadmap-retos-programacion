# Tipos de operadores

# Operadores aritméticos 
num1 = 16
num2 = 200 
num3 = 105
num4 = 78 

num2 + num1 # suma 

num3 - num4 # resta 

num1 * num3 # multiplicación 

num4 / num1 # división

num2 % num4 # resto 

num3 // num4 # cociente 

num2 ** num3 # potenciación 

print((num2 - num4) * (num3 / num1) + num4 ** num1) 

# Operadores asignación 
x = 5 

x += 3  # equivale a x = x + 3 
8 

x -= 3 
2 

x *= 3
15 

x /= 2
2.5

x %= 2 
1

x //= 2
2 

x **= 3
125

print((x += 3) * (x %= 2))

# Operadores relacionales 
x = 5 

x == 3 
False 

x != 7 # ! significa distinto 
True 

x > 4
False

x < 9 
True 

x <= 1
False 

x >= 5 
True 

print(x !=  5)

# Operadores lógicos 
x = False 
y = True 

x and y # and devuelve True si ambos elementos son True 
False 

x or y # or devuelve True si al menos un elemento es True 
True 

not y # not devuelve True si el elemento es falso y viceversa 
False 

print(x and y) 

# Operadores especiales 
# Operador de identidad 
´´´comparan la identidad de dos objetos, 
comprueban si ambos objetos hacen referencia 
a la misma ubicación de memoria´´´

a = [1, 2, 3]
b = a 

print(a is b) #True 

print(a is not b) #False 

x = 5 
x = 10 

print(x is y) #False 

print(x is not y) #True 

# Operador de pertenencia 
´´´se utilizan para comprobar 
la pertenencia de un valor a una 
secuencia o conjunto, como,
cadenas, listas, conjuntos, etc´´´

Text = "Hello, world" 

print("Hello" in text) #True, "Hello" is present in the string

print("hi" in text) #False, "hi" is not present in the string

fruits = ["apple", "banana", "cherry"]

print("grape" not in fruits) #True, "grape" is not present in the list 

print("banana" not in fruits) #False, "banana" is present in the list









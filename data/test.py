
<<<<<<< HEAD
=======

# y = (x - 5) * 2
# esto quiere decir que para cada valor que tengamos x y es el resultado de 
# restarle 5 a x y multiplicarlo por 2

# por ejemplo, si x = 4
# y = (x - 5) * 2
#      ^ x = 4

# y = (4 - 5) * 2
#       ^ (4 - 5) = -1

# y = -1 * 2
# y = -2

# una funcion es una expresion donde la x es como la i de un for, puede tomar distinos
# valores y segun esos distintos valores la y da un resultado distinto:
print(f'\n ejemplo con un valor de x:')
x = [4]

for i in x:
    y = (i - 5) * 2
    print(f'para x = {i}, y = {y}')

# si tenemos varios valores de x pues tendremos varios valores de y
print(f'\n ejemplo con varios valores de x:')
x = [4,5,6]

for i in x:
    y = (i - 5) * 2
    print(f'para x = {i}, y = {y}')
>>>>>>> main

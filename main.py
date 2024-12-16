import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Introduce la longitud de la contraseña: "))
contraseña = ""
for _ in range(longitud):
    contraseña += random.choice(characters)

print("La contraseña generada es:", contraseña)

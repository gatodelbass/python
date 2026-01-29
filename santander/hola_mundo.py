print("hola mundo")

# conjuntos deben tener elementos unicos?
frutas = {"manzana", "platano", "fresa", "manzana", "coco"}
frutos = {"papaya", "mango", "coco", "platano", "fresa"}
fruits = {"coco"}
print(frutas)
# si el elemento ya existe, no lo agrega al conjunto
#union
frutas_unidas = frutas | frutos
print(frutas_unidas)

#interseccion
frutas_comunes = frutas & frutos & fruits
print(frutas_comunes)



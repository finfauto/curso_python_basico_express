# List

grades = [7.1, 4.3, 8.5, 5.0]
print(grades)
grades.append(3.5)
print(grades)
grades.clear()
print(grades)
print(len(grades))
#print(grades[0])  # IndexError!!
grades = [7.1, 4.3, 8.5, 5.0]
print(grades[0])
print(grades[1:])


# Strings

print("hola")
print("hola" + "Luís")
saludo = "hola" + "luis"
print(saludo)
lista_nombres = "Carlos,Luisa,Pedro,Carmen".split(',')
print(lista_nombres)
print(",".join(lista_nombres))
lista_nombres.sort()
print(lista_nombres)


# Dicts

test_dict = {}
print(test_dict)
test_dict["mi nueva clave"] = 1
print(test_dict)
print(test_dict["mi_nueva_clave"])
print(test_dict["otra_clave"])  # KeyError!!


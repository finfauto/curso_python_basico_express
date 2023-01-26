a = 0
print(id(a))
print(a)
a += 1
print(id(a))
print(a)


l = [1, 2, 3]
print(l)
print(id(l))
for element in l:
    print(f"Value is {element} and it id is{id(element)}")

index = 0
while index < len(l):
    l[index] = l[index] * 2
    index += 1

print(l)
print(id(l))
for element in l:
    print(f"Value is {element} and it id is{id(element)}")

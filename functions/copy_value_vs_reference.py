def whatever(anything):
    print(f"The anything inside the function is {anything} with id {id(anything)}")
    anything += 1
    print(f"The anything after adding 1 is {anything} with id {id(anything)}")

anything = 0
print(f"The anything outside the function is {anything} with id {id(anything)}")
whatever(anything)
print(f"Let's check if the anything variable was modified inside the función -> {anything} with id {id(anything)}")

def whatever_list(anything):
    print(f"The anything inside the function is {anything} with id {id(anything)}")
    anything.append(3)
    print(f"The anything after appending 3 is {anything} with id {id(anything)}")

anything = [1, 2]
print(f"The anything outside the function is {anything} with id {id(anything)}")
whatever_list(anything)
print(f"Let's check if the anything variable was modified inside the función -> {anything} with id {id(anything)}")


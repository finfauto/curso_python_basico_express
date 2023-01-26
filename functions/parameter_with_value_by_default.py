def any_function(parameter1, parameter2, parameter3=10, parameter4=11):
    print(f"parameter1 -> {parameter1}")
    print(f"parameter2 -> {parameter2}")
    print(f"parameter3 -> {parameter3}")
    print(f"parameter4 -> {parameter4}")


any_function(1, 2)
any_function(4, 3, 2, 1)


any_function(1)
any_function(parameter1=1, parameter4=2)

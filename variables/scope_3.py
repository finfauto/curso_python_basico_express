def scope_test1(variable1):
    print(variable1)


def scope_test2(variable2):
    print(variable2)
    print(variable1)


if __name__ == "__main__":
    scope_test1("Juan")
    scope_test2("Luisa")


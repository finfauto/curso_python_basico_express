def scope_test(variable1):
    print(variable1)  # variable1 is accesible from here
    for i in range(10):
        print(i)  # variable i is accesible from here

    print(i)  # is i accesible from here?


if __name__ == "__main__":
    scope_test("hello")

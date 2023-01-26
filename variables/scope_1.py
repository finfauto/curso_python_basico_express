def scope_test_meh(variable1):
    if len(variable1) > 0:
        name = "Sandra"
    else:
        name = None

    print(f"{variable1} {name}")  # We should not be using name because it is not declared in out scope


def scope_test_should_fail(variable1):
    if len(variable1) > 0:
        name = "Sandra"

    print(f"{variable1} {name}")  # We haven't declared name but it is working!??!


def scope_test_formally_ok(variable1):
    name = None
    if len(variable1) > 0:
        name = "Sandra"

    print(f"{variable1} {name}")  # All variables are visible in out scope


if __name__ == "__main__":
    scope_test_meh("hello")
    scope_test_should_fail("hello")
    scope_test_formally_ok("hello")

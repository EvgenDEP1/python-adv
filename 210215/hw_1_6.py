from decorators import debug, do_twice, repeat


@debug
@do_twice
def greet(name):
    print(f"Привет {name}")


@repeat(num_times=4)
def greett(name):
    print(f"Hello {name}")


greet("Evgen")
greett("World")

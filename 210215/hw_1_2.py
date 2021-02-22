from decorators import do_twice, timer



@do_twice
def say_whee():
    print("Текст")


@do_twice
def greet(name):
    print(f"Привет {name}")


@do_twice
def return_greeting(name):
    print("Приветствия")
    return f"Hi {name}"


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


say_whee()
greet("мир")

hi_evgen = return_greeting("Евген")
print(hi_evgen)

print(say_whee)
print(say_whee.__name__)
help(say_whee)

waste_some_time(1)

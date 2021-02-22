# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
#
# say_whee = my_decorator(say_whee)
# say_whee()

from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 18:
            func()
        else:
            pass

    return wrapper


@not_during_the_night
def say_whee():
    print("ТУК ТУК")


say_whee = not_during_the_night(say_whee)
say_whee()

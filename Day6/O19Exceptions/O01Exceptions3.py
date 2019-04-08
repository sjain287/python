import sys


class MyError(Exception):
    pass


class YourError(Exception):
    pass


class OurError(Exception):
    pass


val = 10
try:
    if val < 5:
        raise MyError("Value too small")
    if val > 15:
        raise YourError("Value should be Limited")
    if val == 10:
        raise OurError("This value is not permitted")
except MyError as me:
    print(me)
except YourError as ye:
    print(ye)
except OurError as oe:
    print(oe)

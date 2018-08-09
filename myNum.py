#!/usr/bin/env python3


class MyNum():
    def __init__(self,value):
        print("Calling __init__")
        self.value = value

    def increment(self):
        self.value = self.value + 1

dd = MyNum(5)
dd.increment()
dd.increment()
print(dd.value)
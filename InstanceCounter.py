#!/usr/bin/env python3


class InstanceCounter():
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self,newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)
d = InstanceCounter(20)

for obj in (a,b,c,d):
    print("Val of obj: {}".format(obj.get_val()))
    print("Count 'from instance' {}".format(obj.count))
#!/usr/bin/env python3

class Test:
    class t2:
        def __init__(self):
            print("t2")
    def __init__(self):
        print("test")
    def show(self):
        tt = Test.t2()

if __name__ == "__main__":
    t1 = Test()
    t1.show()
    # t2 = PBTypeString("abc")
    # print(t2.type)
    # t3 = PBTypeHash("ab")
    # print(t3.type)
    # print(PBTypeString.Type)
    # pdb.set_trace()


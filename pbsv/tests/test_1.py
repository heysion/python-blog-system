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

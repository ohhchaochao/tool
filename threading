import threading
import time


class MyThreading(threading.Thread):
    def __init__(self, name):
        super(MyThreading, self).__init__()
        self.name = name

    def run(self):
        print("%s" % self.name)
        # function()


if __name__ == "__main__":
    a = MyThreading(1)
    b = MyThreading(2)
    end_time = time.time()
    a.start()
    b.start()


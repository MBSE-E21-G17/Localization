import datetime
import random
import time


def timeNow():
    now = datetime.datetime.now()
    tid = now.strftime("%H:%M:%S:%f %p")
    return tid


class Customer:
    customers = [1, 2, 3]

    def __init__(self, PATH):
        self.PATH = PATH
        self.timeTaken = 1

    def move(self, customer):
        for g in self.PATH:
            print(" ")
            for p in g:
                # print(g[2])
                if (p[2] == self.timeTaken):
                    print("At time {} seconds, customer is at ({},{})".format(
                        p[2], p[0], p[1]))
                self.timeTaken += 1

            # time.sleep(random.randrange(1, 10))

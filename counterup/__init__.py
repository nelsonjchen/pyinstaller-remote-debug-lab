from time import sleep


class CounterPrint(object):
    def __init__(self):
        count = 0
        while True:
            count = count + 1
            print("Count: " + str(count))
            sleep(1)

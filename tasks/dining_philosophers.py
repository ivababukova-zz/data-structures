import threading
import random
import time

class Chopstick:
    def __init__(self, index):
        self.lock = threading.Lock()
        self.index = index

    def pick_up(self):
        self.lock.acquire()
        print("{} is picked up.".format(self.index))

    def put_down(self):
        self.lock.release()
        print("{} is put down.".format(self.index))

class Philosopher(threading.Thread):

    running = True

    def __init__(self, index, left, right):
        threading.Thread.__init__(self)
        self.index = index
        self.left = left
        self.right = right

    def run(self):
        while(self.running):
            #  Philosopher is thinking (but really is sleeping).
            time.sleep(random.uniform(3,13))
            print('{} is hungry.'.format(self.index))
            self.eat()

    def eat(self):
        self.left.pick_up()
        self.right.pick_up()
        print("Philosopher {} is eating".format(self.index))
        self.left.put_down()
        self.right.put_down()
        print("**** that's it ****")

def main():
    numb_philosophers = 5
    chopsticks = [Chopstick(i) for i in range(numb_philosophers)]
    philosophers = [Philosopher(i, chopsticks[i], chopsticks[(i-1)%numb_philosophers]) for i in range(numb_philosophers)]
    Philosopher.running = True
    for p in philosophers:
        p.start()
    Philosopher.running = False

if __name__ == '__main__':
    main()
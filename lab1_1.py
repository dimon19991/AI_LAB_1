from math import exp
from random import uniform

y = 0.3

class Neuron:

    def __init__(self, x, counr):
        self.x = x
        w = []
        for i in range(counr):
            w.append(uniform(-1, 1))

        self.w = w


    def sumo(self):
        sums = 0
        for i in range(len(self.x)):
            sums += int(self.x[i]) * self.w[i]
        return sums

    def activation(self):
        self.y = 1 / (1 + exp(-1 * self.sumo()))

    def mistake(self):
        self.delta = abs((self.y - y)/y)


    def correction(self):
        sigma = self.y * (1 - self.y) * (y - self.y)
        delta_w = []
        for i in range(len(self.x)):
            delta_w.append(self.x[i] * sigma)
            self.w[i] = self.w[i] + delta_w[i]

    def training(self):
        q = 0
        while(True):
            self.activation()
            self.mistake()
            print(str(q) + "\t Delta -  " + str(self.delta) + "\t Y - " + str(self.y))
            q+=1
            if self.delta < delte:
                break
            else:
                self.correction()



delte = 0.1
x = "1 7 4 5 0.3"

x = x.split(" ")
y_o = float(x.pop(-1))
x = list(map(lambda z: float(z), x))
w = []
delta_w = []
k = 1

neuron_1 = Neuron(x, 4)
neuron_1.training()


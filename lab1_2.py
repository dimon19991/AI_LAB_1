from math import exp
from random import uniform

delte = 0.1
y = 0.5
x = 3


class Neuron_I:
    def activation(self):
        self.y = self.y * 1

    def training(self, x):
        self.y = x[0]
        self.activation()
        return self.y


class Neuron_M:
    def __init__(self, counr):
        w = []
        for i in range(counr):
            w.append(uniform(-1, 1))
        self.w = w

    def sumo(self):
        sums = 0
        for i in range(len(self.x)):
            sums += float(self.x[i]) * self.w[i]
        self.y = sums

    def activation(self):
        self.y = 1 / (1 + exp(-1 * self.y))

    def correction(self):
        sigma = self.y * (1 - self.y) * (y - self.y)
        delta_w = []
        for i in range(len(self.x)):
            delta_w.append(self.x[i] * sigma)
            self.w[i] = self.w[i] + delta_w[i]

    def training(self, x):
        self.x = x
        self.sumo()
        self.activation()
        return self.y


class Neuron_U:
    def __init__(self, counr):
        w = []
        for i in range(counr):
            w.append(uniform(-1, 1))
            # w.append(0.5)
        self.w = w

    def sumo(self):
        sums = 0
        for i in range(len(self.x)):
            sums += float(self.x[i]) * self.w[i]
        self.y = sums

    def activation(self):
        self.y = 1 / (1 + exp(-1 * self.y))

    def mistake(self):
        self.delta = abs((self.y - y) / y)
        return self.delta

    def correction(self):
        sigma = self.y * (1 - self.y) * (y - self.y)
        delta_w = []
        for i in range(len(self.x)):
            delta_w.append(self.x[i] * sigma)
            self.w[i] = self.w[i] + delta_w[i]

    def training(self, x):
        self.x = x
        self.sumo()
        self.activation()
        self.mistake()
        print("Delta - " + str(self.delta) + "\t Y - " + str(self.y))
        return self.y


neuron_1_1 = Neuron_I()
neuron_2_1 = Neuron_M(1)
neuron_3_1 = Neuron_U(1)
z = 0
while (True):

    print("Итерация " + str(z))
    z += 1
    new_y = neuron_1_1.training([x])
    new_y = neuron_2_1.training([new_y])
    new_y = neuron_3_1.training([new_y])
    if neuron_3_1.mistake() < delte:
        break
    else:
        neuron_3_1.correction()
        neuron_2_1.correction()

print("\n\nТестування")
x = 3.1
new_y = neuron_1_1.training([x])
new_y = neuron_2_1.training([new_y])
new_y = neuron_3_1.training([new_y])


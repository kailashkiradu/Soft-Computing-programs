import random

LEARNING_RATE = 0.1
MAX_ITERATIONS = 1000

class Perceptron:
    def __init__(self, num_inputs):
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1, 1)

    def activate(self, net):
        return 1 if net >= 0 else -1

    def train(self, data):
        converged = False
        iteration = 0
        while not converged and iteration < MAX_ITERATIONS:
            converged = True
            for x, label in data:
                net = sum(x[i] * self.weights[i] for i in range(len(x))) + self.bias
                output = self.activate(net)
                error = label - output
                if error != 0:
                    for i in range(len(self.weights)):
                        self.weights[i] += LEARNING_RATE * error * x[i]
                    self.bias += LEARNING_RATE * error
                    converged = False
            iteration += 1

        if converged:
            print("Perceptron converged after", iteration, "iterations")
        else:
            print("Perceptron did not converge after", MAX_ITERATIONS, "iterations")

def main():
    # Example data points
    data = [
        ([2.0, 3.0], 1),
        ([4.0, 5.0], 1),
        ([-1.0, 1.0], -1),
        ([-3.0, -4.0], -1)
    ]
    # Initialize Perceptron
    perceptron = Perceptron(num_inputs=2)
    # Train Perceptron
    perceptron.train(data)
    # Print trained weights
    print("Trained Weights:", perceptron.weights)
    print("Bias:", perceptron.bias)

if __name__ == "__main__":
    main()

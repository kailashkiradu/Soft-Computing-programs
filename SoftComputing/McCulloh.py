class McCullochPittsNeuron:
    def __init__(self, num_inputs, weights, threshold):
        self.num_inputs = num_inputs
        self.weights = weights
        self.threshold = threshold

    def activate(self, inputs):
        if len(inputs) != self.num_inputs:
            raise ValueError("Number of inputs must match the number of weights")
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))
        output = 1 if weighted_sum >= self.threshold else 0
        return output

if __name__ == "__main__":
    # Define inputs, weights, and threshold
    inputs = [0, 1, 1]
    weights = [0.5, -1, 1]
    threshold = 0.5
    neuron = McCullochPittsNeuron(num_inputs=len(inputs), weights=weights, threshold=threshold)
    output = neuron.activate(inputs)
    print("Output:", output)

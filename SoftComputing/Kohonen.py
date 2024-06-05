import numpy as np

class SOM:
    def __init__(self, input_size, map_size):
        self.input_size = input_size
        self.map_size = map_size
        self.weights = np.random.rand(map_size[0], map_size[1], input_size)

    def train(self, data, epochs, learning_rate=0.1, sigma=1.0):
        for epoch in range(epochs):
            for i, x in enumerate(data):
                # Find the Best Matching Unit (BMU)
                bmu_idx = self._find_bmu(x)
                # Update weights of BMU and its neighbors
                self._update_weights(x, bmu_idx, epoch, learning_rate, sigma)
            # Print SOM weights after each epoch
            print("SOM weights after training:")
            print(self.weights)

    def _find_bmu(self, x):
        # Compute distances between input vector and all neurons
        distances = np.linalg.norm(self.weights - x, axis=-1)
        # Find the index of the neuron with the smallest distance
        bmu_idx = np.unravel_index(np.argmin(distances), distances.shape)
        return bmu_idx

    def _update_weights(self, x, bmu_idx, epoch, learning_rate, sigma):
        # Update weights of BMU and its neighbors based on the learning rate and neighborhood function
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                # Calculate the influence of the neuron on the BMU
                influence = self._neighborhood_function(bmu_idx, (i, j), epoch, sigma)
                # Update weights
                self.weights[i, j] += influence * learning_rate * (x - self.weights[i, j])

    def _neighborhood_function(self, bmu_idx, neuron_idx, epoch, sigma):
        # Gaussian neighborhood function
        distance = np.linalg.norm(np.subtract(bmu_idx, neuron_idx))
        return np.exp(-distance**2 / (2 * (sigma**2)))

# Example usage
if __name__ == "__main__":
    # Example dataset (random)
    data = np.random.rand(100, 2)  # 100 samples, 2 features

    # Define SOM parameters
    input_size = data.shape[1]
    map_size = (10, 10)
    epochs = 100
    learning_rate = 0.1
    sigma = 1.0

    # Initialize and train SOM
    som = SOM(input_size, map_size)
    som.train(data, epochs, learning_rate, sigma)

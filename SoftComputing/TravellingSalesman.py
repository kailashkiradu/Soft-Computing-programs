import numpy as np
import random
import matplotlib.pyplot as plt

# Number of cities
num_cities = 20

# Generate random cities
random.seed(42)
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)]

# Calculate distance between two cities
def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Calculate total distance of a route
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance(route[i], route[i+1])
    total += distance(route[-1], route[0])  # Return to the starting city
    return total

# Initialize population
def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        population.append(random.sample(cities, len(cities)))  # Fixed indentation
    return population

# Evaluate population
def evaluate_population(population):
    fitness_values = []
    for individual in population:
        fitness_values.append(1 / total_distance(individual))  # Inverse of distance as fitness
    return fitness_values

# Selection (Roulette wheel selection)
def selection(population, fitness_values):
    selected_parents = []
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    for _ in range(len(population)):
        selected_parents.append(random.choices(population, probabilities)[0])
    return selected_parents

# Crossover (Order crossover)
def crossover(parents):
    offspring = []
    for i in range(0, len(parents), 2):
        parent1, parent2 = parents[i], parents[i+1]
        crossover_point1 = random.randint(0, len(parent1) - 1)
        crossover_point2 = random.randint(crossover_point1 + 1, len(parent1))
        offspring1 = parent1[crossover_point1:crossover_point2]
        offspring2 = [city for city in parent2 if city not in offspring1]
        offspring.append(offspring1 + offspring2)
        offspring.append(offspring2 + offspring1)
    return offspring

# Mutation (Swap mutation)
def mutation(offspring, mutation_rate=0.01):
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            swap_indices = random.sample(range(len(offspring[i])), 2)
            offspring[i][swap_indices[0]], offspring[i][swap_indices[1]] = \
                offspring[i][swap_indices[1]], offspring[i][swap_indices[0]]
    return offspring

# Replacement (Elitism: Keep the best individuals)
def replace_population(combined_population, population_size):
    combined_population.sort(key=lambda x: total_distance(x))
    return combined_population[:population_size]

# Genetic algorithm
def genetic_algorithm(population_size, generations):
    population = initialize_population(population_size)
    best_distances = []
    for gen in range(generations):
        fitness_values = evaluate_population(population)
        best_distances.append(1 / max(fitness_values))  # Store the best distance of each generation
        selected_parents = selection(population, fitness_values)
        offspring = crossover(selected_parents)
        mutated_offspring = mutation(offspring)
        population = replace_population(mutated_offspring, population_size)
    best_solution = min(population, key=total_distance)
    return best_solution, best_distances

# Main function
if __name__ == "__main__":
    population_size = 100
    generations = 100
    best_solution, best_distances = genetic_algorithm(population_size, generations)
    print("Best Route:", best_solution)
    print("Best Distance:", total_distance(best_solution))

    # Plotting the convergence curve
    plt.plot(best_distances)
    plt.xlabel('Generation')
    plt.ylabel('Best Distance')
    plt.title('Convergence Curve')
    plt.show()

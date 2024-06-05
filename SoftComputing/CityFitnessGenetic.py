import numpy as np
import random

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        distance = np.sqrt((x_distance ** 2) + (y_distance ** 2))
        return distance

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def route_distance(self):
        if self.distance == 0:
            path_distance = 0
            for i in range(len(self.route)):
                from_city = self.route[i]
                if i + 1 < len(self.route):
                    to_city = self.route[i + 1]
                else:
                    to_city = self.route[0]
                path_distance += from_city.distance_to(to_city)
            self.distance = path_distance
        return self.distance

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness

    @staticmethod
    def create_route(city_list):
        route = random.sample(city_list, len(city_list))
        return route

    @staticmethod
    def initial_population(pop_size, city_list):
        population = []
        for _ in range(pop_size):
            population.append(Fitness.create_route(city_list))
        return population

    @staticmethod
    def rank_routes(population):
        fitness_results = {}
        for i in range(len(population)):
            fitness_results[i] = Fitness(population[i]).route_fitness()
        return sorted(fitness_results.items(), key=lambda x: x[1], reverse=True)

    @staticmethod
    def selection(population_ranked, elite_size):
        selection_results = []
        for i in range(elite_size):
            selection_results.append(population_ranked[i][0])
        for _ in range(len(population_ranked) - elite_size):
            pick = 100 * random.random()
            for i in range(len(population_ranked)):
                if pick <= population_ranked[i][1]:
                    selection_results.append(population_ranked[i][0])
                    break
        return selection_results

    @staticmethod
    def mating_pool(population, selection_results):
        matingpool = []
        for i in range(len(selection_results)):
            index = selection_results[i]
            matingpool.append(population[index])
        return matingpool

    @staticmethod
    def breed(parent1, parent2):
        child = []
        child_parent1 = []
        child_parent2 = []
        gene1 = int(random.random() * len(parent1))
        gene2 = int(random.random() * len(parent1))
        start_gene = min(gene1, gene2)
        end_gene = max(gene1, gene2)
        for i in range(start_gene, end_gene):
            child_parent1.append(parent1[i])
        child_parent2 = [item for item in parent2 if item not in child_parent1]
        child = child_parent1 + child_parent2
        return child

# Define a list of cities
city_list = [City(0, 0), City(3, 0), City(6, 0), City(0, 4), City(3, 4)]

# Set genetic algorithm parameters
population_size = 20
elite_size = 5
generations = 10

# Initialize the population
population = Fitness.initial_population(population_size, city_list)

# Evolve the population over generations
for gen in range(generations):
    ranked_routes = Fitness.rank_routes(population)
    selected_routes = Fitness.selection(ranked_routes, elite_size)
    mating_pool = Fitness.mating_pool(population, selected_routes)
    children = []
    while len(children) < population_size:
        parent1 = random.choice(mating_pool)
        parent2 = random.choice(mating_pool)
        child = Fitness.breed(parent1, parent2)
        children.append(child)
    population = children

# Print the best route and its fitness
best_route_index = Fitness.rank_routes(population)[0][0]
best_route = population[best_route_index]
best_distance = Fitness(best_route).route_distance()
print("Best Route:", best_route)
print("Best Distance:", best_distance)

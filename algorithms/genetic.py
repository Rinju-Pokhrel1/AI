import random

def fitness(individual, target):
    return sum(abs(individual[i] - target[i]) for i in range(len(target)))

def create_individual(length):
    return [random.randint(0, 1) for _ in range(length)]

def mutate(individual, rate=0.01):
    return [1-g if random.random() < rate else g for g in individual]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    return parent1[:point]+parent2[point:], parent2[:point]+parent1[point:]

def genetic_algorithm(target, population_size=10, generations=100, mutation_rate=0.01):
    population = [create_individual(len(target)) for _ in range(population_size)]
    for gen in range(generations):
        population = sorted(population, key=lambda ind: fitness(ind, target))
        if fitness(population[0], target) == 0:
            return population[0], gen
        next_gen = population[:2]
        while len(next_gen) < population_size:
            p1, p2 = random.sample(population[:5], 2)
            c1, c2 = crossover(p1, p2)
            next_gen.append(mutate(c1, mutation_rate))
            if len(next_gen) < population_size:
                next_gen.append(mutate(c2, mutation_rate))
        population = next_gen
    return population[0], generations

target = [1,0,1,1,0,1,0,1]
solution, gen = genetic_algorithm(target)
print("Best solution:", solution, "found in generation:", gen)

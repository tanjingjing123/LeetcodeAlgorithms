import numpy as np

N_ITEMS = 20  # 物品数量
CROSS_RATE = 0.5  # DNA交叉概率
MUTATE_RATE = 0.01  # 变异概率
POP_SIZE = 400  # 个体数量
N_GENERATIONS = 20  # 迭代轮数

class GA:
    def __init__(self, DNA_size, cross_rate, mutate_rate, pop_size, n_generations):
        self.DNA_size = DNA_size
        self.cross_rate = cross_rate
        self.mutate_rate = mutate_rate
        self.pop_size = pop_size
        self.n_generations = n_generations
        #  初始化每个个体的DNA
        self.pop = np.random.randint(0, 2, size=(pop_size, DNA_size))

    def get_fitness(self, w, v, c):
        fitness = np.empty(shape=self.pop_size, dtype=np.float32)    #shape --- Number of rows
        for i, individual in enumerate(self.pop):  # 计算每个个体的fitness和weight
            weight = w[individual.astype(np.bool)].sum()
            value = v[individual.astype(np.bool)].sum()
            # 若物品总重量超过capacity，则fitness为0
            fitness[i] = 0 if weight > c else value
        return np.exp(fitness/self.DNA_size)

    def select(self, fitness):  # 适应度高的DNA有更大的概率保留
        index = np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True, p=fitness/fitness.sum())
        return self.pop[index]

    def mutate(self, dna):
        for point in range(self.DNA_size):
            if np.random.rand() < self.mutate_rate:
                dna[point] = 0 if dna[point] == 0 else 1  # 变异

    def crossover(self, pop):
        pop_copy = pop.copy()
        for i in range(self.pop_size):
            if np.random.rand() < self.cross_rate:
                i_ = np.random.randint(self.pop_size, size=1)  # 选择另一个体
                cross_points = np.random.randint(2, size=self.DNA_size).astype(np.bool)  # 确定DNA交叉点
                pop[i, cross_points] = pop_copy[i_][0][cross_points]
            self.mutate(pop[i])


c = 40  # 背包容量
w = np.array([4, 5, 6, 2, 2, 3, 7, 8, 6, 9, 1, 5, 6, 8, 3, 4, 4, 9, 4, 2])  # 物品重量
v = np.array([6, 4, 5, 3, 6, 2, 4, 4, 9, 5, 3, 7, 8, 3, 6, 8, 4, 2, 3, 9])  # 物品价值

ga = GA(N_ITEMS, CROSS_RATE, MUTATE_RATE, POP_SIZE, N_GENERATIONS)

for generation in range(N_GENERATIONS):
    fitness = ga.get_fitness(w, v, c)
    #print(generation)
    #print(fitness)
    pop = ga.select(fitness)
    #print(pop)
    ga.crossover(pop)
    best_idx = np.argmax(fitness)     #numpy.argmax(array, axis = None, out = None) : Returns indices of the max element of the array in a particular axis.
    print(best_idx)
    print('Gen:', generation, '| best fit: %.2f' % (np.log(fitness[best_idx])*ga.DNA_size), '| items:', ga.pop[best_idx])
    ga.pop = pop
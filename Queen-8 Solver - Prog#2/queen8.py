import random

#constants variables 
num_q = 8
max_fitness_score = 28
mutation_probability = 0.10

#Population generation function 
def generate_population(population, fitness):
    
    new_population = []
    prob = [prop(n, fitness) for n in population]
    for i in range(len(population)):
        x = rand_selection(population, prob)
        y = rand_selection(population, prob)
        
        child = crossover(x, y)
        
        if random.random() < mutation_probability:
            child = mutate(child)
        
        print(f"{str(child)},  fitness outcome = {fitness(child)}")

        new_population.append(child)
        if fitness(child) == max_fitness_score: 
            break
    return new_population

#Fitness Function
def fitness(seq):
    score = 0  
    for r in range(num_q):
        c = seq[r]        
        for other_row in range(num_q):
            if other_row == r: # check if the two queens at the same raw
                continue
            if seq[other_row] == c: # check if thetwo queens at the same column
                continue
            if other_row + seq[other_row] == r + c: # check if the two queens meet digonly  
                continue
            if other_row - seq[other_row] == r - c: # check if the two queens meet digonly
                continue
            score += 1 
    return score/2

#crossover function 
def crossover(x, y):
    c = random.randint(0, len(x)-1)
    r =  x[0:c] + y[c:len(x)]
    return r

#mutation function
def mutate(seq):
    for row in range(len(seq)):
        if random.random() < mutation_probability:
            seq[row] = random.randrange(num_q)
    return seq


# getting probability function
def prop(seq, fitness):
    prop =  fitness(seq) / max_fitness_score
    return prop


def rand_selection(population, probs):
    pop_probability = zip(population, probs)

    total = sum(s for k, s in pop_probability)
    r = random.uniform(0, total)
    n = 0
    
    for k, s in zip(population, probs):
        if n + s >= r:
            return k
        n += s
        

def rand_i(size):
    x = [ random.randint(0, size - 1) for i in range(size) ]
    return x

#Printing the queen-8 board
def print_8Q(chrom):
    board = []

    for x in range(num_q):
        board.append(["x"] * num_q)

    for i in range(num_q):
        board[chrom[i]][i] = "Q"

    def print_8Q2(board):
        for r in board:
            print(" ".join(r))

    print()
    print_8Q2(board)

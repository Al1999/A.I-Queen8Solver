from statistics import mean
from queen8 import rand_i, fitness, generate_population, print_8Q  
import pandas as pd

import openpyxl 

num_q = 8 #Constant number of queens variable
generation = 1

#main function
if __name__ == "__main__":

    pop_size = 0
    print("\n            -  W E L C O M E  T O  8 Q U E E N  S O L V E R  -")
    print("\n- Choose the size of the population by typing one of the numbers listed below: \n> 10\n> 100\n> 500\n> 1000")
    pop_size = input()
    pop_size = int(pop_size)
    
    Average_fitness = 0
    Max_fitness  = 0
    data = {'Average fitness':[], 'Number of generation':[]}
    df = pd.DataFrame(data, columns=['Average fitness','Number of generation'])

    if pop_size == 10 or pop_size == 100 or pop_size == 500 or pop_size == 1000:
        #generting new first population
        population = [rand_i(num_q) for i in range(pop_size)]
        i = population[0]
        while not 28 in [fitness(x) for x in population]:
            print(f"\n            >>> Generation {generation} <<<")
            
            #regenerting new population
            population = generate_population(population, fitness)
            
            #getting the Average fitness and save it into a dataframe to create a table graph  
            Average_fitness = mean([fitness(x) for x in population])
            Max_fitness = max([fitness(x) for x in population])
            new_row = {'Average fitness':   Average_fitness , 'Number of generation' : generation}
            df = df.append(new_row ,ignore_index= True)

            print(f"> Maximum fitness = {Max_fitness}")
            print(f"> Average fitness = {Average_fitness}")
            generation += 1

        print(f"\n> Solved in Generation {(generation-1)}!")

        for x in population:
            if fitness(x) == 28:
                print(f"{str(x)},  fitness outcome = {fitness(x)}\n")
                print('> The Solution of Queen-8 Board <')
                print_8Q(x)
                print("\n")
        #print('> The initial population of Queen-8`s Board <')
        #print_8Q(i)
        #writer = pd.ExcelWriter('/Users/alkhtabalrashdy/Downloads/data_q8.xlsx')
        #df.to_excel(writer)
        #writer.save()
    
    else:
        print("\n!-> Error: You have to choose one of the numbers above! Sorry try again next time <-!\n")


# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what, and that is exactly what you are called
# to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line, you will be given the minimum wealth. 
# You should distribute the wealth so that no part of the population has less than the minimum wealth. To do that, you should always take wealth from the wealthiest
# part of the population. 
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible". 


population = list(map(int,input().split(', ')))
minimum_wealth = int(input())

income = sum([abs(x - minimum_wealth) for x in population if x < minimum_wealth])
wealth = sum([abs(x - minimum_wealth) for x in population if x > minimum_wealth])

if income > wealth:
    print(f"No equal distribution possible")
else:
    while min(population) < minimum_wealth:
        transfer = minimum_wealth - min(population)
        population[population.index(min(population))] += transfer
        population[population.index(max(population))] -= transfer

    print(population)

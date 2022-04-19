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
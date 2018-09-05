numberGames = {}

numberGames[(1,2,4)] = 8

numberGames[(4,2,1)] = 10

numberGames[(1,2)] = 12

sum = 0

for k in numberGames:

    sum += numberGames[k]


print(len(numberGames) + sum)

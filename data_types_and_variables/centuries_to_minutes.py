centuries = int(input())
years = 0
days = 0
hour = 0
minutes = 0

years = centuries * 100
days = int(years * 365.2422)
hour = days * 24
minutes = hour * 60

print(f"{centuries} centuries = {years} years = {days} days = {hour} hours = {minutes} minutes", end='')

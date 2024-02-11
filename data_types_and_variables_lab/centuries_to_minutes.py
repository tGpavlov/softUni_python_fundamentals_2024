num_of_centuries = int(input())

centuries = num_of_centuries * 100
years = int(centuries * 365.2422)
days = years * 24
hours = days * 60

print(f'{num_of_centuries} centuries = {centuries} years = {years}'
      f' days = {days} hours = {hours} minutes')

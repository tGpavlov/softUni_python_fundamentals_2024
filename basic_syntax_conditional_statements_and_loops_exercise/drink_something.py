ppl_age = int(input())
drink = ''

if ppl_age <= 14:
    drink = 'toddy'
elif ppl_age <= 18:
    drink = 'coke'
elif ppl_age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f'drink {drink}')

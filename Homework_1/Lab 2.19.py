# Anthony Flores 1792816 CIS2348 2.19

lemon_juice = int(input('Enter amount of lemon juice (in cups):\n'))
Water = int(input('Enter amount of water (in cups):\n'))
Agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
Servings = int(input('How many servings does this make?''\n'))
print()
print('Lemonade ingredients - yields', '{:.2f}'.format(Servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(Water), 'cup(s) water')
print('{:.2f}'.format(Agave_nectar), 'cup(s) agave nectar')
print()  # end of question (1)

sec_servings = int(input('How many servings would you like to make?''\n'))
print()

print('Lemonade ingredients - yields', '{:.2f}'.format(sec_servings), 'servings')
print('{:.2f}'.format(lemon_juice * sec_servings / Servings), 'cup(s) lemon juice')
print('{:.2f}'.format(Water * sec_servings / Servings), 'cup(s) water')
print('{:.2f}'.format(Agave_nectar * sec_servings / Servings), 'cup(s) agave nectar')
print()

print('Lemonade ingredients - yields', '{:.2f}'.format(sec_servings), 'servings')
print('{:.2f}'.format(lemon_juice * sec_servings / Servings / 16), 'gallon(s) lemon juice')
print('{:.2f}'.format(Water * sec_servings / Servings / 16), 'gallon(s) water')
print('{:.2f}'.format(Agave_nectar * sec_servings / Servings / 16), 'gallon(s) agave nectar')


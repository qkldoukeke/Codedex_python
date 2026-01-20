# Write code below 💖

def get_item(i):
  if i == 1:
    return '🍔 Cheeseburger'
  elif i == 2:
    return '🍟 Fries'
  elif i == 3:
    return '🥤 Soda'
  elif i == 4:
    return '🍦 Ice Cream'
  elif i == 5:
    return '🍪 Cookie'
  else:
    return 'invalid option'

def welcome():
  print('welcome!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order?'))
print(get_item(option))
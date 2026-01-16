# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
answer = int(input('Enter your answer (1-2): '))
if answer == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print( "Wrong input.")

print("Q2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer = int(input('Enter your answer (1-4): '))
if answer == 1:
  Hufflepuff += 2
elif answer == 2:
  Slytherin += 2
elif answer == 3:
  Ravenclaw += 2
elif answer == 4:
  Gryffindor += 2
else:
  print("Wrong input.")

print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer = int(input('Enter your answer (1-4): '))
if answer == 1:
  Hufflepuff += 4
elif answer == 2:
  Slytherin += 4
elif answer == 3:
  Ravenclaw += 4
elif answer == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

print("Hufflepuff:" + str(Hufflepuff))
print("Slytherin:" + str(Slytherin))
print("Ravenclaw:" + str(Ravenclaw))
print("Gryffindor:" + str(Gryffindor))

height = Hufflepuff
if Slytherin > height:
  height = Slytherin
if Ravenclaw > height:
  height = Ravenclaw
if Gryffindor > height:
  height = Gryffindor

print(height)


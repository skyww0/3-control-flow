Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0

answer1=int(input("Do you like 1)dawn or 2)dusk?:"))

if answer1==1:
  Gryffindor+=1
  Ravenclaw+=1

else:
  Hufflepuff+=1
  Slytherin+=1


answer2=int(input("when im dead i want people to remember me as? 1)the good 2)the great 3)the wise 4)the bold:"))

if answer2==1:
  Hufflepuff+=2
elif answer2==2:
  Slytherin+=2
elif answer2==3:
  Ravenclaw+=2
elif answer2==4:
  Gryffindor+=2
else:
  print('Wrong output.')


answer3=int(input("what kind of instrument most pleases your ear? 1)the violin 2)the trumpet 3)the piano 4)the drum:"))

if answer3==1:
  Slytherin+=4
elif answer3==2:
  Hufflepuff+=4
elif answer3==3:
  Ravenclaw+=4
elif answer3==4:
  Gryffindor+=4
else:
  print("Wrong output")

print("house scores:")

print("Gryffindor:", Gryffindor)
print("Slytherin:", Slytherin)
print("Ravenclaw:", Ravenclaw)
print("Hufflepuff:", Hufflepuff)

  


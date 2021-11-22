import random
animals=['dog','puppy','cat','kitten','rabbit','hamster','chinchilla','guenia pig','mouse','rat']
birds=['penguin','dove','swan','owl','crane','sparrow']
sound=['moo','roar','tweet','bark','purr','quack','squeak']
option1=random.choice(animals)
option2=random.choice(birds)
option3=random.choice(sound)
print(option1+' and '+option2+' are '+option3)
input()
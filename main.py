print("it is loving score game : ")
your_name = input("please enter your name : ")
gf_name = input("please enter your gf name : ")

lover_combine = your_name + gf_name
lover_name = lover_combine.lower()

t = lover_name.count('t')
r = lover_name.count('r')
u = lover_name.count('u')
e = lover_name.count('e')

true = t+r+u+e

l = lover_name.count('l')
o = lover_name.count('o')
v = lover_name.count('v')
e = lover_name.count('e')

love = l+o+v+e

love_score = str(true + love)
print(love_score)
number=int(input('enter the number:'))


import inflect
p = inflect.engine()

x=p.number_to_words(number)

print(x)

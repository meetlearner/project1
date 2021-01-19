print ('Meet H Chokshi 301023542')
print()
fruit = []
initialStock = []
sold = []
inStock = []
j=0
while j<4:
    fruit1=input('Enter the name of the fruit: ')
    fruit.append(fruit1)
    j=j+1
print(fruit)
f=0
while f<4:
    inStock1=input('Enter the Kgs for' +fruit[0]+' then '+fruit[1]+' then '+fruit[2]+' and last for '+fruit[3]+': ')
    fruit.append(inStock1)
    f=f+1
print(inStock)

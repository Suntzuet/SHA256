#print("Paco")
#print("sa matao")

#first_name="Work"
#last_name="Book"
#print(type(name))

#age = 23
#age += 1
#print("Your age is "+ str(age))

#height = 250.5
#print(height)
#print("Your height is:" + str(height) + "cm")

#human = False
#print(human)
#print("Are u a human?:" + str(human))

#name, age, atractive = Bro, 21, True
#Spongebob = Patrick = Anthony= 32
#print(Spongebob + Patrick)
#name = "bro code"
#print(len(name))
#print(name.find("C"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("o"))
#print(name*3)

#x = 2
#y = 1.0
#z = "3"
#print(x)
#print(int(y))
#print(int(z)*3)
#y = bool(y)
#print(y)

#name = input("What's ur name?: ")
#age = int(input("How old are you?: "))
#height = float(input("how tall ru?: "))
#age = age + 1
#print("ur " + name)
#print("ur " + str(age) + " yo")
#print("ur " + str(height)+ " though")

#import math

#pi = 3.14
#x = 5
#y= 3.4
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,3)) la potencia
#print(math.sqrt(pi))
#print(max(pi, x, y))
#print(min(x,y))

#           indexing[] [=inclusivo ]=exclusivo
#           slice() (=desde el inicio )= desde el final -|n|, es exclusivo
#           [start:stop:step]

#name= "Bro Code"
#first_name= name[:3]
#last_name= name[4:]
#funky_name= name[::2]
#reversed_name= name[::-1]
#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

#website = "http://google.com"
#website2= "http://wikipedia.com"
#slice = slice(7,-4)

#print(website[slice])
#print(website2[slice])

#age = int(input("How old ru? :"))

#input("How many rows?: ")if age == 100:

#    print("u goddam old")
#elif age >= 18:
#    print("UR overage")
#elif age<0:
#    print("depending on the country ur have not bornyet"
#else:
#    print("U not overage")

#logical operators (and, or, not)
#temp = int(input("What's the temperature outside?: "))

#if not(temp >=0 and temp <= 30):
#    print ("good temp outside")
#elif not(temp >0):
#     print ("kinda warm")

#while 1==1:
#    print("Help im stuck")

#name = None

#while not name:
#    name = input ("Write ur name: ")
#print ("Hello " + name)

#for i in range(50, 100+1, 2):
#    print(i)

#for i in "Bro Code":
#    print(i)

#import time

#for seconds in range(11, 0, -1):
#    print(seconds)
#    time.sleep(1)
#print("Happy new year")

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol =  input("Choose a symbol: ")

#for i in range(rows):
#   for j in range(columns):
#       print(symbol, end="") end hace q no pase a la line de debajo el código
#   print() aqui pasa a la línea de debajo

#while True:
#    name = input("Enter ur name: ")
#        if name != " ":
#            break

#phone_number= "123-456-789"

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

#for i in range(1,20):
#    if i == 13:
#        pass
#    else:
#        print(i,end="")

#food= ["pizza","hamburgers","Hot Dogs", "Spaghetti"]
#for i in food:
#    print(i)

#food.append("ice cream")
#food.remove("Hot Dogs")
#food.pop() remove last element
#food.insert(0,cake)
#food.sort()
#food.clear()all of the elements

#drinks = ["cofee", "soda", "tea"]
#dinner= ["pizza","hamburgers","Hot Dogs", "Spaghetti"]
#dessert = ["cake", "fruit"]

#food=[drink, dinner, dessert]
#print(food[0],[0],[0])

#student = ("Bro", 21, "male")
#print(student.count("Bro"))  n de bro
#print(student.index("male")) posición

#for x in student:
#    print(x)

#if "Bro" in student:
#    print("Bro is here")

#utensils = {"fork", "spoon", "knife"}
#dishes = {"bowl", "plate", "cup", "knife"}
#dinner_table = utensils.union(dishes)
#for x in utensils:
#    print(x)

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dishes.update(utensils)
#print(utensils.difference(dishes))
#print(dishes.difference(utensils))
#print(utensils.intersection(dishes))

#capitals = {'USA':'Washington DC',
#            'Spain':'Madrid',
#            'Japan':'Tokio',
#            'Russia':'Moscow'}
#print(capitals['Germany'])
#print(capitals.get['Germany'])
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for key,value in capitals.items():
#    print(key, value)

#capitals.update({'Germany': 'Berlin'})
#capitals.update({'USA': 'Las Vegas'})
#capitals.pop('USA')
#capitals.clear()

#print(capitals['USA'])

name = "bro Code"

#if(name[0].islower()):
#    print("yep")

#first_name = name[0:3].upper()
#last_name = name[4:].lower()
#last_character = name[-1]

#print(last_name)
#print(first_name)
#print(last_character)

#def hello(name):
#    print("hello " + name)
#    print("Have a nice day")

#hello("Bro")
#my_name = "BRO"

#hello(my_name)

#def multiply(n1,n2):
##    result=n1*n2
##    return result
#    return n1*n2
#print(multiply(6,8))

#def hello(first,middle,last):
#    print("Hello" + first + middle + last)
#hello(middle="larry",last="catula", first="paco")

#print(round(abs(float(input("Enter a whole positive number: ")))))

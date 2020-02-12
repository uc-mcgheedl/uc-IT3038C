import time


start_time = time.time()
print('What is your name?')
myName = input()
print('Hello, ' + myName + '. That is a good name.')
myAge = int(input())

if  myAge < 13:
    print("You're just a kid")
elif myAge == 13:
    print("You're a teenager")
elif myAge > 13 and myAge < 13:
    print("you're young and dumb")
elif myAge >=30 and myAge < 65:
    print("you're adulting")
else:
    print("youre still alive")

programAge = int(time.time() - start_time)
print("%s? That's funny, Im only a %s seconds old" % (myAge, programAge))
print("I wish I was " + str(int(myAge) *  2) + " years old")


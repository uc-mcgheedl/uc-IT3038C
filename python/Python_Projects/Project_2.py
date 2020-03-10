import random
import time


num = random.randint(1, 99)
print(num)

# Starting the timer 
start = time.time()
tries = 0

try:
    guess = int(input("Enter a Number between 1 - 99: "))
except ValueError:
            print ("This is not a number. Please enter a number between the bounds of 1 - 99 tosser")
            tries +=1
finally:
        
    
#Looping until user answers correctly
    while num != "" :
        try:
        
            tries +=1
        
            if guess > 99 or guess < 1:
                print("Please enter a number between the bounds of 1 - 99")
                guess = int(input("Guess again: "))
            elif guess < num:
                print ("Too Low!")
                guess = int(input("Guess again: "))
            elif guess > num:
                print ("Too high!")
                guess = int(input("Guess again: "))
            else:
                elapsed = time.time() - start
                print ("Great Job! You guessed the number in %s tries and in %d seconds" %(str(tries), elapsed))
                break
        
            # Error checking for non number input
        except ValueError:
            print ("This is not a number. Please enter a number between the bounds of 1 - 99")

  

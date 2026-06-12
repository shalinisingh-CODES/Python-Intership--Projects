import random
 
secret_number=random.randint(1,100)

max_attempts= 10

attempt =0

print("Number Guessing Game")
print("You have 10 attempts to guess it")

while attempt < max_attempts:
    Guess = int(input("enter your guess :- "))
    attempt= attempt+1
    if Guess == secret_number:
       print("CORRECT!  You guessed the number in",attempt,"attempts!")
       break
    elif  Guess < secret_number:
        print("Too low , try a higher number")
    else:
        print("Too high, try a lower number")

    attempts_left = max_attempts-attempt
    print("you have",attempts_left,"attempts left")
    if attempt== max_attempts:
      print("Sorry , you ran out of attempts")
      print("the number was",secret_number)
    
      
   
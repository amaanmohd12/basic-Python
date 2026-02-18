import random
secret_number=random.randint(1,100)
attempts=0
while True:
    try:
        guess=int(input("Enter the guess(1-100):"))
        attempts+=1
        if guess > secret_number:
          print("Too High")
        elif guess < secret_number:
          print("Too Low")
        else:
          print("Congratulations you guessed it!")
          print("You guessed in",attempts,"attempts")
          break 
    except ValueError:
       print("Please enter a valid number!")       

        

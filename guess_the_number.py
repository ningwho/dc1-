import random

guess_tried
secret_number = random.randint(1,10)

print "I'm thinking of a number between 1 and 10."
while True:
    guess = int(raw_input("What's the number? "))
    if guess == secret_number:
        print "Yes, you win!"
        break
    elif guess < secret_number:
        print 'Too high. Try again'
    elif guess < secret_number:
        print 'Too low. Try again.'
    else:
        print 'Nope, try again'

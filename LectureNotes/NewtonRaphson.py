


epsilon = 0.01
y = 24.0
guess = y/2
numGuesses = 0

while abs(guess**2 - y) >= epsilon:
    numGuesses += 1
    guess = guess-((guess**2-y) / 2*guess)

# find the square root of y using Newton Raphson, the guess is the root



import time
start_time = time.time()
num = 61412
epsilon = 1
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**2 - num) >= epsilon and guess <= num:
    guess += increment
    num_guesses += 1

end_time = time.time()
print('num_guesses =', num_guesses)
if abs(guess**2 - num) >= epsilon:
    print('Failed on cube root of', num)
else:
    print(guess, 'is close to the cube root of', num)
print("The time taken to get the cube root: ", end_time - start_time)

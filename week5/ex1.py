import numpy as np

def steepest_descent(initial_guess, learning_rate, iterations):
    x, y = initial_guess
    
    for i in range(iterations):
        gradient = np.array([2 * (x - 2), 2 * (y + 1)])
        update = -learning_rate * gradient
        x, y = x + update[0], y + update[1]
        
        print(f"Iteration {i+1}: x = {x}, y = {y}, f(x, y) = {(x - 2)**2 + (y + 1)**2}")
        
    return x, y

# Parameters
initial_guess = [0, 0]
learning_rate = 0.1
iterations = 10

# Running the steepest descent algorithm
result = steepest_descent(initial_guess, learning_rate, iterations)
print(f"Final result: x = {result[0]}, y = {result[1]}")

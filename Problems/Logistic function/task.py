import math

def sigmoid(x):
    x = float(x)
    y = math.exp(x) / (math.exp(x) + 1)
    return round(y, 2)

user_input = input()

print(sigmoid(user_input))


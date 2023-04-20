import math
import matplotlib.pyplot as plt

def binomial(n, al, x):
    
    
    
    J = 1 - al  # interactions are related to the magnetic field
    #  binomial coefficient
    coef = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    # transition prob
    prob = coef * (al ** x) * (J ** (n - x))
    return prob


n = 10
al = 0.5


probs = [binomial(n, al, x) for x in range(n+1)]


fig, ax = plt.subplots()
ax.bar(range(n+1), probs)
ax.set_xlabel('Number of Successes')
ax.set_ylabel('Probability')
plt.show()

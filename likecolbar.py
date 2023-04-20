import math
import matplotlib.pyplot as plt
import numpy as np

def binomial_likelihood(n, al, x):
    
    
    
    J = 1 - al
    coef = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    likelihood = coef * (al ** x) * (J ** (n - x))
    return likelihood


n = 10
x = 5


max_likelihood = 0
best_al = 0
al_vals = []
likelihoods = []
for al in range(0, 101):
    al = al / 100.0
    al_vals.append(al)
    likelihood = binomial_likelihood(n, al, x)
    likelihoods.append(likelihood)
    if likelihood > max_likelihood:
        max_likelihood = likelihood
        best_al = al

print(f"The maximum likelihood estimate is {best_al:.2f} with a likelihood of {max_likelihood:.5f}")


fig, ax = plt.subplots()
cmap = plt.cm.Reds
heatmap = ax.pcolormesh([al_vals], [0, 1], [likelihoods], cmap=cmap, shading='auto')
ax.set_xlabel('Probability of Success')
ax.set_ylabel('Trial')
ax.set_xticks(np.arange(0, 1.1, 0.1))
fig.colorbar(heatmap)
plt.show()

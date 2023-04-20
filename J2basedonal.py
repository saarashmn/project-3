import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from binlike2 import binomial_likelihood

# Define the parameters
n = 20
j1_vals = np.linspace(0.01, 0.99, 50)
j2_vals = np.linspace(0.01, 1.99, 50)

# Calculate the likelihood values
likelihoods = np.zeros((len(j1_vals), len(j2_vals)))
for i, j1 in enumerate(j1_vals):
    for j, j2 in enumerate(j2_vals):
        likelihoods[i,j] = binomial_likelihood(al=10, j1=j1, j2=j2, n=n)

# Find the maximum likelihood
max_likelihood = np.max(likelihoods)
max_likelihood_idx = np.unravel_index(np.argmax(likelihoods, axis=None), likelihoods.shape)
max_j1 = j1_vals[max_likelihood_idx[0]]
max_j2 = j2_vals[max_likelihood_idx[1]]

fig, ax = plt.subplots()
im = ax.imshow(likelihoods, cmap='viridis', extent=[0, 1, n, 0], aspect='auto')
ax.set_xlabel('p')
ax.set_ylabel('al')
ax.set_title(f'Likelihood based on J1 and J2')
fig.colorbar(im, ax=ax)
plt.show()


max_likelihood = np.max(likelihoods)
max_likelihood_idx = np.unravel_index(np.argmax(likelihoods, axis=None), likelihoods.shape)
max_p = p_vals[max_likelihood_idx[1]]
max_al = al_vals[max_likelihood_idx[0]]


print(f'Maximum likelihood: {max_likelihood:.4f}')
print(f'p at max likelihood: {max_p:.4f}')
print(f'al at max likelihood: {max_al:.4f}')

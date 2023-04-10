#Syd Aarash Maroufian

import numpy as np
from scipy.stats import norm

# Simulate the experiment
realJ = 2
realalpha = 0.3
nexp= 100
data = simulate_experiment(realJ, realalpha, nexp)


def simulate_experiment(J, alpha, nexp):
    """Simulate an experiment with a normal distribution and return the data"""
    return np.random.binomial(J, alpha, size=nexp)

def likelihood(mu, data):
    """Calculate the likelihood function for a normal distribution"""
    return np.prod(norm.pdf(data, loc=mu))

def estimate_parameter(data):
    """Estimate the parameter mu using maximum likelihood estimation"""
    return np.mean(data)

# Estimate the parameter using maximum likelihood estimation
estimated_J = estimate_parameter(data)

print(f"True mu: {real J}")
print(f"Estimated mu: {estimated J}")

# Calculate the likelihood function for a range of mu values
mu_values = np.linspace(0, 10, 1000)
likelihoods = [likelihood(mu, data) for mu in mu_values]

# Plot the likelihood function
plt.plot(mu_values, likelihoods)
plt.axvline(mu_estimated, color='purple', linestyle='--')
plt.xlabel('normal distribution mean (mu)')
plt.ylabel('Likelihood')
plt.title('Likelihood function for estimating mu')
plt.show()

n_bootstraps = 1000
bootstrapped_estimates = []
for i in range(n_bootstraps):
    bootstrap_data = np.random.choice(data, size=nexp, replace=True)
    bootstrap_estimate = estimate_parameter(bootstrap_data)
    bootstrapped_estimates.append(bootstrap_estimate)

# Calculate the confidence interval
lower_bound = np.percentile(bootstrapped_estimates, 2.5)
upper_bound = np.percentile(bootstrapped_estimates, 97.5)
print(f"Estimated mu: {mu_estimated:.2f}")
print(f"Confidence interval: [{lower_bound:.2f}, {upper_bound:.2f}]")

 

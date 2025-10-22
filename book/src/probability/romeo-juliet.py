import matplotlib.pyplot as plt 
import numpy as np
from numpy.random import sample 

def monte_carlo_romeo_juliet(n_simulations=10000, wait_time=0.25):
    romeo_arrivals = np.random.uniform(0,1,n_simulations)
    juliet_arrivals = np.random.uniform(0,1,n_simulations)

    #check the meeting conditions for each pair 

    time_differences = np.abs(romeo_arrivals - juliet_arrivals)
    they_meet = time_differences <= wait_time

    #count success 

    number_of_meetings = np.sum(they_meet)

    #estimate the probability
    estimated_prob = number_of_meetings / n_simulations


    return estimated_prob, romeo_arrivals, juliet_arrivals, they_meet



#visualize the convergence. How estimates improve with more trials 

def show_convergence():
    """show how the monte-carlo-estimates converge to true value"""
    sample_sizes = [10,50,100,500,1000,5000,10000,50000]
    estimates = []
    for n in sample_sizes:
        prob, _, _, _ = monte_carlo_romeo_juliet(n_simulations=n)
        estimates.append(prob)
    plt.figure(figsize=(10,6))
    plt.semilogx(sample_sizes, estimates, 'bo-', label='MC Estimate')
    plt.axhline(y=7/16, color='r', linestyle='--', label='True probability')
    plt.xlabel('Number of simulations')
    plt.ylabel('Estimated Probability')
    plt.title('Monte Carlo Covergence')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

        


# run the simulations 
np.random.seed(42)
prob, romeo, juliet, meet = monte_carlo_romeo_juliet(
    n_simulations=10000,
    wait_time=0.25
)

#Display Results 
print(f"Monte Carlo Simulations Results:")
print(f"Number of simulations: 10,000")
print(f"Number of meetings: {np.sum(meet)}")
print(f"The estimated probability:{prob:0.4f}({prob*100:0.2f}%)")
print(f"\n Theoretical probability: 7/16 = {7/16:0.4f}({7/16*100:0.2f}%)")
print(f"Estimation error: {abs(prob - 7/16):0.4f}")
show_convergence()










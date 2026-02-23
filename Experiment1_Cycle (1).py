import matplotlib.pyplot as plt
import random
from graph import create_random_graph, has_cycle

#Saira: Experiment Setup
def run_experiment():
    n_vals = [75, 100, 125]   # different graph sizes
    runs_per_m = 150          # number of random graphs per edge count

    print("Experiment 1: Cycle Probability vs Number of Edges loading ...")

    plt.figure(figsize=(10, 6))

    for n in n_vals:
        print(f"\n Testing experiment for given n = {n}") # run an experiment for each n

        m_vals = list(range(0, n + 51, 10)) 
        m_vals_norm = [m / n for m in m_vals]
        cycle_probs = []

        for m in m_vals:
            cycle_count = 0
            for _ in range(runs_per_m):
                G = create_random_graph(n, m)
                if has_cycle(G):
                    cycle_count += 1

            cycle_prob = cycle_count / runs_per_m
            cycle_probs.append(cycle_prob)
            
#Saira: Plotting of graphs of nodes 50, 100, 150 
        plt.plot(m_vals_norm, cycle_probs, marker='o', label=f'n = {n}')  # plotting curves for each n

    plt.title('Experiment 1: Probability of Cycle vs Number of Edges per Node (m/n)')
    
    plt.ylabel('Cycle Probability')
    plt.xlabel('Number of Edges per Node (m/n)')
    plt.legend()
    plt.grid(True)

    output_filename = 'experiment1_cycle_probability_multiple_n.png'
    plt.savefig(output_filename, dpi=300)
    print(f"\nGraph saved to {output_filename}")

if __name__ == "__main__":
    run_experiment()
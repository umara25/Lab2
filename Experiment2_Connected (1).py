import matplotlib.pyplot as plt
import random
from graph import create_random_graph, has_cycle, is_connected

#Saira: Experiment 2 Setup
def run_experiment_2():
    n_vals = [75, 100, 125]   # differing node sizes for graph generation
    runs_per_m = 150          # number of random graphs per edge count

    print("Experiment 2: Connected Probability vs Number of Edges Experiment Loading ...")
    plt.figure(figsize=(10, 6))

    for n in n_vals:
        print(f"\n Testing the experiment for a given n = {n}")  # run an experiment for each n

        m_vals = list(range(0, 2*n+1, 10))
        m_vals_norm = [m/n for m in m_vals]
        connected_probs = []

        for m in m_vals:
            c_count = 0
            for _ in range(runs_per_m):
                G = create_random_graph(n, m)
                if is_connected(G):
                    c_count += 1
            connected_prob = c_count / runs_per_m
            connected_probs.append(connected_prob)
            
#Saira: Experiment 2 plotting of different graph sizes
        plt.plot(m_vals_norm, connected_probs, marker='o', label=f'n = {n}')

    plt.title('Experiment 2: Probability of Connectivity vs Edges per Node (m/n)')
    
    plt.ylabel('Connected Probability')
    plt.xlabel('Edges per Node (m/n)')
    plt.legend()
    plt.grid(True)

    output_filename = 'experiment2_connected_probability.png'
    plt.savefig(output_filename, dpi=300)
    print(f"\nGraph saved to {output_filename}")

if __name__ == "__main__":
    run_experiment_2()
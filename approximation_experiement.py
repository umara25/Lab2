import matplotlib.pyplot as plt
from graph import create_random_graph, MVC, approx1, approx2, approx3

#Yusuf: Approximation experiment comparing approx1, approx2, approx3 against MVC
def run_approximation_experiment():
    n = 8
    runs = 1000
    m_vals = list(range(1, 29, 3))

    ratio1, ratio2, ratio3 = [], [], []

    print("Approximation Experiment loading ...")

    for m in m_vals:
        mvc_total = 0
        a1_total = 0
        a2_total = 0
        a3_total = 0

        for _ in range(runs):
            G = create_random_graph(n, m)
            mvc_total += len(MVC(G))
            a1_total += len(approx1(G))
            a2_total += len(approx2(G))
            a3_total += len(approx3(G))

        if mvc_total == 0:
            ratio1.append(1.0)
            ratio2.append(1.0)
            ratio3.append(1.0)
        else:
            ratio1.append(a1_total / mvc_total)
            ratio2.append(a2_total / mvc_total)
            ratio3.append(a3_total / mvc_total)

        print(f"m = {m} done")

    plt.figure(figsize=(10, 6))
    plt.plot(m_vals, ratio1, marker='o', label='approx1')
    plt.plot(m_vals, ratio2, marker='o', label='approx2')
    plt.plot(m_vals, ratio3, marker='o', label='approx3')
    plt.axhline(y=1.0, color='black', linestyle='--', label='MVC (optimal)')
    plt.title('Approximation Performance vs Number of Edges (n=8, 1000 runs)')
    plt.xlabel('Number of Edges (m)')
    plt.ylabel('Approximation Size / MVC Size')
    plt.legend()
    plt.grid(True)
    plt.savefig('approximation_experiment_n8.png', dpi=300)
    print("Graph saved to approximation_experiment_n8.png")


#Umar: Second experiment varying node size to see how approximations scale
def run_node_size_experiment():
    n_vals = [6, 8, 10]
    runs = 500

    print("\nNode size experiment loading ...")

    plt.figure(figsize=(10, 6))

    for n in n_vals:
        max_edges = n * (n - 1) // 2
        m_vals = list(range(1, max_edges + 1, max(1, max_edges // 10)))
        if m_vals[-1] != max_edges:
            m_vals.append(max_edges)

        ratios1, ratios2, ratios3 = [], [], []
        proportions = []

        for m in m_vals:
            mvc_total = 0
            a1_total = 0
            a2_total = 0
            a3_total = 0

            for _ in range(runs):
                G = create_random_graph(n, m)
                mvc_total += len(MVC(G))
                a1_total += len(approx1(G))
                a2_total += len(approx2(G))
                a3_total += len(approx3(G))

            if mvc_total > 0:
                ratios1.append(a1_total / mvc_total)
                ratios2.append(a2_total / mvc_total)
                ratios3.append(a3_total / mvc_total)
            else:
                ratios1.append(1.0)
                ratios2.append(1.0)
                ratios3.append(1.0)
            proportions.append(m / max_edges)

        plt.plot(proportions, ratios1, marker='o', markersize=3, label=f'approx1 n={n}')
        plt.plot(proportions, ratios2, marker='s', markersize=3, label=f'approx2 n={n}')
        plt.plot(proportions, ratios3, marker='^', markersize=3, label=f'approx3 n={n}')

        print(f"n={n} done")

    plt.axhline(y=1.0, color='black', linestyle='--', label='MVC (optimal)')
    plt.title('Approximation Performance vs Edge Proportion for Different n')
    plt.xlabel('Proportion of Maximum Edges')
    plt.ylabel('Approximation Size / MVC Size')
    plt.legend(fontsize=8)
    plt.grid(True)
    plt.savefig('approximation_experiment_node_size.png', dpi=300)
    print("Graph saved to approximation_experiment_node_size.png")


#Yusuf: Third experiment showing worst case performance of approx1 on small graphs
def run_worst_case_experiment():
    n = 8
    runs = 1000
    m_vals = list(range(1, 29, 3))

    worst1, worst2, worst3 = [], [], []

    print("\nWorst case experiment loading ...")

    for m in m_vals:
        w1, w2, w3 = 0, 0, 0

        for _ in range(runs):
            G = create_random_graph(n, m)
            mvc_size = len(MVC(G))
            if mvc_size > 0:
                r1 = len(approx1(G)) / mvc_size
                r2 = len(approx2(G)) / mvc_size
                r3 = len(approx3(G)) / mvc_size
                if r1 > w1:
                    w1 = r1
                if r2 > w2:
                    w2 = r2
                if r3 > w3:
                    w3 = r3

        worst1.append(w1)
        worst2.append(w2)
        worst3.append(w3)
        print(f"m = {m} done")

    plt.figure(figsize=(10, 6))
    plt.plot(m_vals, worst1, marker='o', label='approx1 worst case')
    plt.plot(m_vals, worst2, marker='o', label='approx2 worst case')
    plt.plot(m_vals, worst3, marker='o', label='approx3 worst case')
    plt.axhline(y=1.0, color='black', linestyle='--', label='MVC (optimal)')
    plt.title('Worst Case Approximation Performance vs Number of Edges (n=8, 1000 runs)')
    plt.xlabel('Number of Edges (m)')
    plt.ylabel('Worst Case Approx Size / MVC Size')
    plt.legend()
    plt.grid(True)
    plt.savefig('approximation_experiment_worst_case.png', dpi=300)
    print("Graph saved to approximation_experiment_worst_case.png")


if __name__ == "__main__":
    run_approximation_experiment()
    run_node_size_experiment()
    run_worst_case_experiment()
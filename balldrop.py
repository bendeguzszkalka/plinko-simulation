import random
from collections import Counter as Counter

multipliers = [10, 5, 2, 0.7, 0.2, 0.7, 2, 5, 10,0,0,0,0,0,0,0,0,0,0,0,0]

def Play(games=1, bet=500, lines=8, mult=multipliers):
    holes = lines + 1
    results = []
    reward = []
    for game in range(games):
        r = 0
        for line in range(lines):
            if (random.randint(0, 1) == 1):
                r += 1
        results.append(r)
        reward.append(bet*mult[r])
    cost = games*bet
    results_sorted = dict(sorted(Counter(results).items()))
    print(f"The balls fell into these holes: {results_sorted}.")
    print(f"Your costs: {cost}.")
    print(f"You got back: {sum(reward)}.")
    return(results_sorted)

def plot(data):
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats import norm

    x = list(data.keys())
    y = list(data.values())

    # Adjust the figure size based on the number of data points
    fig_width = len(x) * 1.0  # 1 unit width per data point
    fig_height = 6            # Fixed height for visibility

    # Create the plot with dynamic figure size
    plt.figure(figsize=(fig_width, fig_height))
    plt.bar(x, y)

    # Add labels and title
    plt.xlabel('Holes')
    plt.ylabel('Balls in holes')
    plt.title('Bar Plot of the Ball Drop Game')

#    mean, std_dev = norm.fit(y)
#    x_curve = np.linspace(min(x), max(x), 100)
#    y_curve = norm.pdf(x_curve, mean, std_dev) * max(y)  # Scale by max(y) for overlay
#    y_curve_scaled = y_curve * (max(y) / max(y_curve))
#    plt.plot(x_curve, y_curve_scaled, color='red', label='Normal Distribution', linewidth=2)

    # Display the plot
    plt.legend()
    plt.grid(True, axis='y')
    plt.show()

results_sorted = Play(games=1000000, bet=500, lines=20)
plot(results_sorted)
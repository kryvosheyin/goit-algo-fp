import numpy as np
import matplotlib.pyplot as plt


def simulate_dice_rolls_numpy(num_simulations):
    rng = np.random.default_rng()
    # generating all dice rolls and sum them
    total_sums = np.sum(rng.integers(1, 7, size=(num_simulations, 2)), axis=1)
    sum_counts = np.bincount(total_sums, minlength=13)[2:]
    probabilities = sum_counts / num_simulations
    return probabilities


def display_probabilities(probabilities):
    print(f"{'Sum':<5}|{'Probability':5}")
    print("--------------------")
    for sum_value, probability in zip(range(2, 13), probabilities):
        print(f"{sum_value:<5}|{probability:.4f}")


def plot_probabilities(probabilities):
    sums = np.arange(2, 13)
    plt.bar(sums, probabilities, align="center", alpha=0.7)
    plt.xlabel("Sum of Dice")
    plt.ylabel("Probability")
    plt.title("Probabilities of Sum of Two Dice Rolls")
    plt.xticks(sums)
    plt.show()


if __name__ == "__main__":
    num_simulations = 1_000_000
    probabilities = simulate_dice_rolls_numpy(num_simulations)
    display_probabilities(probabilities)
    plot_probabilities(probabilities)

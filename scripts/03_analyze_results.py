import pandas as pd
import matplotlib.pyplot as plt

def analyze_inspection_results(results_path, renewal_data_path, output_path):
    results = pd.read_csv(results_path)
    renewal_data = pd.read_csv(renewal_data_path)

    mean_observed = results["Observed Intervals"].mean()
    mean_interarrival = renewal_data["Interarrival Times"].mean()

    print(f"Mean Observed Interval: {mean_observed}")
    print(f"Mean Interarrival Time: {mean_interarrival}")

    results["Observed Intervals"].hist(bins=30, alpha=0.7)
    plt.axvline(mean_observed, color="r", linestyle="--", label="Mean Observed")
    plt.axvline(mean_interarrival, color="g", linestyle="--", label="Mean Interarrival")
    plt.legend()
    plt.title("Histogram of Observed Intervals")
    plt.xlabel("Interval Length")
    plt.ylabel("Frequency")
    plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    analyze_inspection_results(
        "outputs/inspection_results.csv",
        "outputs/renewal_data.csv",
        "outputs/interval_histogram.png"
    )
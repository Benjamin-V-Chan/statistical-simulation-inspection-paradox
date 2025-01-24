import pandas as pd
import numpy as np

def inspect_intervals(cumulative_times, num_samples):
    max_time = cumulative_times.iloc[-1]
    inspection_times = np.random.uniform(0, max_time, num_samples)
    observed_intervals = []

    for t in inspection_times:
        interval_start = cumulative_times[cumulative_times <= t].iloc[-1]
        interval_end = cumulative_times[cumulative_times > t].iloc[0]
        observed_intervals.append(interval_end - interval_start)
    
    return pd.DataFrame({"Inspection Times": inspection_times, "Observed Intervals": observed_intervals})

if __name__ == "__main__":
    renewal_data = pd.read_csv("outputs/renewal_data.csv")
    results = inspect_intervals(renewal_data["Cumulative Times"], 500)
    results.to_csv("outputs/inspection_results.csv", index=False)
import numpy as np
import pandas as pd

def generate_interarrival_times(num_events, dist_type="exponential", **kwargs):
    if dist_type == "exponential":
        rate = kwargs.get("rate", 1)
        interarrivals = np.random.exponential(1 / rate, num_events)
    elif dist_type == "uniform":
        low = kwargs.get("low", 0)
        high = kwargs.get("high", 1)
        interarrivals = np.random.uniform(low, high, num_events)
    else:
        raise ValueError("Unsupported distribution type.")
    
    cumulative_times = np.cumsum(interarrivals)
    return pd.DataFrame({"Interarrival Times": interarrivals, "Cumulative Times": cumulative_times})

if __name__ == "__main__":
    data = generate_interarrival_times(1000, dist_type="exponential", rate=0.5)
    data.to_csv("outputs/renewal_data.csv", index=False)
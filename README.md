# statistical-simulation-inspection-paradox

## Project Overview

This project simulates and analyzes the **Inspection Paradox** in Renewal Theory. The Inspection Paradox is a counterintuitive statistical phenomenon where intervals observed at random points in time tend to be longer than the average interval in the process. This occurs because longer intervals are more likely to be sampled when choosing random points in time.

### Mathematical Background

Let the interarrival times of a renewal process be given by $\{X_1, X_2, \dots\}$, where each $X_i$ is independently and identically distributed. The cumulative arrival times are:

$$S_n = \sum_{i=1}^n X_i$$

For a random inspection time $T$, the interval containing $T$ is determined by:

$$I(T) = \min\{n : S_{n-1} \leq T < S_n\}$$

The length of this interval is given by:

$$L(T) = S_n - S_{n-1}$$

The Inspection Paradox emerges because the probability of sampling an interval of length $x$ is proportional to $x$, leading to a higher likelihood of observing longer intervals.

For an exponential interarrival time distribution with rate parameter $\lambda$, the mean observed interval $\mathbb{E}[L(T)]$ is:

$$\mathbb{E}[L(T)] = \frac{2}{\lambda}$$

which is twice the mean interarrival time.

## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_renewal_data.py  # Generate renewal process data
│   ├── 02_simulate_inspection.py   # Simulate inspection paradox scenarios
│   ├── 03_analyze_results.py       # Analyze simulation results
│   ├── utils.py                    # Helper functions for modular use
├── outputs/
│   ├── renewal_data.csv            # Generated renewal process data
│   ├── inspection_results.csv      # Results of inspection paradox simulation
│   ├── interval_histogram.png      # Histogram of observed intervals
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
```

## Usage

### 1. Setup the Project:

Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 2. Generate Renewal Process Data:

Run the script to generate renewal data based on interarrival times:

```bash
python scripts/01_generate_renewal_data.py
```

This will create a file `outputs/renewal_data.csv` containing the interarrival times and cumulative arrival times.

### 3. Simulate the Inspection Paradox:

Simulate random inspection times and observe the intervals containing them:

```bash
python scripts/02_simulate_inspection.py
```

This will generate a file `outputs/inspection_results.csv` with the inspection times and observed intervals.

### 4. Analyze the Results:

Analyze the inspection paradox results and plot a histogram of observed intervals:

```bash
python scripts/03_analyze_results.py
```

The histogram will be saved as `outputs/interval_histogram.png`. The script will also print the mean observed interval and mean interarrival time for comparison.

## Requirements

- Python 3.8 or higher
- Required Python packages (install via `requirements.txt`):
  - numpy
  - pandas
  - matplotlib
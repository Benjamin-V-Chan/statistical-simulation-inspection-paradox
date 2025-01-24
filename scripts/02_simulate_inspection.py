# 02_simulate_inspection.py
# Purpose: Simulate the inspection paradox by sampling random points in time

# Import necessary libraries
# Load renewal process data from outputs/renewal_data.csv
# Define function to sample random inspection times within total simulation time
# For each inspection time, find the interval it falls into (inspection paradox condition)
# Compute and return the observed interval lengths
# Save the results to a CSV in outputs/
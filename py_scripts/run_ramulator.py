import os
import sys
import yaml
import subprocess
import pandas as pd
import re

# Get trace directory and output CSV filename from command-line arguments
if len(sys.argv) > 1:
    trace_dir = sys.argv[1]
else:
    trace_dir = "/home/fann/projects/cache_simulator/sampled_trace/"

if len(sys.argv) > 2:
    output_csv = sys.argv[2]
else:
    output_csv = 'perf_results.csv'

# Path to the configuration file
config_path = "../fan_config.yaml"

# Load the configuration file
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

# Get all trace files in the specified directory ending with .trace
trace_files = [f for f in os.listdir(trace_dir) if f.endswith('.txt')]

if not trace_files:
    print(f"Cannot find any .trace files in {trace_dir}")
    sys.exit(1)

for trace_filename in trace_files:
    trace_path = os.path.join(trace_dir, trace_filename)
    config['Frontend']['path'] = trace_path

    # Echo report: starting simulation for current trace file
    print(f"Starting simulation for: {trace_filename}")

    temp_config_path = "../temp/temp_config.yaml"
    with open(temp_config_path, 'w') as temp_config:
        yaml.dump(config, temp_config)

    try:
        result = subprocess.run(['../ramulator2', '-f', temp_config_path],
                                capture_output=True, text=True, timeout=300)

        with open(os.path.join("./output", "{}.out".format(trace_filename)), "w+") as f:
            f.write(result.stdout)

    except subprocess.TimeoutExpired:
        print(f"Timeout occurred for: {trace_filename}")
        continue

    # Echo report: finished simulation for current trace file
    print(f"Finished simulation for: {trace_filename}")

print(f"All simulations finished, output has been saved to {output_csv}.")

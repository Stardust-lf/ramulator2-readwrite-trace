import os
import sys
import yaml
import subprocess
import pandas as pd
import re

# Get trace directory and output CSV filename from command-line arguments
if len(sys.argv) > 1:
    trace_dir = sys.argv[1]
    out_dir_path = sys.argv[2]
    slow_freq = sys.argv[3]
else:
    trace_dir = "../traces/"
    out_dir_path = "./simu_out"

# if len(sys.argv) > 2:
#     output_file = sys.argv[2]
# else:
#     output_file = 'perf_results.txt'

# Path to the configuration file
config_path = "../fan_config.yaml"

# def extract_info(output):
#     """
#     Extracts all numerical information from the simulator output string.
#     If the same key appears more than once, its values are stored in a list.
#     """
#     info_dict = {}
#     matches = re.findall(r"(\w+):\s*([\d.]+)", output)
#     for key, value in matches:
#         try:
#             num_value = float(value)
#         except ValueError:
#             num_value = None
#         if key in info_dict:
#             if not isinstance(info_dict[key], list):
#                 info_dict[key] = [info_dict[key]]
#             info_dict[key].append(num_value)
#         else:
#             info_dict[key] = num_value
#     return info_dict


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
    config['MemorySystem']['Controller']['wait_ratio'] = str(round(6400/int(slow_freq), 3))

    # Echo report: starting simulation for current trace file
    print(f"Starting simulation for: {trace_filename} with slow chip freq {slow_freq}")

    temp_config_path = "../temp/temp_config.yaml"
    with open(temp_config_path, 'w') as temp_config:
        yaml.dump(config, temp_config)

    try:
        result = subprocess.run(['../build/ramulator2', '-f', temp_config_path],
                                capture_output=True, text=True, timeout=300)
        with open(os.path.join(out_dir_path, trace_filename), "w+") as file:
            file.writelines(result.stdout)

    except subprocess.TimeoutExpired:
        print(f"Timeout occurred for: {trace_filename}")
        continue

    # Echo report: finished simulation for current trace file
    print(f"Finished simulation for: {trace_filename}")


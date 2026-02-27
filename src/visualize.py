#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Use a font that supports Unicode characters including Korean
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial Unicode MS', 'Noto Sans CJK']
plt.rcParams['axes.unicode_minus'] = False

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# get top 10 items, sorted from low to high
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_10 = items[:10]
top_10_sorted = sorted(top_10, key=lambda item: item[1])  # sort low to high for plotting

# extract keys and values for plotting
keys = [item[0] for item in top_10_sorted]
values = [item[1] for item in top_10_sorted]

# create bar graph
plt.figure(figsize=(10, 6))
plt.bar(keys, values)
plt.xlabel('Country/Language Code')
plt.ylabel('Tweet Count')
file_type = 'Languages' if 'lang' in args.input_path else 'Countries'
plt.title(f'Top 10 {file_type}  by Tweet Count with Hashtag: {args.key}')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# generate output filename
# Extract the base filename and hashtag to create a descriptive name
input_base = os.path.basename(args.input_path).replace('.', '_')
if '코로나바이러스' in args.key:
    key_safe = 'korean'
elif 'coronavirus' in args.key:
    key_safe = 'coronavirus'
else:
    key_safe = args.key.replace('#', '').replace('/', '_')
output_filename = f'{input_base}_{key_safe}.png'

# save the plot
plt.savefig(output_filename)
print(f'Saved plot to {output_filename}')

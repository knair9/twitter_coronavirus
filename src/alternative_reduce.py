#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True, help='List of hashtags to plot')
parser.add_argument('--output_file', default='hashtag_timeline.png', help='Output PNG filename')
args = parser.parse_args()

# imports
import os
import json
import glob
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

# Dictionary to store: hashtag -> {date: count}
hashtag_data = defaultdict(lambda: defaultdict(int))

# Get all .lang files from outputs folder, sorted by date
lang_files = sorted(glob.glob('outputs/*.lang'))

print(f"Processing {len(lang_files)} files...")

# Scan through all output files
for filepath in lang_files:
    # Extract date from filename: geoTwitter20-MM-DD.zip.lang
    filename = os.path.basename(filepath)
    # Parse date - format is geoTwitterYY-MM-DD.zip.lang
    try:
        date_str = filename.split('geoTwitter')[1].split('.zip')[0]  # Gets "20-MM-DD"
        year = 2000 + int(date_str.split('-')[0])  # 2020
        month = int(date_str.split('-')[1])
        day = int(date_str.split('-')[2])
        date = datetime(year, month, day)
        day_of_year = date.timetuple().tm_yday
    except:
        print(f"Warning: Could not parse date from {filename}")
        continue
    
    # Read the file
    with open(filepath) as f:
        counts = json.load(f)
    
    # Extract counts for each requested hashtag
    for hashtag in args.hashtags:
        if hashtag in counts:
            # Sum up all languages for this hashtag on this day
            total_count = sum(counts[hashtag].values())
            hashtag_data[hashtag][day_of_year] = total_count

# Create line plot
plt.figure(figsize=(14, 8))

for hashtag in args.hashtags:
    if hashtag in hashtag_data:
        # Sort by day of year
        days = sorted(hashtag_data[hashtag].keys())
        counts = [hashtag_data[hashtag][day] for day in days]
        
        # Plot the line
        plt.plot(days, counts, marker='o', markersize=2, label=hashtag, linewidth=1.5)
    else:
        print(f"Warning: No data found for hashtag {hashtag}")

# Format the plot
plt.xlabel('Day of Year (2020)', fontsize=12)
plt.ylabel('Number of Tweets', fontsize=12)
plt.title('Hashtag Usage Over Time in 2020', fontsize=14, fontweight='bold')
plt.legend(loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the plot
plt.savefig(args.output_file, dpi=150)
print(f'Saved plot to {args.output_file}')

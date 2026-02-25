#!/bin/bash

# Loop over all 2020 tweet files in the dataset
for file in /data/Twitter\ dataset/geoTwitter20-*.zip
do
    echo "Processing: $file"
    # Run map.py in the background with nohup
    # nohup ensures it keeps running after disconnect
    # & runs it in parallel
    nohup python3 src/map.py --input_path="$file" &
done

echo "All map jobs started. Check nohup.out for progress."

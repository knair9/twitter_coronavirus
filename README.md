# Twitter Coronavirus Analysis 2020

## Project Overview
This project analyzes 1.1 billion geotagged tweets from 2020 to track the spread of coronavirus-related discussions on social media. Using the MapReduce parallel processing paradigm, I processed 366 days of Twitter data to identify patterns in hashtag usage across different languages and countries.

## Technical Implementation

### MapReduce Pipeline
- **Map Phase**: Processed 366 daily tweet files (each containing ~3 million tweets) in parallel using Python multiprocessing
- **Reduce Phase**: Aggregated results across all files to produce comprehensive statistics
- **Technologies**: Python, JSON processing, parallel computing with `nohup` and background processes

### Key Features
1. **Multilingual Analysis**: Tracked hashtags in English, Korean (코로나바이러스), Japanese (コロナウイルス), and Chinese (冠状病毒)
2. **Geographic Tracking**: Analyzed tweet distribution by country code
3. **Temporal Analysis**: Visualized hashtag trends over the entire year
4. **Data Visualization**: Created charts using matplotlib to communicate findings

## Visualizations

### Top Languages for #coronavirus
![Coronavirus by Language](reduced_lang_coronavirus.png)

English dominated coronavirus discussions, followed by Spanish and Portuguese. The "undefined" language category represents tweets where language detection was uncertain.

### Top Countries for #coronavirus
![Coronavirus by Country](reduced_country_coronavirus.png)

The United States led in coronavirus-related tweets, with significant activity from Great Britain, Brazil, and other English and Spanish-speaking nations.

### Top Languages for Korean Hashtag #코로나바이러스
![Korean Hashtag by Language](reduced_lang_korean.png)

The Korean coronavirus hashtag was primarily used by Korean speakers, with minimal crossover to other languages.

### Top Countries for Korean Hashtag #코로나바이러스
![Korean Hashtag by Country](reduced_country_korean.png)

South Korea dominated usage of the Korean hashtag, demonstrating clear geographic and linguistic clustering.

### Hashtag Usage Over Time
![Hashtag Timeline](hashtag_timeline.png)

This timeline shows the dramatic increase in coronavirus-related tweets starting in March 2020, coinciding with the WHO's pandemic declaration and global lockdowns. The data clearly shows:
- Minimal activity in January 2020
- Explosive growth in March 2020
- Sustained high activity throughout the year
- `#covid19` (without hyphen) was significantly more popular than `#covid-19` (with hyphen)

## Technical Skills Demonstrated
- Large-scale data processing (1.1 billion tweets)
- Parallel computing and process management
- Python scripting and data analysis
- Shell scripting and automation
- Data visualization with matplotlib
- Working with JSON and complex data structures
- Git version control

## Results
Successfully processed all 366 days of 2020 Twitter data, generating insights into:
- Geographic distribution of pandemic discussions
- Language preferences in crisis communication
- Temporal patterns of social media response to global events
- Hashtag adoption and virality patterns

## Repository Structure
- `src/map.py` - Mapper for counting hashtag usage by language and country
- `src/reduce.py` - Reducer for aggregating results across all days
- `src/visualize.py` - Bar chart visualization generator
- `src/alternative_reduce.py` - Time-series analysis and line plot generator
- `run_maps.sh` - Shell script for parallel execution of map jobs

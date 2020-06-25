from collections import Counter
from pprint import pprint
from pathlib import Path

import pandas as pd


def device_counts(df):
    device_ids = list(df['device_id'])
    counter = Counter(device_ids)
    repeats = {k: v for k, v in counter.items() if v > 1}
    assert sum(repeats.values()) + len(counter.keys()) - len(repeats.keys()) == len(device_ids)

    return repeats

def device_locations(base_path='.'):
    df = pd.read_csv(Path(base_path) / 'data/newcastle_date_20200320.csv',
                     sep='\t',
                     names=['date', '?1', '?2', 'latitude', 'longitude', 'device_id'])
    return df

def highest_device_count_id(counts):
    most_frequent_device_and_count = max(counts.items(), key=lambda entry: entry[1])
    most_frequent_device_id = most_frequent_device_and_count[0]
    return most_frequent_device_id

def single_device_tracking(base_path='.'):
    df = device_locations(base_path)
    #print(df)
    counts = device_counts(df)
    #print(counts)
    most_frequent_device_id = highest_device_count_id(counts)
    #print(most_frequent_device_id)
    
    rows = df[df['device_id'] == most_frequent_device_id]
    #print(rows[['latitude', 'longitude']])

    return rows[['latitude', 'longitude']]

def main():
    print(single_device_tracking())


if __name__ == '__main__':
    main()

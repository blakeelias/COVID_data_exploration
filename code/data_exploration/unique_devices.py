from collections import Counter
from pprint import pprint

import pandas as pd


def main():
    df = pd.read_csv('data/newcastle_date_20200320.csv',
                     sep='\t',
                     names=['date', '?1', '?2', 'latitude', 'longitude', 'device_id'])
    print(df)
    # print(df[df['device_id'] == 1584677574]['latitude'])

    device_ids = list(df['device_id'])

    counter = Counter(device_ids)
    repeats = {k: v for k, v in counter.items() if v > 1}
    assert sum(repeats.values()) + len(counter.keys()) - len(repeats.keys()) == len(device_ids)

    most_frequent_device_and_count = max(repeats.items(), key=lambda entry: entry[1])
    most_frequent_device_id = most_frequent_device_and_count[0]
    rows = df[df['device_id'] == most_frequent_device_id]
    print(rows['longitude'])
    print(rows['latitude'])

    
if __name__ == '__main__':
    main()

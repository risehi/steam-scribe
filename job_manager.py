# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DqObGbqodEen-eXOsKeTvMJ2GPqVwmAG
"""

import os
import time
from appid_retriever import fetch_appids
import json
import steam_fetcher


appids = fetch_appids()
appids_list = []

def write_appids():
    with open('appids.txt', 'w') as f:
        for id in appids:
            f.write(f"{id}\n")

def read_appids():
    with open('appids.txt', 'r') as f:
        for line in f:
            id_value = int(line.strip())
            _appids.append(id_value)

def manage_app_data(appids, filename="app_details.json"):
    """Manages fetching and saving app details."""

    existing_data = {}

    try:
        with open(filename, 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        pass

    fetched_appids = set(existing_data.keys())
    remaining_appids = [appid for appid in appids if str(appid) not in fetched_appids]
    total_appids = len(appids)

    print(f"Starting to fetch data for {len(remaining_appids)} app IDs...")

    for appid in remaining_appids:
        data = steam_fetcher.fetch_app_details(appid)

        #  print(f"Raw API response for app ID {appid}:", data)

        if data[str(appid)]['success']:
            if data[str(appid)]['data'].get('type') == 'game':
                if not data[str(appid)]['data'].get('release_date', {}).get('coming_soon'):
                    existing_data[appid] = data[str(appid)]['data']
                    print(f"Successfully fetched data for app ID: {appid}")
                else:
                    print(f"App ID {appid} is not yet released.")
            else:
                print(f"App ID {appid} is not a game.")
        else:
            print(f"Failed to fetch data for app ID: {appid}")

        # Save data incrementally after each fetch
        temp_filename = filename + ".temp"
        try:
            with open(temp_filename, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=4)
            os.replace(temp_filename, filename)
            print(f"Data saved incrementally for app ID: {appid}")
        except Exception as e:
            print(f"Error saving data to file: {e}")

        time.sleep(1.5)

        # Print progress
        progress_percentage = (len(existing_data) / total_appids) * 100
        print(f"Progress: {progress_percentage:.2f}% completed.")

    print("All data fetched and saved to app_details.json.")


def main():
    manage_app_data(appids)

if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DqObGbqodEen-eXOsKeTvMJ2GPqVwmAG
"""

import requests
import time

def fetch_app_details(appid, retry_delay=120):
    """Fetches app details for a single appid from Steam API."""

    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"

    while True:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            break
        except requests.exceptions.RequestException:
            time.sleep(retry_delay)

    data = response.json()
    return data
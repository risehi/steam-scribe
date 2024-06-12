# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DqObGbqodEen-eXOsKeTvMJ2GPqVwmAG
"""

from steam.webapi import WebAPI

api = WebAPI('replace with your API key')

def fetch_appids():
    all_apps = api.call('ISteamApps.GetAppList')
    app_list = all_apps['applist']['apps']
    appids = [app['appid'] for app in app_list]
    return appids
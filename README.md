#### Steam Scribe
This collection of Python scripts designed to gather Steam app data via the Steam WebAPI   
and `https://store.steampowered.com/api/appdetails?appids={appid}` endpoints.
- **appid_retriever.py** fetches all app IDs using official Steam WebAPI  
*Note: make sure to generate and use your own personal Steam API key*
- **steam_fetcher.py** fetches app details for a appID from Steam API at `https://store.steampowered.com/api/appdetails?appids={appid}`  
*Note: Replace the {appid} placeholder in the URL with an actual appid; for instance, 70 corresponds to the original Half-Life.*
- **job_manager.py** the main script, loads above mentioned scripts as modules, executes them to retrieve data, implements cooldowns, and ensures atomic saving of data into a file. It also handles loading previously saved file in case the execution was interrupted  
 *Note:These scripts are intended to be executed on a remote headless Linux instance.*
# XA Hub User Scraper

## What is XA Hub?

XA Hub is a known Roblox hacking group that provides various tools and scripts for Roblox users. As a result, most of the member in this group engage in hacking and exploiting Roblox games.

> **This group should be eradicated from Roblox as it promotes hacking and exploiting, which is against Roblox's Terms of Service.**

## Description

This is a Python script that scrapes user data from the XA Hub Roblox group.

- XA Hub Link: https://www.roblox.com/communities/35310933/XA-Hub#!/about

## Usage

``` shell
# Clone the repository
git clone https://github.com/redrubyyy611/xa-hub-user-scraper.git

# Change directory to the cloned repository
cd xa-hub-user-scraper

# Install the required dependencies
poetry env use python3
poetry env activate
poetry install

# Run the script
poetry run python main.py --scrape # to scrape the users
poetry run python main.py --extract # to retrieve only the ID's after scraping
```

The script will create a file called `xa_hub_users.txt` in the same directory as the script. This file will contain the scraped user data.

A JSON file called `xa_hub_users.json` will also be created, which contains the same data in JSON format.

After scraping, you can run the script with the `--extract` option to retrieve only the user IDs from the scraped data. This will create a file called `xa_hub_user_ids.txt` in the same directory as the script.

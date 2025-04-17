"""
This script fetches users from the XA Hub group on Roblox and saves them in both text and JSON formats.
It also provides functionality to extract user IDs from the scraped data.

Usage:
    scraper.py --scrape
    scraper.py --extract
    scraper.py --scrape --extract
"""

import argparse
import json
import os
import os.path
import time
import urllib.parse

import requests

from xa_hub_scraper_utils.constants import *
from xa_hub_scraper_utils.logger import (
    bold_text,
    error_log,
    info_log,
    success_log,
    warning_log,
)
from xa_hub_scraper_utils.roblox_api_data_structures import (
    RobloxGroupResponse,
    RobloxGroupUser,
)


def fetch_users(group_name: str, base_url: str, output_file: str) -> None:
    """
    Fetches users from the specified URL and saves them to a file.
    Args:
        group (str): The name of the group.
        base_url (str): The URL to fetch users from.
        output_file (str): The file to save the users to.
    """
    url = base_url
    users: list[RobloxGroupUser] = []

    i = 0
    while url:
        info_log(
            f"{group_name} | Fetching data from (users {i + 1}-{i + 100}): {bold_text(base_url)}"
        )
        response = requests.get(url)
        if response.status_code != 200:
            error_log(f"Failed to fetch data from {bold_text(url)}.")
            error_log(f"Status code: {bold_text(str(response.status_code))}")
            error_log(f"Response: {bold_text(response.text)}")
            exit(5)

        roblox_group_response: RobloxGroupResponse = RobloxGroupResponse.model_validate(
            response.json()
        )
        for roblox_group_user in roblox_group_response.data:
            users.append(roblox_group_user)

        if not roblox_group_response.nextPageCursor:
            break

        url = f"{base_url}&cursor={urllib.parse.quote(roblox_group_response.nextPageCursor)}"
        time.sleep(1)  # Prevent rate limiting
        i += 100

    if len(users) == 0:
        warning_log("No users found.")
        exit(0)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(str(user) for user in users))
    success_log(f"Saved {len(users)} {group_name} users to {output_file} as text.")

    # save in JSON format for easy model loading
    json_output_file = output_file.replace(".txt", ".json")
    with open(json_output_file, "w", encoding="utf-8") as file:
        json.dump(
            [user.model_dump() for user in users], file, indent=4, ensure_ascii=False
        )
    success_log(f"Saved {len(users)} {group_name} users to {json_output_file} as JSON.")


def ensure_json_users_file_exists(group_name: str, file_path: str) -> None:
    """
    Ensure the JSON file exists and is not empty.
    Args:
        group (str): The name of the group.
        file_path (str): The path to the JSON file.
    """
    if not os.path.exists(os.path.join(os.getcwd(), file_path)):
        error_log(
            f"{group_name} users JSON file does not exist: {bold_text(file_path)}"
        )
        exit(4)

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            json.load(file)
        except json.JSONDecodeError:
            error_log(f"Invalid JSON in file: {bold_text(file_path)}")
            exit(3)


def extract_user_ids(group_name: str, input_file: str, output_file: str) -> None:
    """
    Extracts user IDs from the specified JSON file and saves them to a text file.
    Args:
        group (str): The name of the group.
        input_file (str): The JSON file to extract user IDs from.
        output_file (str): The file to save the user IDs to.
    """
    if not input_file.endswith(".json"):
        error_log(
            f"Input file for ID extraction must be a JSON file: {bold_text(input_file)}"
        )
        exit(6)

    ensure_json_users_file_exists(group_name=group_name, file_path=input_file)

    with open(input_file, "r", encoding="utf-8") as file:
        users = json.load(file)
        valid_users: list[RobloxGroupUser] = []
        for user in users:
            try:
                valid_user = RobloxGroupUser.model_validate(user)
                valid_users.append(valid_user)
            except ValueError as e:
                error_log(f"Invalid user data: {bold_text(user)}")
                error_log(f"Error: {bold_text(e)}")
                exit(2)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join([str(user.userId) for user in valid_users]))
    success_log(f"Extracted {len(valid_users)} {group_name} user IDs to {output_file}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Roblox Hacking Group User Scraper")
    parser.add_argument(
        "-s",
        "--scrape",
        action="store_true",
        help="Scrape users from the the given Roblox Hacking group(s)",
    )
    parser.add_argument(
        "-e",
        "--extract",
        action="store_true",
        help="Extract user IDs from the scraped data",
    )
    parser.add_argument(
        "-g",
        "--groups",
        action="append",
        type=str,
        nargs="*",
        help="Specify the hacking group(s) to scrape users from.",
        required=True,
    )
    args = parser.parse_args()

    if not args.scrape and not args.extract:
        error_log("No arguments provided.")
        parser.print_help()
        exit(1)

    for group in args.groups[0]:

        requested_group = str(group).lower()

        if requested_group in RobloxHackingGroups.XA_HUB.value["aliases"]:
            group_name = RobloxHackingGroups.XA_HUB.value["name"]
            base_url = ROBLOX_GROUP_BASE_SEARCH_URL.format(
                XA_HUB_GROUP_ID, XA_HUB_MEMBER_ROLE_ID
            )
            users_txt_file = XA_HUB_USERS_FILE
            users_json_file = XA_HUB_USER_IDS_JSON_FILE
            user_ids_txt_file = XA_HUB_USER_IDS_TXT_FILE
        else:
            warning_log(f"Ignoring invalid group specified: {bold_text(group)}")
            continue

        if args.scrape:
            fetch_users(
                group_name=group_name, base_url=base_url, output_file=users_txt_file
            )

        if args.extract:
            extract_user_ids(
                group_name=group_name,
                input_file=users_json_file,
                output_file=user_ids_txt_file,
            )

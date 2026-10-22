#!/usr/bin/env python3
"""Retrieve a GitHub user's location using the GitHub API."""

import sys
import time

import requests


def user_location(url):
    """Print a GitHub user's location or the relevant API error."""
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print(data.get("location"))
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers["X-RateLimit-Reset"])
        current_time = int(time.time())
        minutes = max(0, (reset_time - current_time) // 60)
        print(f"Reset in {minutes} min")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_location(sys.argv[1])

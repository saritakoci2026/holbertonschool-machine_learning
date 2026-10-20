#!/usr/bin/env python3
"""Find Star Wars ships that can hold a given number of passengers."""

import requests


def availableShips(passengerCount):
    """Return names of ships that can carry passengerCount passengers."""
    ships = []
    url = 'https://swapi-api.hbtn.io/api/starships/'

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for ship in data['results']:
            passengers = ship.get('passengers', 'unknown')

            try:
                capacity = int(passengers.replace(',', ''))
            except (ValueError, AttributeError):
                continue

            if capacity >= passengerCount:
                ships.append(ship['name'])

        url = data['next']

    return ships

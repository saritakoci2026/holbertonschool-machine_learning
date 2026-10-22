#!/usr/bin/env python3
"""Retrieve home planets of all sentient species."""

import requests


def sentientPlanets():
    """Return a list of unique home planets of sentient species."""
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []
    seen = set()
    cache = {}

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for species in data["results"]:
            classification = species.get("classification") or ""
            designation = species.get("designation") or ""

            if (
                "sentient" not in classification.lower()
                and "sentient" not in designation.lower()
            ):
                continue

            homeworld = species.get("homeworld")

            if not homeworld:
                name = "unknown"
            else:
                if homeworld not in cache:
                    planet_response = requests.get(
                        homeworld, timeout=10
                    )
                    planet_response.raise_for_status()
                    cache[homeworld] = planet_response.json()["name"]

                name = cache[homeworld]

            if name not in seen:
                planets.append(name)
                seen.add(name)

        url = data["next"]

    return planets

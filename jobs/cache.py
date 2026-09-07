import hashlib
import json


def generate_cache_key(description: str) -> str:
    cache_key = hashlib.sha256(description.encode()).hexdigest()
    return cache_key


def load_cache():
    with open("cache/skills.json", "r") as file:
        cache_data = json.load(file)
        return cache_data


def save_cache(cache: dict):
    with open("cache/skills.json", "w") as file:
        json.dump(cache, file, indent=4)

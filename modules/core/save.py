import json
import os
from typing import Optional


def save_status(data: dict, file_path: str):
    with open(file_path, "w") as file:
        json.dump(data, file)

def load_status(file_path: str) -> Optional[dict]:
    try:
        with open(file_path) as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def wipe_status(file_path: str):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass  
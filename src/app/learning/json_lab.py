import json
from pathlib import Path

FOLDER_PATH = Path('src/app/learning')
FILE_NAME = Path('config.json')
ALL_PATH = Path(FOLDER_PATH) / FILE_NAME

config = {
    'project_name': 'Power_algorithm',
    'version': '0.0.1',
    'nodes': {
        'alpha-1': {'cores': 10, 'load': 0.75},
        'alpha-2': {'cores': 10, 'load': 0.5},
        'beta-1': {'cores': 5, 'load': 0.5},
        'beta-2': {'cores': 5, 'load': 0.25},
        'omega-3': {'cores': 30, 'load': 0.5}
    },
    'debug_mode': True,
}

# Writing JSON file
with open(ALL_PATH, 'w', encoding='utf-8') as file:
    json.dump(config, file, indent=4)

# Reading JSON file
try:
    with open(ALL_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError as err:
    print(f'Something went wrong. File not found. Error: {err}.')
else:
    print('Data has been read successfully.')
print(f'Starting project version: {data['version']}.')

for node in data['nodes'].keys():
    print(f'Server name: {node}')

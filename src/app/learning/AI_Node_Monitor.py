from pathlib import Path

ENCODING = 'utf-8'
FOLDER_PATH = Path('src/app/learning')
FILE_NAME = Path('server_logs.txt')
ALL_PATH = Path(FOLDER_PATH) / FILE_NAME

def calculate_power(node_dict):
    return node_dict['cores'] * (1 - node_dict['load'])

def calculate_efficiency(power):
    if power >= 5:
        status = 'Efficient'
    else:
        status = 'Overload'
    return status


nodes = [
    # Dumb error test.
    {
        'name': 'corrupted_epsilon',
        'cores': '@##$!@!#',
        'load': 0.75
    },
    {
        'name': 'alpha-1',
        'cores': 10,
        'load': 0.75
    },
    {
        'name': 'alpha-2',
        'cores': 10,
        'load': 0.5
    },
    {
        'name': 'beta-1',
        'cores': 5,
        'load': 0.75
    },
    {
        'name': 'beta-2',
        'cores': 5,
        'load': 0.75
    },
    {
        'name': 'omega-1',
        'cores': 30,
        'load': 0.5
    }
]

log_lines = list()

for node in nodes:
    try:
        power = calculate_power(node)
        status = calculate_efficiency(power)
    except (TypeError, KeyError) as err:
        log_lines.append(f"Server {node.get('name', 'Unknown')}. ERROR: {err}\n")
        print(f'Something went wrong. Error: {err}. In report may be trubls.')
    else:
        log_lines.append(f'Server {node['name']}: Availble power {power} - {status}\n')
    

with open(ALL_PATH, 'w', encoding=ENCODING) as file:
    file.writelines(log_lines)

print('Report successfully create.')
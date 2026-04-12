from pathlib import Path

FOLDER_PATH = Path('src/app/learning')
FILE_NAME = Path('server_logs.txt')
ALL_PATH = Path(FOLDER_PATH) / FILE_NAME

logs = ['System start', 'AI core initialized', 'Connection established']

with open(ALL_PATH, 'w', encoding='utf-8') as file:
    for item in logs:
        file.write(item + '\n')

content = None
with open(ALL_PATH, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

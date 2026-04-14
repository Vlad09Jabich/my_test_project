from pathlib import Path

FILE_PATH = Path('ghost_logs.txt')

try:
    special_error = 1 / 0
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError as err:
    print('Error: file not found')
    print(err)
except Exception as err:
    print(err)
finally:
    print('File system was checked.')
    

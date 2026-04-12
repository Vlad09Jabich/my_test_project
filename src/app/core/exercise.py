from pathlib import Path


FOLDER_PATH = '/home/vlad/Programming/Texts/'

fhand = None
data = None

while True:
    fname = input('Enter file name (with file extension): ')
    full_path = Path(FOLDER_PATH) / fname

    try:
        with open(full_path, "r", encoding="utf-8") as fhand:
            data = fhand.read()
    except FileNotFoundError:
        print('Error: File not found.')
    except Exception as error:
        print(f'Error: {error}')
    else:
        print('File:', fname, 'found successfuly.')
        break
    finally:
        print(f'Target path: {full_path} \n')

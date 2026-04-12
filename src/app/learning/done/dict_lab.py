profile = {
    'name': 'Vlad',
    'role': 'Student',
    'skills': ['Python', 'Linux', 'uv']
}

profile['role'] = 'Junior Developer'

profile['skills'].append('Dictionaries')

try:
    print(profile['expirience'])
except Exception as err:
    print(err)

print(profile.get('experience'))


print(f'My dictionary {profile}')
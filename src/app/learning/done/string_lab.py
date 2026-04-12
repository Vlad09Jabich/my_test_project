raw_data = " python - мощный язык "
clean_data = raw_data.strip().capitalize()
print(clean_data[0:6])

career_path = 'junior-middle-senior-head'
l = career_path.split('-')
print(l[-1])

print(f'Мой путь: {l[0]} -> {l[-1]}')
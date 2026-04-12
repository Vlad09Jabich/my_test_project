server_status = 'offline'
access_level = 1

if server_status == 'online':
    print('Сервер работает. Добро пожаловать.')
elif server_status == 'maintenance':
    if access_level > 8:
        print('Технический доступ разрешен.')
    else:
        print('Доступ запрещён. Обратитесь к Head of AI.')
else:
    print('Система отключена. Доступ невозможен.')
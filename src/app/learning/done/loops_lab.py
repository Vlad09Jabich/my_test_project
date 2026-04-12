servers = ["web-1", "db-1", "ai-node-1", "backup-1"]
# print(len(servers))
# print(servers[0])

for server in servers:
    print(f'Проверка системы: {server}')
    if server == 'ai-node-1':
        print('Найдено ядро ИИ!')
        break

for x in range(5, 0, -1):
    print(f'Запуск через... {x}')

battery = 100

while battery > 0:
    print(f'Заряд: {battery}')
    battery -= 20


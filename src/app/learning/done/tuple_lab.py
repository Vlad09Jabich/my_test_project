server_ip = ('192.168.1.1', 8080)
# print(type(server_ip))

# try:
#     server_ip[0] = '127.0.0.1'
# except TypeError as err:
#     print(err)

# all_ips = list(server_ip)
all_ips = [server_ip]
# print(f'Lists length = {len(all_ips)}, and this list: {all_ips}')
print(all_ips)
print(type(all_ips))
print(all_ips[0])
print(type(all_ips[0]))
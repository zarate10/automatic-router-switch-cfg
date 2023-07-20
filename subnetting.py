def subnet_calc(ip, subnet_mask, num_hosts):
    ip_binary = ''.join(format(int(octeto), '08b') for octeto in ip.split('.'))

    valid_hosts = [254, 126, 62, 30, 14, 6, 2]
    if num_hosts in valid_hosts:
        num_hosts = num_hosts - 1

    subnet_bits = 32 - (num_hosts + 2).bit_length()
    subnet_mask_binary = '1' * subnet_bits + '0' * (32 - subnet_bits)
    subnet_mask_decimal = '.'.join(str(int(subnet_mask_binary[i:i+8], 2)) for i in range(0, 32, 8))

    if subnet_bits < 0:
        raise ValueError('La cantidad de hosts especificada no es válida para ninguna subred.')

    network_address_binary = ip_binary[:subnet_bits] + '0' * (32 - subnet_bits)
    network_address = '.'.join(str(int(network_address_binary[i:i+8], 2)) for i in range(0, 32, 8))

    broadcast_address_binary = ip_binary[:subnet_bits] + '1' * (32 - subnet_bits)
    broadcast_address = '.'.join(str(int(broadcast_address_binary[i:i+8], 2)) for i in range(0, 32, 8))

    first_host_binary = network_address_binary[:-1] + '1'
    first_host = '.'.join(str(int(first_host_binary[i:i+8], 2)) for i in range(0, 32, 8))

    last_host_binary = broadcast_address_binary[:-1] + '0'
    last_host = '.'.join(str(int(last_host_binary[i:i+8], 2)) for i in range(0, 32, 8))

    return network_address, first_host, last_host, broadcast_address, subnet_mask_decimal

def mostrar_subnet(network_address, first_host, last_host, broadcast_address, subnet_mask_decimal): 
    print('{:<17} | {:<15} | {:<15} | {:<15} | {:<15}'.format(network_address, first_host, last_host, broadcast_address, subnet_mask_decimal))

ipaddress = input("IP: ")
subredes = []

if (ipaddress): 
    while True:
        
        cantidad = int(input("Hosts: "))

        if (cantidad == -1): 
            break 

        if (not len(subredes)): 
            subredes.append(subnet_calc(ipaddress, '255.255.255.0', cantidad))
        else: 
            broadcast_ultima_subred = subredes[(len(subredes) - 1)][3]
            new_subred = ".".join([str(int(n) + 1) if i == 3 else n for i, n in enumerate(broadcast_ultima_subred.split("."))])
            subredes.append(subnet_calc(new_subred, '255.255.255.0', cantidad))

    print('{:<17} | {:<15} | {:<15} | {:<15} | {:<15}'.format("Red", "Primera", "Última", "Broadcast", "Submask"))

    for subred in subredes: 
        mostrar_subnet(subred[0], subred[1], subred[2], subred[3], subred[4])
else: 
    print("Sin IP")
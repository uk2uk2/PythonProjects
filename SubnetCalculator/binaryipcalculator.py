

def to_binary(octet):
    binary_places = [128, 64, 32, 16, 8, 4, 2, 1]
    binary_representation = ''

    for value in binary_places:
        if octet >= value:
            octet -= value
            binary_representation += '1'
        else:
            binary_representation += '0'

    return binary_representation


def get_binary_representation(address):
    octets = address.split('.')
    return '.'.join(to_binary(int(octet)) for octet in octets)


# Prompt the user for an IP address and a subnet mask
ip_address = input("Input your IP address: ")
subnet_mask = input("Input your subnet mask: ")

# Convert the IP address and subnet mask to binary
binary_ip = get_binary_representation(ip_address)
binary_subnet_mask = get_binary_representation(subnet_mask)

# Output the results
print(f"The binary representation of IP address {ip_address} is {binary_ip}")
print(f"The binary representation of subnet mask {subnet_mask} is {binary_subnet_mask}")
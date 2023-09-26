def to_binary(octet):
    """
    Convert an IP address octet to binary.

    """
    
    binary_octet = ''
    values = [128,64,32,16,8,4,2,1]
    for value in values:
        if octet >= value:
            binary_octet += '1'
            octet -= value
        else:
            binary_octet += '0'
    return binary_octet


def ip_to_int32(ip):
  # your code here
    from ipaddress import IPv4Address
    addr = IPv4Address(ip)
    return int(addr)
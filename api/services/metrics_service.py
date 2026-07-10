registered_hosts = {}
next_host_id = 1


def register_host(hostname, operating_system, ip_address):

    global next_host_id

    key = (hostname, operating_system)

    if key in registered_hosts:
        return registered_hosts[key]

    host_id = next_host_id

    registered_hosts[key] = host_id

    next_host_id += 1

    print()

    print("==========================")
    print("Host Registered")
    print("==========================")
    print(f"Host ID : {host_id}")
    print(f"Hostname: {hostname}")
    print(f"OS      : {operating_system}")
    print(f"IP      : {ip_address}")

    return host_id
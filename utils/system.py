import os
import re
import subprocess

def execute_ping(target_ip):
    # Validate target_ip against a strict allow-list (IPv4 addresses only)
    if not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', target_ip):
        raise ValueError("Invalid target IP address")

    # Each octet must be between 0 and 255
    if not all(0 <= int(octet) <= 255 for octet in target_ip.split('.')):
        raise ValueError("Invalid target IP address: octet out of range")

    # Use subprocess with a list of arguments and no shell — safe from command injection
    return subprocess.run(
        ["ping", "-c", "1", target_ip],
        capture_output=True,
        text=True,
        shell=False
    ).stdout


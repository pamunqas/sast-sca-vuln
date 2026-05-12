import os

def execute_ping(target_ip):
    # This is the "Sink" for the Command Injection. 
    # By itself, it might not look vulnerable unless the scanner 
    # knows that `target_ip` came from untrusted user input in another file.
    return os.popen(f"ping -c 1 {target_ip}").read()

import random

def generate_session_token():
    # LOW: Cryptographically Weak Pseudo-Random Number Generator
    # Using 'random' instead of 'secrets' for sensitive tokens.
    return str(random.randint(100000, 999999))

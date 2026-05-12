import hashlib
from flask import Blueprint, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/hash_password')
def hash_password():
    # MEDIUM: Use of Weak/Broken Cryptographic Algorithm
    # The scanner should find this isolated in the routing logic.
    password = request.args.get('password', 'default_password')
    hashed = hashlib.md5(password.encode()).hexdigest()
    return f"Hashed password: {hashed}"

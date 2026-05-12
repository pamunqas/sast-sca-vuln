from flask import Blueprint, request
from utils.system import execute_ping

network_bp = Blueprint('network', __name__)

@network_bp.route('/ping')
def ping():
    # CRITICAL: OS Command Injection (Cross-File)
    # This tests "Taint Analysis". The scanner must track the untrusted 
    # input ('target') from this file, down into the execute_ping function 
    # located in utils/system.py.
    target = request.args.get('target', '127.0.0.1')
    result = execute_ping(target)
    return f"<pre>{result}</pre>"

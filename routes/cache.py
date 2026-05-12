import hashlib
from flask import Blueprint, request

cache_bp = Blueprint('cache', __name__)

@cache_bp.route('/cache_image')
def cache_image():
    # FALSE POSITIVE: Safe use of MD5
    # The tool should ideally recognize this isn't hashing a password, 
    # but it will likely flag it anyway. This tests your platform's 
    # triage and suppression capabilities.
    filename = request.args.get('file', 'banner.png')
    cache_key = hashlib.md5(filename.encode()).hexdigest()
    return f"Cache key for {filename}: {cache_key}"

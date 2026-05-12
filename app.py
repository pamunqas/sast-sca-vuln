from flask import Flask
import config
from routes.network import network_bp
from routes.auth import auth_bp
from routes.cache import cache_bp
from utils.generators import generate_session_token

app = Flask(__name__)

# Registering separated route files
app.register_blueprint(network_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(cache_bp)

@app.route('/token')
def get_token():
    # Calling an external utility function
    token = generate_session_token()
    return f"Your new session token is: {token}"

if __name__ == '__main__':
    app.run(debug=config.DEBUG_MODE, host='0.0.0.0')

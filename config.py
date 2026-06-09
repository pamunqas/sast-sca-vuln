# HIGH: Hardcoded Secrets / Credentials
# WARNING: Hardcoded credentials removed for security.
# Set these via environment variables before running the application.
import os

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY", "")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY", "")

# LOW: Debug mode enabled
DEBUG_MODE = True


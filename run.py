"""App entry point."""
from app import app as application

application.run(host='0.0.0.0', debug=True)

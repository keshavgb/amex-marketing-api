# App Setup
# This is like "opening the restaurant for business"
# It connects all the pieces together

from flask import Flask

def create_app():
    """Create and configure the API."""
    app = Flask(__name__)

    # Register the routes (connect the menu to the waiter)
    from src.routes import campaigns_bp
    app.register_blueprint(campaigns_bp)

    return app
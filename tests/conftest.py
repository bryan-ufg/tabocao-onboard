import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch
import pytest

mock_user_payload = {
    "id": "user_123",
    "email": "teste@exemplo.com",
    "public_metadata": {"role": "admin"}
}

def mock_verify_session(fn):
    def wrapper(*args, **kwargs):
        from flask import g
        g.clerk_user = mock_user_payload
        return fn(*args, **kwargs)
    return wrapper

@pytest.fixture
def app():
    with patch("services.verify_session", mock_verify_session):
        from app import create_app
        from extensions import db

        config_override = {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }

        app = create_app(config_override=config_override)

        with app.app_context():
            db.create_all()
            yield app
            db.session.remove()
            db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

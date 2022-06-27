from flaskr import app
from flaskr.cfg.config import TestConfig
import pytest


@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    flask_app.config.from_object(TestConfig)
    print(flask_app.config)
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = Path(__file__).parent.parent / "app.py"


def test_landing_page_renders_without_error():
    """No image uploaded yet: the app must never touch the model file on this path."""
    at = AppTest.from_file(str(APP_PATH))
    at.run()
    assert not at.exception

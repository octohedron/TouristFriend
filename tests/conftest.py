import pytest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from api import app as _app


@pytest.fixture
def app():
    return _app

# -*- coding: utf-8 -*-

import pytest
from todolist import create_app
from todolist.services import todo as todo_service


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture(scope='function', autouse=True)
def reset_todo_list():
    """Reset `todo_service._TODOS` state."""
    todo_service._TODOS = {}

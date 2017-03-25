# -*- coding: utf-8 -*-

from uuid import uuid4


_TODOS = {}


def list():
    return [{
        'id': key,
        'description': value
    } for key, value in _TODOS.items()]


def new(description):
    todo_id = str(uuid4())
    _TODOS[todo_id] = description
    return {
        'id': todo_id,
        'description': description
    }


def delete(todo_id):
    del _TODOS[todo_id]

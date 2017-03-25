# -*- coding: utf-8 -*-

from todolist.services import todo as todo_service


def test_todo_new():
    todo = todo_service.new('Task 1')

    assert 'id' in todo
    assert todo['description'] == 'Task 1'


def test_todo_list():
    todo_service.new('Task 1')
    todo_service.new('Task 2')

    all_todos = todo_service.list()
    assert len(all_todos) == 2


def test_todo_delete():
    todo = todo_service.new('Task 1')
    todo_service.delete(todo['id'])
    assert todo_service.list() == []

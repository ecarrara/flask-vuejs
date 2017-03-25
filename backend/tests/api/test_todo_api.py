# -*- coding: utf-8 -*-

import json
from todolist.services import todo as todo_service


def test_new_todo(client):
    response = client.post('/v0/todo', headers={
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'description': 'Task 1'
    }))

    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['description'] == 'Task 1'


def test_delete_todo(client):
    todo = todo_service.new('Task 1')

    response = client.delete('/v0/todo/{}'.format(todo['id']), headers={
        'Content-Type': 'application/json'
    })

    assert response.status_code == 200


def test_list_todo(client):
    todo_service.new('Task 1')
    todo_service.new('Task 2')

    response = client.get('/v0/todo', headers={
        'Content-Type': 'application/json'
    })

    assert response.status_code == 200
    assert len(response.json['objects']) == 2

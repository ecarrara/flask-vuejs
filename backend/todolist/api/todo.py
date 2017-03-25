# -*- coding: utf-8 -*-

from flask import request, jsonify
from todolist.api import api
from todolist.services import todo as todo_service


@api.route('/todo', methods=['GET'])
def list_todos():
    return jsonify({
        'objects': todo_service.list()
    })


@api.route('/todo', methods=['POST'])
def new_todo():
    todo = todo_service.new(request.json['description'])
    return jsonify(todo), 201


@api.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    print(todo_service._TODOS)
    print(todo_id)
    todo_service.delete(todo_id)
    return jsonify(dict(deleted=True)), 200

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from todolist import create_app


app = create_app()
manager = Manager(app)


if __name__ == '__main__':
    manager.run()

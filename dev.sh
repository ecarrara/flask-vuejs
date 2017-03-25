#!/bin/bash

CI_DIR=${CI_DIR:-./ci}

PYTHON_PACKAGE_NAME=todolist
VENV_NAME=todolist

PYTHON_VERSION=python2
NODE_VERSION=v7.4.0

command=$1

. $(which virtualenvwrapper_lazy.sh)

check_py_venv() {
    if [[ "$VIRTUAL_ENV" != "$WORKON_HOME/$VENV_NAME" ]]; then
        echo -e "Please activate virtualenv before!"
        echo -e "Run:"
        echo -e "  $ workon $VENV_NAME"
        exit 1
    fi
}

check_js_env() {
    if [[ "$NVM_DIR" == "" ]]; then
        curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
    fi

    NODE_PATH=$(which node)
    if [[ "$NODE_PATH" != "$NVM_DIR/versions/node/v7.4.0/bin/node" ]]; then
        echo -e "Please install node and nvm first"
        echo -e "Run:"
        echo -e "  $ $0 jsenv"
    fi
}

case "$command" in
  "pyenv")
        echo "Entrando no ambiente Python $VENV_NAME"
        if ! [[ -e "$WORKON_HOME/$VENV_NAME/bin/activate" ]]; then
            echo "Criando ambiente $VENV_NAME..."
            mkvirtualenv --python $(which $PYTHON_VERSION) $VENV_NAME
        fi

        workon $VENV_NAME

        pip install -r backend/requirements.txt

        echo -e ""
        echo -e "Run:"
        echo -e "  $ workon $VENV_NAME"
  ;;
  "pytest")
        check_py_venv

        CI_DIR=$(realpath $CI_DIR)
        mkdir -p $CI_DIR

        cd backend
        ENVIRONMENT=testing python -m pytest tests \
                --cov $PYTHON_PACKAGE_NAME \
                --cov-report html:$CI_DIR/python/coverage_html \
                --cov-report xml:$CI_DIR/python/coverage.xml \
                --cov-report annotate:$CI_DIR/python/coverage_annotate \
                --cov-report term-missing \
                --junitxml $CI_DIR/python/tests.xml
        cd - > /dev/null
  ;;
  "pydev")
        check_py_venv

        cd backend
        ENVIRONMENT=development ./manage.py runserver --threaded
        cd - > /dev/null
  ;;
  "jsenv")
        cd frontend

        if [[ -z ${NVM_DIR+x} ]]; then
            echo -e "Installing NVM..."
            curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash

            source $HOME/.bashrc
        fi

        . $NVM_DIR/nvm.sh

        nvm install $NODE_VERSION
        nvm use $NODE_VERSION

        npm install

        echo -e ""
        echo -e "Run:"
        echo -e "  $ nvm use v7.4.0"
        cd - > /dev/null
  ;;
  "jstest")
        check_js_env

        cd frontend
        npm run test
        cd - > /dev/null
  ;;
  "jsdev")
        check_js_env

        cd frontend
        npm run dev
        cd - > /dev/null
  ;;
  *)
      echo "$0 <subcomando>"
      echo -e "  pyenv \t Prepara o ambiente de desenvolvimento Python"
      echo -e "  pytest \t Executa os testes do backend"
      echo -e "  pydev \t Executa servidor de desenvolvimento do backend"
      echo -e "  jsenv \t Prepara o ambiente de desenvolvimento JS"
      echo -e "  jstest \t Executa os testes do frontend"
      echo -e "  jsdev \t Executa servidor de desenvolvimento do frontend"
   ;;
esac

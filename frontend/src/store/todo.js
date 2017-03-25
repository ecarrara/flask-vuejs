import { TODO_LIST, TODO_NEW, TODO_DELETE } from './actions'
import todoService from '../services/todo'

export const types = {
  TODO_LIST_REQUEST: 'TODO_LIST_REQUEST',
  TODO_LIST_SUCCESSFUL: 'TODO_LIST_SUCCESSFUL',
  TODO_LIST_FAILURE: 'TODO_LIST_FAILURE',
  TODO_LIST_ADD: 'TODO_LIST_ADD',
  TODO_LIST_DELETE: 'TODO_LIST_DELETE'
}

export const state = {
  todos: [],
  isLoading: false,
  errorMessage: ''
}

export const mutations = {
  [types.TODO_LIST_REQUEST]: (state) => {
    state.isLoading = true
    state.error = null
  },
  [types.TODO_LIST_SUCCESSFUL]: (state, todos) => {
    state.isLoading = false
    state.error = null
    state.todos = todos
  },
  [types.TODO_LIST_FAILURE]: (state, error) => {
    state.isLoading = false
    state.error = error
    state.todos = []
  },
  [types.TODO_LIST_ADD]: (state, todo) => {
    state.todos.push(todo)
  },
  [types.TODO_LIST_DELETE]: (state, todoId) => {
    state.todos = state.todos.filter((todo) => todo.id !== todoId)
  }
}

export const actions = {
  [TODO_LIST] ({state, commit}) {
    commit(types.TODO_LIST_REQUEST)

    todoService.all().then(response => {
      commit(types.TODO_LIST_SUCCESSFUL, response)
    }).catch(error => {
      if (error) {
        console.warn(error)
        commit(types.TODO_LIST_FAILURE, error)
      }
    })
  },
  [TODO_NEW] ({state, commit}, description) {
    todoService.new(description).then((response) => {
      commit(types.TODO_LIST_ADD, response)
    })
  },
  [TODO_DELETE] ({state, commit}, todoId) {
    todoService.delete(todoId).then(() => {
      commit(types.TODO_LIST_DELETE, todoId)
    })
  }
}

export default {
  state,
  mutations,
  actions
}

const _MOCKED_TODOS = [{
  id: 'cb869698-76d1-4f77-9340-609da63fad0d',
  description: 'Task 1'
}, {
  id: 'a712db82-4d67-46c5-9676-1267ad4c14e3',
  description: 'Task 2'
}]

let _idCounter = 0

export default {
  all: () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(_MOCKED_TODOS)
      }, 100)
    })
  },
  new: (description) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve({
          id: _idCounter++,
          description: description
        })
      }, 100)
    })
  },
  delete: (todoId) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve()
      }, 100)
    })
  }
}

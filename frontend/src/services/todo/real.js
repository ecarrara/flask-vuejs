import api from '../../../api'

export default {
  all: () => {
    return api.get(`/todo`).then((response) => {
      return response.data.objects
    })
  },
  new: (description) => {
    return api.post(`/todo`, {
      description: description
    }).then((response) => {
      return response.data.objects
    })
  }
}

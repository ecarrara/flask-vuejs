<template>
  <div id="app">
    <h1>todos</h1>
    <TodoNew @create="createTodo" />
    <Todo v-for="todo in todos" :todo="todo" :key="todo.id" @delete="deleteTodo(todo)" />
  </div>
</template>

<script>
import { TODO_LIST, TODO_NEW, TODO_DELETE } from './store/actions'
import TodoNew from './components/TodoNew'
import Todo from './components/Todo'

export default {
  name: 'app',
  components: {
    TodoNew,
    Todo
  },
  created: function () {
    this.$store.dispatch(TODO_LIST)
  },
  methods: {
    createTodo: function (description) {
      this.$store.dispatch(TODO_NEW, description)
    },
    deleteTodo: function (todo) {
      this.$store.dispatch(TODO_DELETE, todo.id)
    }
  },
  computed: {
    todos () {
      return this.$store.state.todo.todos
    }
  }
}
</script>

<style lang="scss">
@import "styles/base";
</style>

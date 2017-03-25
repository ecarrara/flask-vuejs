<template>
  <div class="new-todo">
    <input placeholder="What needs to be done?" v-model="description" @keyup.enter="createTodo">
  </div>
</template>

<script>
export default {
  data: () => {
    return {
      description: ''
    }
  },
  methods: {
    createTodo: function () {
      this.$emit('create', this.description)
    }
  }
}
</script>

<style lang="scss" scoped>
.new-todo {
  margin-bottom: 15px;

  input {
    width: 100%;
    padding: 10px;
    font-size: 14px;
  }
}
</style>

<template>
  <div class="todo">
    <button class="delete-button" type="button" @click="deleteTodo">×</button>
    {{ todo.description }}
  </div>
</template>

<script>
export default {
  props: ['todo'],
  methods: {
    deleteTodo: function () {
      this.$emit('delete')
    }
  }
}
</script>

<style lang="scss" scoped>
.todo {
  border-bottom: 1px solid #ddd;
  padding: 10px 0;

  .delete-button {
    float: right;
    border: none;
    background: none;
    color: #a32;
    font-size: 16px;
    padding: 0 10px;
    cursor: pointer;
  }
}
</style>

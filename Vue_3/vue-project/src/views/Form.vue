<script>
import NewButton from '../components/UI/NewButton.vue'

export default {
    components: {
        NewButton
    }
}
</script>

<template>
    <new-button
        background="red" 
        color="white" 
        :disable="true"
    />
  </template>

<style scoped>
</style>
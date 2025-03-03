<template>
    <button 
        :style="{ background: background, color: color }" 
        :disabled="disable"
    >
        Button
    </button>
</template>

<script>
export default {
    props: {
        background: {
            type: String
        },
        color: {
            type: String
        },
        disable: {
            type: Boolean
        }
    }
}
</script>

<style scoped>

</style>
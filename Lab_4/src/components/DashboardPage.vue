<template>
  <div class="dashboard-page">
    <h1 class="app-name">exQuiz me?!</h1>
    <bubbles-component/>
  </div>
</template>

<script>
import BubblesComponent from "@/components/BubblesComponent.vue";

export default {
  name: 'DashboardPage',
  components: {BubblesComponent}
}
</script>

<style scoped lang="scss">
.dashboard-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #6441A5; /* fallback for old browsers */
  background: -webkit-linear-gradient(to bottom, #2a0845, #6441A5); /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to bottom, #2a0845, #6441A5); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  justify-content: center;
  bottom: 0;
  left: 0;
  position: fixed;
  right: 0;
  top: 0;

  .app-name {
    color: white;
    font-size: 3rem;
  }
}
</style>
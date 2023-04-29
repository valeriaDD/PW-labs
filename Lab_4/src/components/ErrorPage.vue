<template>
  <div class="container gradient--purple">
    <div class="container__status"> {{ statusCode }}</div>
    <div class="container__title"> {{ text }}</div>
    <bubbles-component/>
  </div>
</template>

<script>
import BubblesComponent from "@/components/animated/BubblesComponent.vue";

export default {
  name: "ErrorPage",
  props: {
    statusCode: {
      type: Number,
      default: 404,
    },
    text: {
      type: String,
      default: "Ups, page not found :("
    }
  },
  components: {BubblesComponent}
}
</script>

<style scoped lang="scss">
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  color: white;
  bottom: 0;
  left: 0;
  position: fixed;
  right: 0;
  top: 0;
  background: #593656;
  background: -webkit-linear-gradient(to bottom, #2e253a, #482b47);
  background: linear-gradient(to bottom, #2e253a, #482b47);

  &__status {
    font-size: 6rem;
    font-weight: bolder;
  }

  &__title {
    font-size: 1.8rem;
  }
}
</style>
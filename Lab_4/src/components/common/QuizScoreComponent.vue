<template>
  <div class="score-container">
    <div class="score-container__header"> Your score is</div>
    <div class="score-container__score"> {{score}} </div>
    <img src="@/assets/trophy_img.png" :height="imgHeight">
  </div>
</template>

<script>
export default {
  name: "QuizScoreComponent",
    props: {
      score: {
          type: String,
          default: "0/0"
      },
      imgHeight: {
          type: Number,
          default: 200,
      }
    }
}
</script>

<style scoped lang="scss">
.score-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
<template>
  <div class="score-container">
    <div class="score-container__header"> Your score is</div>
    <div class="score-container__score"> {{score}} </div>
    <img src="@/assets/trophy_img.png" height="200">
  </div>
</template>

<script>
export default {
  name: "QuizScoreComponent",
    props: {
      score: {
          type: String,
          default: "0/0"
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
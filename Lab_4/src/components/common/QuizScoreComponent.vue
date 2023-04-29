<template>
  <div class="score-container">
    <div class="score-container__header"> Your score is</div>
    <div class="score-container__score"> 12/20</div>
    <img src="@/assets/trophy_img.png" height="200">
  </div>
</template>

<script>
export default {
  name: "QuizScoreComponent"
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
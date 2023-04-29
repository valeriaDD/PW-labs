<template>
<div class="card">
  <div class="card__title"> Get to know the most powerful things in the whole word</div>
  <div class="card__footer">
    <div class="question-count"> 25 quiestions </div>
    <i class="icon el-icon-right" />
  </div>
</div>
</template>

<script>

export default {
  name: "QuizCardComponent",
}
</script>


<style scoped lang="scss">
.card {
  padding: 2rem;
  color: black;
  background: white;
  border-radius: 0.4rem;
  box-shadow: rgba(0, 0, 0, 0.25) 0 25px 50px -12px;
  opacity: 0.8;
  transition: all 0.3s ease-in-out;

  &__footer {
    margin-top: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .icon {
      font-size: 1.5rem;
      visibility: hidden;
      opacity: 0;
      translate: -1rem;
      transition: all 0.3s ease-in-out;
    }
  }

  &:hover {
    cursor: pointer;
    opacity: 1;
    box-shadow: rgba(0, 0, 0, 0.25) 0 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;

    .card__footer {
      .icon {
        translate: 0;
        opacity: 1;
        visibility: visible;
      }
    }
  }

  &__title {
    font-size: 1.2rem;
    font-weight: bold;
  }
}
</style>
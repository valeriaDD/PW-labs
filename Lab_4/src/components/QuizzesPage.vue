<template>
    <div class="container">
        <div class="cover"/>
        <div class="title"> Game is on, what's your pick?</div>
        <el-col class="quizzes-container" :lg="16" :sm="18" :xs="23">
            <quiz-card-component
                    class="quiz-item" v-for="(quiz, index) in quizzes"
                    :key="index"
                    :quiz="quiz"
                    :style="{ backgroundColor: pastelColors[index % pastelColors.length] }"
            />
        </el-col>
        <router-view/>
    </div>
</template>

<script>
import QuizCardComponent from "@/components/common/QuizCardComponent.vue";

export default {
    name: "QuizzesPage",
    components: {QuizCardComponent},
    data() {
        return {
            pastelColors: ['#ffd1dc', '#f9d5e5', '#e8d5f1', '#d1d1ff', '#c0e8d5', '#ffdeb8', '#b8ffe1'],
        };
    },
    computed: {
        quizzes() {
            return this.$store.getters['quizzes/getQuizzes'];
        }
    },
    beforeCreate() {
        this.$store.dispatch('quizzes/loadQuizzes')
    }
}
</script>

<style scoped lang="scss">
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  min-height: 100vh;
  color: white;
  background: #2e253a;

  .header {
    align-self: flex-start;
  }

  .title {
    padding: 1rem 5rem 1rem;
    font-size: 6rem;
    opacity: 1;
  }

  .quizzes-container {
    padding: 2rem 2rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
  }

  .cover {
    width: 100%;
    z-index: 100;
    height: 40vh;
    background-image: url('@/assets/forest.jpg');
    background-repeat: no-repeat;
    background-position: 60% 60%;
    background-size: cover;
  }
}
</style>
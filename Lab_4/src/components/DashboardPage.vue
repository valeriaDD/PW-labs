<template>
  <div class="dashboard-page">
    <h1 class="app-name">exQuiz me?!</h1>
    <el-col class="register-component" :lg="6" :sm="8" :xs="20">
      <el-form class="register-component__form">
        <el-form-item >
          <el-input v-model="name" placeholder="Name"/>
        </el-form-item>
        <el-form-item>
          <el-input v-model="surname" placeholder="Surname"/>
        </el-form-item>
      </el-form>
      <el-button class="register-component__action" @click="submit" round> Play </el-button>
    </el-col>
    <falling-stars-component/>
  </div>
</template>

<script>
import FallingStarsComponent from "@/components/animated/FallingStarsComponent.vue";

export default {
  name: 'DashboardPage',
  components: {FallingStarsComponent},
  data() {
    return {
      name: "",
      surname: "",
    };
  },
  methods: {
    submit() {
      console.log(this.name + " " + this.surname)
    }
  }
}
</script>

<style scoped lang="scss">
.dashboard-page {
  background-image: url('@/assets/forest.jpg');
  background-repeat: no-repeat;
  background-position: 50% 55%;
  background-size: cover;
  display: flex;
  flex-direction: column;
  align-items: center;
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

  .register-component {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;

    &__form {
      width: 100%;
    }

    &__action {
      width: fit-content;
      min-width: 7rem;
    }
  }
}
</style>
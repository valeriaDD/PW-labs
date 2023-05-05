<template>
    <div class="question">
        <div class="question__title" :class="{correct: isInReview && correct, incorrect: isInReview && !correct}">
            <span> {{ number ?? '' }}. </span> <span> {{ question.question }}</span>
        </div>
        <el-form-item>
            <el-radio-group class="answers" v-model="value" @change="addAnswer">
                <el-radio :label="answer" class="radio-button" v-for="(answer, index) in question.answers" :key="index"/>
            </el-radio-group>
        </el-form-item>
    </div>
</template>

<script>
export default {
    name: "QuestionComponent",
    props: {
        question: {
            type: Object,
            required: true,
        },
        number: {
            type: Number,
            default: null,
        },
        correct: {
            type: Boolean,
            default: undefined,
        }
    },
    data() {
        return {
            value: '',
        };
    },
    computed: {
        isInReview() {
            return typeof this.correct !== 'undefined';
        }
    },
    methods: {
        addAnswer(value) {
            this.$store.dispatch("quiz/addAnswer", {
                question: this.question?.id,
                answer: value,
            })
        }
    }
}
</script>

<style scoped lang="scss">
.correct {
  color: green !important;
}

.incorrect {
  color: red !important;
}

.question {
  .question__title {
    font-weight: bolder;
    font-size: 1rem;
  }

  .answers {
    margin-top: 1rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
  }
}
</style>
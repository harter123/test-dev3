<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <HelloWorld msg="Welcome to Your Vue.js App" myProps="hahahah"/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import HelloWorld from '../components/HelloWorld.vue'

    export default {
        name: 'home',
        components: {
            HelloWorld
        },
        props:{
            arg: String,
        },
        date(){
            return {
                message: 'message'
            }
        },
        methods: {

        },
        created(){

        },

    }
</script>

<style scoped>
    .mycss {

    }
</style>
<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import {getLoginUserInfo} from "./request/user";

    export default {
        name: 'App',
        components: {},
        date() {
            return {}
        },
        methods: {},
        created() {
            getLoginUserInfo().then(data => {
                let success = data.data.success;
                if(!success){ //登录失败的情况下，跳转到登录页面
                    this.$router.push('/login')
                }
            })
        },
    }
</script>


<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        height: 100%;
        overflow: auto;
    }

    html, body {
        height: 100%;
    }

    #nav {
        padding: 30px;
    }

    #nav a {
        font-weight: bold;
        color: #2c3e50;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    }

    body {
        display: block;
        margin: 0;
    }
</style>

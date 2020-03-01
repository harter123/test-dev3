import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/about',
        name: 'about',
        // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
         component: About,
        children:[
            {
                path: 'test',
                name: 'home',
                component: () => import(/* webpackChunkName: "about" */ '../components/test.vue'),
            }
        ]
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/login.vue'),
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router

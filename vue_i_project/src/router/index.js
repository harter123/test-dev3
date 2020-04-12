import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
        props: {
            menu: 'service'
        },
        children: [
            {
                path: 'service',
                name: 'service',
                component: () => import('../views/service/index'),
            },
            {
                path: '',
                name: 'service',
                component: () => import('../views/service/index'),
            },
        ]
    },
    {
        path: '/',
        name: 'home',
        component: Home,
        props: {
            menu: 'task'
        },
        children: [
            {
                path: 'task',
                name: 'task',
                component: () => import('../views/task/index'),
            }
        ]
    },
    {
        path: '/',
        name: 'home',
        component: Home,
        props: {
            menu: 'interface'
        },
        children: [
            {
                path: 'interface',
                name: 'interface',
                component: () => import('../views/interface/index'),
            }
        ]
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/login'),
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router

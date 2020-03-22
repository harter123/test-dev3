import {deleteRequest, getRequest, postRequest} from "./common";

export const login = function (username, password) { //登录
    return postRequest('user/login/', {
        username: username,
        password: password,
    })
};

export const register = function (username, password) { //登录
    return postRequest('user/register/', {
        username: username,
        password: password,
    })
};

export const logout = function () {//退出登录
    return deleteRequest('user/logout/')
};

export const getLoginUserInfo = function () { //获取已经登录的用户信息
    return getRequest('user/info/')
};
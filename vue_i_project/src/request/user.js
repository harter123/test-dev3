import {getRequest, postRequest} from "./common";

export const login = function (username, password) { //登录
    return postRequest('test/')
};

export const register = function (username, password) { //登录
    return postRequest('')
};

export const logout = function () {//退出登录
    return getRequest('')
};

export const getLoginUserInfo = function () { //获取已经登录的用户信息
    return getRequest('')
};
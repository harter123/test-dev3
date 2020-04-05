import {deleteRequest, getRequest, postRequest, putRequest} from "./common";

export const getAllServices = function () { //获取所有的服务
    return getRequest('api/services/')
};

export const getSingleService = function (serviceId) { //获取单个的服务
    return getRequest(`api/service/${serviceId}/`)
};

export const addService = function (data) { //创建服务
    return postRequest('api/services/', data)
};

export const deleteService = function (serviceId) {//删除服务
    return deleteRequest(`api/service/${serviceId}/`)
};

export const updateService = function (serviceId, data) { //更新服务
    return putRequest(`api/service/${serviceId}/`, data)
};
import {deleteRequest, getRequest, postRequest, putRequest} from "./common";

export const getInterfaces = function (serviceId) { //获取某个服务下的接口列表
    return getRequest(`interfaces/?service_id=${serviceId}`)
};

export const addInterface = function (data) { //创建接口
    return postRequest('interfaces/', data)
};

export const deleteInterface = function (interfaceId) {//删除接口
    return deleteRequest(`interface/${interfaceId}/`);
};

export const updateInterface = function (interfaceId, data) { //更新接口
    return putRequest(`interface/${interfaceId}/`, data)
};
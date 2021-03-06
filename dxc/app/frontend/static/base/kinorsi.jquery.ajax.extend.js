<!--定义一个新的post json, 简化一些参数的设置-->
$.postJSONEx = function(url, data, args){
    args = $.extend({
        url: url,
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json'
    }, args);
    return $.ajax(args);
};

/**
    * param url: target url.
    * param data: plain object.
**/
$.getJSONEx = function(url, data, args){
    args = $.extend({
        url: url,
        type: 'GET',
        data: data,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json'
    }, args);
    return $.ajax(args);
}

$.deleteJSONEx = function(url, data, args){
    args = $.extend({
        url: url,
        type: 'DELETE',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json'
    }, args);
    return $.ajax(args);
};
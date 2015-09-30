//增加stirng.format方法
String.prototype.format = function()
{
    // 这个方法按参数顺序，更新换{num}的值
    var new_index = 0;
    var args = arguments;
    return this.replace(/\{(\d+)\}/g,
        function(m,i){
            if(args[i] !== undefined) // 加入undefined是因为空字符串也会判断为false.
                return args[i];
            else
                // 这个是当参数不足时仍然显示'{0}', 即重新整理顺序。
                return '{'+ new_index++ +'}'
        });
}

/**
 * 检测是否有滚动条。行滚动一下看有没有。然后返回原位。
**/
function isVerScrollbarVisible(){
    $(document).scrollTop(1);
    if($(document).scrollTop() !== 0){
        $(document).scrollTop(0);
        return true;
    }

    $(document).scrollTop(0);
    return false;
}
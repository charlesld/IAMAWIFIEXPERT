/**
 * Created by hydorgen.cmm on 2016/4/18.
 */
define(function(require) {
    var $ = require('jquery');
    $(document).ready(function () {
        var setContainHeight = function () {
            var contentHeight = $(window).height() - 92 - 64;
            if (contentHeight < 500)
                contentHeight = 500;
            $('.page-content').height(contentHeight);
            var loginFormHeight = $('.form-container').height();
            var top = Math.floor((contentHeight - loginFormHeight) / 2);
            if (top < 0)
                return;
            $('.form-container').css('margin-top', top);
        };
        setContainHeight();
        $(window).resize(setContainHeight);
    })
});
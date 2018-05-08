/**
 * Created by sulong.li on 2016/1/4.
 */
define(function(require, exports, module) {

    require('bootstrap');
    var locale = require('i18n!nls/locale');
    var $ = require('jquery');

    exports.success = function(obj) {
        var success = locale.success;
        var title = obj["title"] ? obj["title"] : success;
        var content = obj["content"] ? obj["content"] : "";
        content = locale[content];
        $('.msgbox').remove();
        $("body").append($('<div class="alert alert-success msgbox"><strong>' + title + '</strong>-<span class="msgbox-content">' + content + '</span></div>').css('z-index', 10000000));
        setTimeout(function() {
            $(".msgbox").alert('close');
        }, 2000);
    };
    exports.error = function(obj) {
        var error = locale.error;
        var title = obj["title"] != undefined ? obj["title"] : error;
        var content = obj["content"] ? obj["content"] : "";
        content = locale[content];
        $('.msgbox').remove();
        $("body").append($('<div class="alert alert-danger msgbox">' +
            '<button type="button" class="close" data-dismiss="alert">×</button>' +
            '<strong>' + title + '</strong>-' +
            '<span class="msgbox-content">' + content + '</span>' +
            '</div>').css('z-index', 10000000));
    };
    exports.warn = function(obj) {
        var warning = locale.warning;
        var title = obj["title"] ? obj["title"] : warning;
        var content = obj["content"] ? obj["content"] : "";
        content = locale[content];
        $('.msgbox').remove();
        $("body").append($('<div class="alert alert-warning msgbox"><strong>' + title + '</strong>-<span class="msgbox-content">' + content + '</span></div>').css('z-index', 10000000));
        setTimeout(function() {
            $(".msgbox").alert('close');
        }, 2000);
    }

});
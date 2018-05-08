define(function (require) {
    var $ = require('jquery');
    var msgBox = require('/static/js/msgbox');
    var error = require('/static/js/error');
    var urlUtil = require('/static/js/urlutil');
    var JSEncrypt = require('jsencrypt');
    var localeUtil = require('/static/js/localeutil');
    /* fill placeholder */
    localeUtil.fillPlaceholder();
    var mac;
    var version = urlUtil.getUrlParam('version');
    if (version == '1.0') {
        mac = urlUtil.getUrlParam('sta_mac');
    } else {
        mac = urlUtil.getUrlParam('mac');
    }
    var target = null;
    if (version == '1.0') {
        target = '//captive.wifi.alibaba-inc.com/portal/api/auth';
    } else {
        var host = urlUtil.getUrlParam('host');
        host = $.trim(host);
        if ('' === host) {
            host = '1.1.1.1';
        }
        target = '//' + host +':8080/web_auth';
    }
    if (mac) {
        $.ajax({
            url: '/web/api/sta/checkShowOneClickForm.json',
            type: 'POST',
            data: {
                mac: mac,
                _tb_token_: globalVars.csrfToken
            },
            dataType: 'json',
            success: function(result) {
                if (result.success) {
                    $('.phone-placeholder').html(result.data);
                    $('#normal-form-container').hide();
                    $('#one-click-login-form-container').show();
                }
            }
        })
    }
    if (!localStorage) {
        $('.mobile-header-change-locale').hide();
        $('.header-change-locale').hide();
    }
    $('#btn-send-sm').click(function (e) {
        e.preventDefault();
        var phoneNo = $('#input-phone-no').val();
        if (!phoneNo || phoneNo.length < 6) {
            msgBox.warn({content: 'incorrectPhoneNo'});
            return;
        }
        $('#btn-send-sm').prop('disabled', true);
        var count = 60;
        var $countContainer = $('#btn-send-sm #count-down-container');
        var timer = setInterval(function () {
            if (count >= 0) {
                $countContainer.html('(' + count-- + ')')
            } else {
                $countContainer.html('');
                clearTimeout(timer);
                $('#btn-send-sm').prop('disabled', false);
            }
        }, 1000);
        var encrypt = new JSEncrypt();
        encrypt.setPublicKey(globalVars.publicKey);
        var encryptedPhoneNo = encrypt.encrypt(phoneNo);
        $.ajax({
            url: '/web/api/captcha/sendCaptcha.json',
            type: 'POST',
            data: {
                phoneNo: encryptedPhoneNo,
                pageUuid: globalVars.pageUuid,
                _tb_token_: globalVars.csrfToken
            },
            dataType: 'json',
            success: function (result) {
                if (result.success) {
                    msgBox.success({content: 'sendCaptchaSuccess'});
                } else {
                    msgBox.error({content: error[result.errorCode]});
                }
            }
        });
    });
    $('#btn-login').click(function (e) {
        e.preventDefault();
        var phoneNo = $('#input-phone-no').val();
        var captcha = $('#input-captcha').val();
        if (!phoneNo || phoneNo.length != 11) {
            msgBox.warn({content: 'pleaseEnter11PhoneNo'});
            return;
        }
        if (!captcha || !captcha.length) {
            msgBox.warn({content: 'pleaseEnterCaptcha'});
            return;
        }
        var encrypt = new JSEncrypt();
        encrypt.setPublicKey(globalVars.publicKey);
        var encryptedPhoneNo = encrypt.encrypt(phoneNo);
        var encryptedCaptcha = encrypt.encrypt(captcha);
        $.ajax({
            url: target,
            dataType: 'jsonp',
            timeout: 5000,
            data: {
                phoneNo: encryptedPhoneNo,
                captcha: encryptedCaptcha
            },

            success: function (result) {
                try {
                    if (result.auth || result.success) {
                        if (result.redirect) {
                            window.location.href = result.redirect;
                        } else {
                            msgBox.success({content: 'loginSuccess'});
                        }
                    } else {
                        msgBox.error({content: error[result.errorCode]});
                    }
                } catch (ex) {
                    msgBox.error({content: error['500']});
                }
            }
        });

    });

    $('#btn-direct-login').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: target,
            dataType: 'jsonp',
            timeout: 5000,
            success: function (result) {
                try {
                    if (result.auth || result.success) {
                        if (result.redirect) {
                            window.location.href = result.redirect;
                        } else {
                            msgBox.success({content: 'loginSuccess'});
                        }
                    } else {
                        msgBox.error({content: error[result.errorCode]});
                    }
                } catch (ex) {
                    msgBox.error({content: error['500']});
                }
            }
        });
    });
    $('#change-locale').click(function() {
        if (localStorage) {
            if ('EN' === $('#change-locale').html()) {
                localStorage.setItem('locale', 'en-us');
                location.reload();
            } else if ('中文' === $('#change-locale').html()) {
                localStorage.setItem('locale', 'zh-cn');
                location.reload();
            }
        } else {
            msgBox.warn({content: 'changeLocaleNotSupport'});
        }
    });
});
(function(arg){
	arg.extend({
		'validate':function(form){
			$(form).find(':submit').click(function(){
				var flag = true;
				$(form).find(':text,:password').each(function(){
					var name = $(this).attr('name');
					var val = $(this).val();
					if(!val || val.trim() == ''){
						flag = false;
						font = name+' is required.';
						alert(font);
						html = "<span style='color:red;'>" + font + "</span>"
						$(this).next().remove();
						$(this).after(html);
					}else{
						html = "<span style='color:green;'>OK</span>"
						$(this).next().remove();
						$(this).after(html);
					}
				});
				return flag;
			});
		}
	});
})(jQuery)

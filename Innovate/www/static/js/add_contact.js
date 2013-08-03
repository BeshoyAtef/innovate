phone_regex =  /^[0-9]+$/;
email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
skype_regex = /^[a-zA-Z][a-zA-Z0-9\.,\-_]{5,31}/;
valid_skype = false;
valid_telephone = false;
valid_email = false;

$(document).on('blur', '#id_skypename', function() {
	var content = $('#id_skypename').val();
	if (!(content.match(skype_regex))){
        valid_skype = false;
        $('#skype_error').css('display','block');
        $('#skype_error').css('color','red');
        }

        else{
        valid_skype = true;
        $('#skype_error').css('display','none'); 
        }
});

$(document).on('blur', '#id_email', function() {
	var content = $('#id_email').val();
	if (!(content.match(email_regex))){
        valid_email = false;
        $('#email_error').css('display','block');
        $('#email_error').css('color','red');
        }

        else{
        valid_email = true;
        $('#email_error').css('display','none'); 
        }
});

$(document).on('blur', '#id_telephonenumber', function() {
	var content = $('#id_telephonenumber').val();
	if (!(content.match(phone_regex))){
        valid_telephone = false;
        $('#telephone_error').css('display','block');
        $('#telephone_error').css('color','red');
        }

        else{
        valid_telephone = true;
        $('#telephone_error').css('display','none'); 
        }
});

jQuery(document).ready(function () {
    //hide a div after 3 seconds
    setTimeout(function(){ jQuery("#success_alert").hide(); }, 10000);
});

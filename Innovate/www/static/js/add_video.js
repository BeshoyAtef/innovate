regex = /^[0-9a-zA-Z][0-9a-zA-Z '-]*$/
valid_title = false;
valid_photographer = false;
valid_director = false;
valid_photographer = false;
$(document).on('blur', '#id_youtube_url', function() {
	var options = $.extend({width:570, height:416}, options);
    var text = $('#id_youtube_url').val();
    var regex = /http:\/\/(www.)?youtube\.com\/watch\?v=([A-Za-z0-9._%-]*)(\&\S+)?/  
    var html = text.replace(regex, '<iframe class="youtube-player" type="text/html" width="' + options.width + '" height="' + options.height + '" src="http://www.youtube.com/embed/$2" frameborder="0"></iframe>');
    $('#video_tag').css('margin-bottom', '12px');
    $("#video_tag").append(html);
});

$(document).on('blur', '#id_title', function() {
	$('#video_tag').hide();
	var content = $('#id_title').val();
	if (!(content.match(regex))){
        valid_title = false;
        $('#title_error').css('display','block');
        $('#title_error').css('color','red');
        }

        else{
        valid_title = true;
        $('#title_error').css('display','none'); 
        }
});

$(document).on('blur', '#id_photographer', function() {
	
	var content = $('#id_photographer').val();
	if (!(content.match(regex))){
        valid_photographer = false;
        $('#photographer_error').css('display','block');
        $('#photographer_error').css('color','red');
        }

        else{
        valid_photographer = true;
        $('#photographer_error').css('display','none'); 
        }
});


$(document).on('blur', '#id_director', function() {
	
	var content = $('#id_title').val();
	if (!(content.match(regex))){
        valid_director = false;
        $('#director_error').css('display','block');
        $('#director_error').css('color','red');
        }

        else{
        valid_director = true;
        $('#director_error').css('display','none'); 
        }
});

$(document).on('blur', '#id_producer', function() {
	var content = $('#id_title').val();
	if (!(content.match(regex))){
        valid_title = false;
        $('#producer_error').css('display','block');
        $('#producer_error').css('color','red');
        }

        else{
        valid_producer = true;
        $('#producer_error').css('display','none'); 
        }
});

jQuery(document).ready(function () {
    //hide a div after 3 seconds
    setTimeout(function(){ jQuery("#success_alert").hide(); }, 10000);
});

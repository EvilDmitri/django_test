$.ajaxSetup({
  beforeSend: function (request) {
      request.setRequestHeader('X-CSRFToken',getCookie('csrftoken'));
  },
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function () {


	function activateTab($tab) {
		var $activeTab = $tab.closest('dl').find('a.active'),
				
        contentLocation = $tab.attr("href");
        $('#model_list').children().remove();

        $.post(contentLocation, function(data, status){
          var head = ich.modelHead(data);
          $('#model_list').append(head);
          $.each(data.qs, function(index, qs) {
              var output = {'model': qs, 'fields': data.names};
              var model = ich.modelBody(output);
              $('#model_list').append(model);

          });

          $('#new_form').remove();
           $('h3').remove();
          new_model = ich.newModel(data);
          $('.eight').append(new_model);
            $('#new_form').append("<input id=path type=hidden value=" + contentLocation + ">");
        }).fail(function(){
            alert('Somthing wrong');
        });

		//Make Tab Active
		$activeTab.removeClass('active');
		$tab.addClass('active');
	}

	$('dl.tabs').each(function () {
		//Get all tabs
		var tabs = $(this).children('dd').children('a');
		tabs.click(function (e) {
			activateTab($(this));
      return false;
		});
	});

	if (window.location.hash) {
		activateTab($('a[href="' + window.location.hash + '"]'));
	}

});


//   $("#new_form").submit(function( event ) {
function post_form() {

    var path = $('#path').val();
    var msg   = $('#new_form').serialize();
        $.ajax({
          type: 'POST',
          url: path + 'create',
          data: msg,
          success: function(data) {
            $('.results').html(data);
          },
          error:  function(xhr, str){
                alert('Возникла ошибка: ' + xhr.responseCode);
            }
        }).done(function(){
            $('.active').click();
        });

}

function submit_form(input_el){
    var path = $('#path').val();


    var table = input_el.parentNode.parentNode;
    var row = table.childNodes[0];
    var columns = row.childNodes[0];
    alert(columns.className);


//        $.ajax({
//          type: 'POST',
//          url: path + 'create',
//          data: msg,
//          success: function(data) {
//            $('.results').html(data);
//          },
//          error:  function(xhr, str){
//                alert('Возникла ошибка: ' + xhr.responseCode);
//            }
//        });
}
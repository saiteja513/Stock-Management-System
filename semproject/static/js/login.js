$(function() {

    $('#tab-login').click(function(e) {
		$(".login").delay(100).fadeIn(100);
 		$(".register").fadeOut(100);
		$('#tab-register').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#tab-register').click(function(e) {
		$(".register").delay(100).fadeIn(100);
 		$(".login").fadeOut(100);
		$('#tab-login').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});

(function ($) {
"use strict";

	// preloader
	$(window).on('load', function () {
		$('#preloader').delay(350).fadeOut('slow');
		$('body').delay(350).css({ 'overflow': 'visible' });
	})
	
	// mobilemenu active
	$('#mobile-menu-active').metisMenu();

	$('#mobile-menu-active .dropdown > a').on('click', function (e) {
		e.preventDefault();
	});

	$(".hamburger-menu > a").on("click", function (e) {
		e.preventDefault();
		$(".slide-bar").toggleClass("show");
		$("body").addClass("on-side");
		$('.body-overlay').addClass('active');
		$(this).addClass('active');
	});

	$(".close-mobile-menu > a").on("click", function (e) {
		e.preventDefault();
		$(".slide-bar").removeClass("show");
		$("body").removeClass("on-side");
		$('.body-overlay').removeClass('active');
		$('.hamburger-menu > a').removeClass('active');
	});

	$('.body-overlay').on('click', function () {
		$(this).removeClass('active');
		$(".slide-bar").removeClass("show");
		$("body").removeClass("on-side");
		$('.hamburger-menu > a').removeClass('active');
	});

	//data background
	$("[data-background]").each(function () {
		$(this).css("background-image", "url(" + $(this).attr("data-background") + ") ")
	})

    // blog-post-active
	$('.blog-active').owlCarousel({
		loop:true,
		margin:50,
		autoplay:true,
		autoplayTimeout:6000,
		smartSpeed:500,
		autoplayHoverPause:true,
		items:6,
		navText:['<i class="ti-angle-left"></i>','<i class="ti-angle-right"></i>'],
		nav:true,
		dots:false,
		responsive:{
			0:{
				items:1
			},
			767:{
				items:2
			},
			992:{
				items:2
			},
			1200:{
				items:2
			}
		}
	});

  	// brand-active
	  $('.brand-active').owlCarousel({
		loop:true,
		margin:0,
		items:1,
		dots:false,
		autoplay:true,
		autoplayTimeout:5000,
		smartSpeed:500,
		autoplayHoverPause:true,
		responsive:{
			0:{
				items:1
			},
			767:{
				items:2
			},
			992:{
				items:3
			},
			1200:{
				items:3
			}
		}
	})

	/* magnificPopup img view */
	$('.popup-image').magnificPopup({
		type: 'image',
		gallery: {
		enabled: true
		}
	});

	/* magnificPopup video view */
	$('.popup-video').magnificPopup({
		type: 'iframe'
	});

	// isotop
	$('.grid').imagesLoaded( function() {
		// init Isotope
		var $grid = $('.grid').isotope({
		itemSelector: '.grid-item',
		percentPosition: true,
		masonry: {
			// use outer width of grid-sizer for columnWidth
			columnWidth: '.grid-item',
		}
	});

	// filter items on button click
	$('.gallery-menu').on( 'click', 'button', function() {
		var filterValue = $(this).attr('data-filter');
		$grid.isotope({ filter: filterValue });
		});
	});

	//for menu active class
	$('.gallery-menu button').on('click', function(event) {
		$(this).siblings('.active').removeClass('active');
		$(this).addClass('active');
		event.preventDefault();
	});
	
	// blog-post-active
		$('.gallery-post-active').owlCarousel({
		loop:true,
		margin:0,
		items:1,
		navText:['<i class="ti-arrow-left"></i>','<i class="ti-arrow-right"></i>'],
		nav:true,
		dots:false,
		responsive:{
			0:{
				items:1
			}
		}
	})

	// Counter Js
	$('.counter').counterUp({
		delay: 20,
		time: 1000
	});

	// WoW Js
	new WOW().init();
	
	// scrollToTop
	$.scrollUp({
		scrollName: 'scrollUp', // Element ID
		topDistance: '300', // Distance from top before showing element (px)
		topSpeed: 300, // Speed back to top (ms)
		animation: 'none', // Fade, slide, none
		animationInSpeed: 200, // Animation in speed (ms)
		animationOutSpeed: 200, // Animation out speed (ms)
		scrollText: '<i class="ti-arrow-up"></i>', // Text for element
		activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
	});

})(jQuery);
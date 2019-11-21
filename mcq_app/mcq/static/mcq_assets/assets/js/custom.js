(function ($) {

    /*================================
        Loader
    ==================================*/
	var preloader = $('.page_loader');
	$(window).on('load', function () {
		preloader.fadeOut('1', function () {
			$(this).remove();
		});
    });
    
	/*================================
	        WOW active
	==================================*/
    new WOW().init();
    
    /*================================
	        Show/Hide Pwd
    =====================-=============*/
    $(".toggle-password").click(function() {

        $(this).toggleClass("fa-eye fa-eye-slash");
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
      });


    /*================================
	        navbar Drop Down
	==================================*/
	$('body').on('mouseenter', '.dropdown-hover', function (e) {
		let dropdown = $(e.target).closest('.dropdown-hover');
		dropdown.addClass('show');
    });
	$('body').on('mouseleave', '.dropdown-hover', function (e) {
		let dropdown = $(e.target).closest('.dropdown-hover');
		dropdown.removeClass('show');
    });

    
    /*================================
                    Sticky Header
            ==================================*/

    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll > 30) {
            $(".main-header").addClass("fixed-header");
        } else {
            $(".main-header").removeClass("fixed-header");
        }
    });


    var swiper = new Swiper('.swiper-container', {
        grabCursor: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
          },
        loop: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });

}(jQuery));
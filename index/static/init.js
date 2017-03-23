(function() {

	skel.init({
		reset: 'full',
		breakpoints: {
			'global': { range: '*', href: res_root + 'css/style.css', viewport: { scalable: false } },
			'wide': { range: '-1680', href: res_root + 'css/style-wide.css' },
			'normal': { range: '-1280', href: res_root + 'css/style-normal.css' },
			'mobile': { range: '-736', href: res_root + 'css/style-mobile.css' },
			'mobilep': { range: '-480', href: res_root + 'css/style-mobilep.css' }
		}
	});

	// Events (JS).
		
		// Remove "loading" class once the page has fully loaded.
			window.onload = function() {
				document.body.className = '';
			}

		// Prevent scrolling on touch.
			window.ontouchmove = function() {
				return false;
			}

		// Fix scroll position on orientation change.
			window.onorientationchange = function() {
				document.body.scrollTop = 0;
			}

    $(function(){
        $("#main_form").submit(function(e){
            e.preventDefault();
            ga('send', 'event', 'button', 'click', 'main');
            $('#results').hide();
            $('#waiting').show();
            $.post(base_path + "process.php", $("#main_form").serialize(),
                function(data){
                    $('#results').hide().html(data).fadeIn('3000');
                    $('#waiting').hide() ;
                    if (window.location.href.indexOf("src=bookmarklet") > -1) {
                        url = $('#results a.button_green').first().attr('href');
                        if (url.length > 0 && url != undefined) {
                            setTimeout(function() {
                                $('#results').append('<div class="dls">Download started...</div>');
                                $('#waitingdls').hide();
                                window.location.href = url;
                            }, 6000);
                            $('#waitingdls').fadeIn(500) ;
                        }
                    }
                });
        });
        value = $("#main_form input[name=url]").val();
        if(value.length>0){
            setTimeout(function() {
                $("#main_form input[type=submit]").click();
            }, 1500);
            
        }
        $("#bookmarklet").click(function(e){
            e.preventDefault();
          alert('Drag and drop this to your bookmarks toolbar or save the link as a bookmark. When you are in Instagram, simply click the bookmark to download the photo.')  
        });
    });

})();
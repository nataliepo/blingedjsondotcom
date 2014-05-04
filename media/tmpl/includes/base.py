<!DOCTYPE html> 
<html lang="en"> 

<head>
    <meta charset="utf-8"> 

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
        <meta http-equiv="Content-Style-Type" content="text/css" /> 
        <meta http-equiv="Content-Script-Type" content="text/javascript" />

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

	    <script src="${ROOT_URL}/static/js/jquery-1.7.2.min.js"></script>  
        <script src="${ROOT_URL}/static/js/utilities.js?${random_number}"></script>  
        <link rel="icon" type="image/png" href="${ROOT_URL}/static/img/fav.ico" />
        <link rel="stylesheet" href="${ROOT_URL}/static/css/bootstrap.min.css">

        <link rel="stylesheet" href="${ROOT_URL}/static/css/bootstrap-responsive.min.css">
		
        <link rel="stylesheet" href="${ROOT_URL}/static/css/styles.css">

        <title>Blinged JSON Validator: ${page_name}</title>
</head>

    <body>
	
		<div class="navbar navbar-inverse navbar-fixed-top">
		 	#* empty nav for now *#
		 </div>
		<div class="container">
        	${body}

			#* bottom nav *#
			<div class="centered-pills">
				<ul class="nav nav-pills">
				#if $active_page == 'index'
				<li class="active">
				#else
				<li>
				#end if	
				    <a href="/">Home</a>
				</li>
							
				#if $active_page == 'about'
				<li class="active">
				#else
				<li>
				#end if
					<a href="/about">About</a>
				</li>
			
				#if $active_page == 'support'
				<li class="active">
				#else
				<li>
				#end if					
					<a href="/support">Support</a>
				</li>
				
				</ul>
				
            </div>
            <div class="mac-icon bottom">
                <p>Release History: <br />
                    v1.0.1 - 04/04/2014<br />
                    v1.0.0 - 03/06/2014</p>
                <a href="https://itunes.apple.com/us/app/blinged-json-validator/id833982915?ls=1&mt=12"><img src="${ROOT_URL}/static/img/mac-store.png" /></a>
            </div>
		
		</div>
		
	
        #* GA *#
        <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-48626214-1', 'blingedjsonvalidator.com');
      ga('send', 'pageview');

        </script>
    </body>
</html>
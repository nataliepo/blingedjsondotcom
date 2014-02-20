<!DOCTYPE html> 
<html lang="en"> 

<head>
    <meta charset="utf-8"> 

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
        <meta http-equiv="Content-Style-Type" content="text/css" /> 
        <meta http-equiv="Content-Script-Type" content="text/javascript" />

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

	    <script src="static/js/jquery-1.7.2.min.js"></script>  
        <script src="static/js/utilities.js?${random_number}"></script>  

        <link rel="stylesheet" href="static/css/bootstrap.min.css">

        <link rel="stylesheet" href="static/css/bootstrap-responsive.min.css">
		
        <link rel="stylesheet" href="static/css/styles.css">

		#* typekit *#
		<script type="text/javascript" src="//use.typekit.net/sgr1ljb.js"></script>
		<script type="text/javascript">try{Typekit.load();}catch(e){}</script>
		

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
		
		</div>
		
	
		
    </body>
</html>
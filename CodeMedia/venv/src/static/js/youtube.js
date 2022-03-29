//https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId=UCd-sdbnIn3NQshYZdYvovUg&maxResults=25&key=AIzaSyADmGM2IlkavvHcQs1n0XU_JNCyoIuqhnM


var channelId = "UCd-sdbnIn3NQshYZdYvovUg"
var apikey = "AIzaSyADmGM2IlkavvHcQs1n0XU_JNCyoIuqhnM"


  var template = null 


$.ajax({
 	url: 'https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId='+channelId+'&maxResults=25&key='+apikey,
 	type: 'GET',
 	dataType: 'json',
 	//data: {param1: 'value1'},
 })
 .done(function(data) {
     //  need to make a function for this
     for (var i =0;  i < data.items.length; i++) {


     if (window.screen.width >= 0 && window.screen.width <= 768) {
		   console.log("window size")
		template =  "<div class='row justify-content-md-center'>\
            <div class='col-md-auto' style='margin-bottom:100'>\
                <iframe width='300px' height='200px' src='https://www.youtube.com/embed/"+data.items[i].id.videoId+"'  frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>\
          </div>\
        </div>\
        "
		
	} else {

		template = "<div class='row justify-content-md-center'>\
            <div class='col-md-auto' style='margin-bottom:100'>\
                <iframe width='800px' height='400px' src='https://www.youtube.com/embed/"+data.items[i].id.videoId+"'  frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>\
          </div>\
        </div>\
        "
	}
        
        $("#youtube_insert").append(template)
     }

 	
 })
 .fail(function() {
 	console.log("error");
 })
 .always(function() {
 	console.log("complete");
 });
 
 
 $(document).on('load', '.selector', function(event) {
     event.preventDefault();
     console.log("document loaded")
     /* Act on the event */
 });


 function getYoutubeTitle(index){


 }
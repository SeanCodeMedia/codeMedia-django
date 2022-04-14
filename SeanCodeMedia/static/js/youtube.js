//https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId=UCd-sdbnIn3NQshYZdYvovUg&maxResults=25&key=AIzaSyADmGM2IlkavvHcQs1n0XU_JNCyoIuqhnM


//   var template = null 


// $.ajax({
//  	url: 'https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId='+channelId+'&maxResults=25&key='+apikey,
//  	type: 'GET',
//  	dataType: 'json',
//  	//data: {param1: 'value1'},
//  })
//  .done(function(data) {
//      //  need to make a function for this
//      for (var i =0;  i < data.items.length; i++) {


//      if (window.screen.width >= 0 && window.screen.width <= 768) {
// 		   console.log("window size")
// 		template =  "<div class='row justify-content-md-center'>\
//             <div class='col-md-auto' style='margin-bottom:100'>\
//                 <iframe width='300px' height='200px' src='https://www.youtube.com/embed/"+data.items[i].id.videoId+"'  frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>\
//           </div>\
//         </div>\
//         "
		
// 	} else {

// 		template = "<div class='row justify-content-md-center'>\
//             <div class='col-md-auto' style='margin-bottom:100'>\
//                 <iframe width='800px' height='400px' src='https://www.youtube.com/embed/"+data.items[i].id.videoId+"'  frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>\
//           </div>\
//         </div>\
//         "
// 	}
        
//         $("#youtube_insert").append(template)
//      }

 	
//  })
//  .fail(function() {
//  	console.log("error");
//  })
//  .always(function() {
//  	console.log("complete");
//  });
 
 
//  $(document).on('load', '.selector', function(event) {
//      event.preventDefault();
//      console.log("document loaded")
//      /* Act on the event */
//  });


//  function getYoutubeTitle(index){


//  }


// var youtubeData = null; 
// var currentPage = null;


// $(document).ready(function($) {
//    $.ajax({
//      url: 'https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId='+channelId+'&maxResults=25&key='+apikey,
//      type: 'GET',
//      dataType: 'json',
//      //data: {param1: 'value1'},
//  }).done(function(data) {
//       youtubeData = data 
//       check_page()
//  }) 
// });




// function buildVideos(range){
//    var codeTemplate = null
//    var moreVideos = null
//     for (var i = 0; i < range; i++) {
//            //wow fadeInLeft
//            // wow fadeInRight
//         if(i%2 == 0){
            
//             codeTemplate =' <li class="wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s">\
//                             <div class="list_inner tilt-effect">\
//                                 <span class="icon">\
//                                     <img class="back" src="./static/images/youtube.png" alt="" />\
//                                 </span>\
//                                 <div class="title">\
//                                     <h3>'+getTitle(i)+'</h3>\
//                                 </div>\
//                                 <div>\
//                                 <img src="'+getThumbnail(i)+'" width="320px" height="180px" alt="" /> \
//                                 </div>\
//                                 <a class="aali_tm_full_link" href="#"></a>\
//                                 <img class="popup_service_image" src="img/service/2.jpg" alt="" />\
//                                 <div class="service_hidden_details">\
//                                     <div class="service_popup_informations">\
//                                        <iframe width="800px" height="400px" src="https://www.youtube.com/embed/'+getVideoID(i)+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\
//                                           <h3>Description</h3>\
//                                          <p>\
//                                              '+getDescription(i)+'\
//                                            </p>\
//                                         </div>\
//                                     </div>\
//                                 </div>\
//                             </div>\
//                         </il>'

                
        
//         } else {

//             codeTemplate = ' <li class="wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.2s">\
//                             <div class="list_inner tilt-effect">\
//                                 <span class="icon"> \
//                                      <img class="back" src="./static/images/youtube.png" alt="" />\
//                                 </span>\
//                                 <div class="title">\
//                                     <h3>'+getTitle(i)+'</h3>\
//                                 </div>\
//                                 <div>\
//                                     <img src="'+getThumbnail(i)+'" width="320px" height="180px" alt="" /> \
//                                 </div>\
//                                 <a class="aali_tm_full_link" href="#"></a>\
//                                 <img class="popup_service_image" src="img/service/1.jpg" alt="" />\
//                                 <div class="service_hidden_details">\
//                                     <div class="service_popup_informations">\
//                                      <iframe width="800px" height="400px" src="https://www.youtube.com/embed/'+getVideoID(i)+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\
//                                         <div class="description">\
//                                            <h3>Description</h3>\
//                                            <p>\
//                                              '+getDescription(i)+'\
//                                            </p>\
//                                         </div>\
//                                     </div>\
//                                 </div>\
//                             </div>\
//                         </li>'
          
//         }

//         $("#youtube_section").append(codeTemplate)

//         aali_tm_service_popup()
//         tiltEffect()


//     }
    
//     moreVideos = '<li class="simple text wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s">\
//                             <div class="list_inner">\
//                                 <div class="wrapper">\
//                                     <div class="inner_text">\
//                                          <h3>Want More Videos ?</h3>\
//                                     </div>\
//                                     <div class="aali_tm_button ">\
//                                         <a class="anchor" href="videos"><span>More Videos <img class="svg" src="./static/images/svg/video.png" alt="" /></span></a>\
//                                     </div>\
//                                 </div>\
//                             </div>\
//                         </li>'

//      if(currentPage =="home"){
//         console.log("home")
//         $("#youtube_section").append(moreVideos)
//       }
      

//     aali_tm_service_popup()
//     tiltEffect()
// }

// function getVideoID(index) {
//       id  = youtubeData.items[index].id.videoId
//       return id
// }

// function getDescription(index){
//       Description = youtubeData.items[index].snippet.description
//       return Description
// }

// function getThumbnail(index){
//       // images size is 480 x 360
//       thumbnail = youtubeData.items[index].snippet.thumbnails.high.url
//       return thumbnail
// }


// function getTitle(index){
  
//       title = youtubeData.items[index].snippet.title
//       if(title.length > 50){
           
//         title = title.substr(0,25)+"....";
//       }
//       return title
// }


const channelId = "UC8qa9USnmzi-ewkXTMiZ9LA"
const apikey =    "AIzaSyBeDsyxjvdjJXrbsBw-TArdAynpAuLI4mQ"  //"AIzaSyADmGM2IlkavvHcQs1n0XU_JNCyoIuqhnM"


class YouTubeLayout {
 
  constructor(pageName="home"){
    this.pageName = pageName
    this.youtubeData; 
    this.get_data()
   }

  get_data(){
    self = this;
    $.ajax({
        type : "GET",
        url : 'https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId='+channelId+'&maxResults=25&key='+apikey,
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : {},
        success : function(data){
          console.log(data);
          self.load_table(data);
        },
      });
  }
    load_table(data){
      
      this.youtubeData = data
      this.check_page(this.pageName,data)
   
    }

check_page (page, data) {
         
     if (page == "home"){
         this.buildVideos(4)
     } else if (page=="videos"){
         this.currentPage = "videos"
         this.buildVideos(data.items.length)  
     }
}



buildVideos(range){
   var codeTemplate = null
   var moreVideos = null
    for (var i = 0; i < range; i++) {
           //wow fadeInLeft
           // wow fadeInRight
        if(i%2 == 0){
            
            this.codeTemplate =' <li class="wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s">\
                            <div class="list_inner tilt-effect">\
                                <span class="icon">\
                                    <img class="back" src="./static/images/youtube.png" alt="" />\
                                </span>\
                                <div class="title">\
                                    <h3>'+this.getTitle(i)+'</h3>\
                                </div>\
                                <div>\
                                <img src="'+this.getThumbnail(i)+'" width="320px" height="180px" alt="" /> \
                                </div>\
                                <a class="aali_tm_full_link" href="#"></a>\
                                <img class="popup_service_image" src="img/service/2.jpg" alt="" />\
                                <div class="service_hidden_details">\
                                    <div class="service_popup_informations">\
                                       <iframe width="800px" height="400px" src="https://www.youtube.com/embed/'+this.getVideoID(i)+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\
                                          <h3>Description</h3>\
                                         <p>\
                                             '+this.getDescription(i)+'\
                                           </p>\
                                        </div>\
                                    </div>\
                                </div>\
                            </div>\
                        </il>'

                
        
        } else {

            this.codeTemplate = ' <li class="wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.2s">\
                            <div class="list_inner tilt-effect">\
                                <span class="icon"> \
                                     <img class="back" src="./static/images/youtube.png" alt="" />\
                                </span>\
                                <div class="title">\
                                    <h3>'+this.getTitle(i)+'</h3>\
                                </div>\
                                <div>\
                                   <img src="'+this.getThumbnail(i)+'" width="320px" height="180px" alt="" /> \
                                </div>\
                                <a class="aali_tm_full_link" href="#"></a>\
                                <img class="popup_service_image" src="img/service/1.jpg" alt="" />\
                                <div class="service_hidden_details">\
                                    <div class="service_popup_informations">\
                                     <iframe width="800px" height="400px" src="https://www.youtube.com/embed/'+this.getVideoID(i)+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\
                                        <div class="description">\
                                           <h3>Description</h3>\
                                           <p>\
                                             '+this.getDescription(i)+'\
                                           </p>\
                                        </div>\
                                    </div>\
                                </div>\
                            </div>\
                        </li>'
          
        }

        $("#youtube_section").append(this.codeTemplate)

        aali_tm_service_popup()
        tiltEffect()


    }
    
    this.moreVideos = '<li class="simple text wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.2s">\
                            <div class="list_inner">\
                                <div class="wrapper">\
                                    <div class="inner_text">\
                                         <h3>Want More Videos ?</h3>\
                                    </div>\
                                    <div class="aali_tm_button ">\
                                        <a class="anchor" href="videos"><span>More Videos <img class="svg" src="./static/images/svg/video.png" alt="" /></span></a>\
                                    </div>\
                                </div>\
                            </div>\
                        </li>'

     if(this.pageName =="home"){
        console.log("home")
        $("#youtube_section").append(this.moreVideos)
      }
      

    aali_tm_service_popup()
    tiltEffect()
}

 getVideoID(index) {
      let id  = this.youtubeData.items[index].id.videoId
      return id
}

 getDescription(index){
      let Description = this.youtubeData.items[index].snippet.description
      return Description
}

 getThumbnail(index){
      // images size is 480 x 360
      let thumbnail = this.youtubeData.items[index].snippet.thumbnails.high.url
      console.log(index)
      return thumbnail
}


   getTitle(index){
  
      let title = this.youtubeData.items[index].snippet.title
      console.log(title)
      if(title.length > 50){
           
        title = title.substr(0,25)+"....";
      }
      return title
}


}

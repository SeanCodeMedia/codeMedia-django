

jQuery(document).ready(function($) {
   console.log("running")
  $("#download").click(function (e) {
   e.preventDefault();
    
   $.ajax({
         url: '/resume/',
         type: 'post',
         data: {},
         success: function (data) {
            "start download"
         }
      });
   });

});



 function get_year () {
    const d = new Date();
    let year = d.getFullYear();
    console.log("year " + year)
    
     document.getElementById("year").innerHTML = "Copy Right &copy; "+year
  }

   get_year ()

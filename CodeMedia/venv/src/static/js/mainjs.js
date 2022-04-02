
 function get_year () {
    const d = new Date();
    let year = d.getFullYear();
    console.log("year " + year)
    
     document.getElementById("year").innerHTML = year
  }
  


$(document).ready(function() {

get_year ()
})

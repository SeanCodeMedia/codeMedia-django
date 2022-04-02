
 function get_year () {
    const d = new Date();
    let year = d.getFullYear();
    console.log("year " + year)
    
     document.getElementById("year").innerHTML = "Copy Right &copy; "+year
  }
  

get_year ()

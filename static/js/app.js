// Functions
(function(){
    console.log("hit");
})()

function moveForwards() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("fowardsResponse").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "/forwards", true);
  xhttp.send();
}

// function to generate heatmaps.
function onclick1(){
    var d = document.getElementById("dept1").value;
    var n=document.getElementById("police").value;
    var start=document.getElementById("fromtime").value;
    var end=document.getElementById("totime").value;

    start+=":00";
    end+=":00";

    var payload = {
                    "city_name" : "Los Angeles", // remember to change this to the variable later.
                    "n" : n,
                    "start" : start,
                    "end" : end
                }
    
    alert(d);
    fetch('http://localhost:8000/allocate/Heatmap', {
        method: 'POST',
    alert(n+" "+start+" "+end, "info");
    fetch("http://localhost:8000/allocate/Heatmap", {
        method: "POST",
        headers:{
            'Content-Type': 'application/json'
            },
        body:JSON.stringify(payload)
        }
    )
    .then(response => response.text())
<<<<<<< HEAD
    .then(text => console.log(text))
>>>>>>> b35ec66e24f604bce501ce6be97137e07f28c345
=======
    .then(text => window.location.replace(text))
>>>>>>> 1496d1211aa4ddc4b25876ed5bd6b5a7df2e25dd
}

// slight variations for the zone plotting.
function onclick2(){
    var n=document.getElementById("police").value;
    var start=document.getElementById("fromtime").value;
    var end=document.getElementById("totime").value;

    start+=":00";
    end+=":00";

    var payload = {
                    "city_name" : "Los Angeles", // remember to change this to the variable later.
                    "n" : n,
                    "start" : start,
                    "end" : end
                }
    
    alert(n+" "+start+" "+end, "info");
    fetch("http://localhost:8000/allocate/Patrol", {
        method: "POST",
        headers:{
            'Content-Type': 'application/json'
            },
        body:JSON.stringify(payload)
        }
    )
    .then(response => response.text())
    .then(text => window.location.replace(text))
}

// function to generate heatmaps.
function onclick1(){
    var d = document.getElementById("dept1").value;
    var n=document.getElementById("police").value;
    var start=document.getElementById('fromtime').value;
    var end=document.getElementById('totime').value;

    start+=":00";
    end+=":00";
    
    alert(d);
    fetch('http://localhost:8000/allocate/Heatmap', {
        method: 'POST',
        headers:{
            'Accept': 'application/json',
            },
        body:{
            'n' : n,
            'start' : start,
            'end' : end
            }
        }
    )
    .then(response => response.text())
    .then(text => console.log(text))
>>>>>>> b35ec66e24f604bce501ce6be97137e07f28c345
}

// slight variations for the zone plotting.
function onclick2(){
    var n=document.getElementById("police").value;
    var start=document.getElementById('fromtime').value;
    var end=document.getElementById('totime').value;

    start+=":00";
    end+=":00";

    alert(n+" "+start+" "+end);
}
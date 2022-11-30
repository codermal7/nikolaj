
// function to generate heatmaps.
function onclick1(){
    var n=document.getElementById("police").value;
    var start=document.getElementById('fromtime').value;
    var end=document.getElementById('totime').value;

    start+=":00";
    end+=":00";
    
    alert(n+" "+start+" "+end, 'info');
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
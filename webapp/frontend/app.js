function onclick1(){
    var n=document.getElementById("police").value;
    var start=document.getElementById('fromtime').value;
    var end=document.getElementById('totime').value;

    start+=":00";
    end+=":00";

    alert(n+" "+start+" "+end);
}

function onclick2(){
    var n=document.getElementById("police").value;
    var start=document.getElementById('fromtime').value;
    var end=document.getElementById('totime').value;

    start+=":00";
    end+=":00";
    
    alert(n+" "+start+" "+end);
}
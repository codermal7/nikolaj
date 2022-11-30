function onclick1(){
    var d = document.getElementById("dept1").value;
    var n=document.getElementById("police").value;
    var start=document.getElementById('fromtime').value;
    var end=document.getElementById('totime').value;

    start+=":00";
    end+=":00";

    alert(d+" "+start+" "+end);
}

function onclick2(){
    var n=document.getElementById("police").value;
    var start=document.getElementById('fromtime').value;
    var end=document.getElementById('totime').value;

    start+=":00";
    end+=":00";
    
    alert(n+" "+start+" "+end);
}
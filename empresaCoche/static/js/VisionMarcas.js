//Author: Aimar Jiménez, Eneko Hernando, Maria Angeles Angulo


function toggleVision(id){
    
    var carDivs = document.getElementsByClassName("coche");
    var coches = document.getElementsByName(""+id)
    for(var j = 0; j<carDivs.length; j++){
        if(""+id === "ALL"){
            carDivs[j].style.display = "block";
        } else {
            carDivs[j].style.display = "none";
        }
        
        
    }

    for (var i = 0; i < coches.length; i++){
        if(coches[i].style.display === "none"){
            coches[i].style.display = "block";
        } else {
          coches[i].style.display = "none";
        }
    }
    
}
//Author: Aimar Jiménez, Eneko Hernando, Maria Angeles Angulo

function showCar(id){
    var carDivs = document.getElementsByClassName("cocheView");
    var coches = document.getElementsByName(""+id)
    for(var j = 0; j<carDivs.length; j++){
       
        carDivs[j].style.display = "none";
   
    }

    for (var i = 0; i < coches.length; i++){
        
        coches[i].style.display = "block";
        
    }
}
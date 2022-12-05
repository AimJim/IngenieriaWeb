function clickCar(id){
    var car = document.getElementById("coche"+id);
    car.setAttribute('name', 'carT');
}

function exitCar(id){
    setTimeout(() => {  
        var car = document.getElementById("coche"+id);
        car.removeAttribute('name'); 
    }, 100);
    
}
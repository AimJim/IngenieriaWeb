function loadDocCarPaint(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        document.getElementById("coloresDisplay").innerHTML = this.responseText;
    }
    xhttp.open("GET","static/txt/colores.txt");
    xhttp.send();
}

function loadDocCarRental(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        document.getElementById("Rental").innerHTML = this.responseText;
    }
    xhttp.open("GET","static/txt/Rental.txt");
    xhttp.send();
}

function loadDocCarFinancing(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        document.getElementById("Financing").innerHTML = this.responseText;
    }
    xhttp.open("GET","static/txt/Financing.txt");
    xhttp.send();
}

function loadDocCarInspection(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        document.getElementById("Inspection").innerHTML = this.responseText;
    }
    xhttp.open("GET","static/txt/Inspection.txt");
    xhttp.send();
}

function loadDocCarRepairing(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        document.getElementById("Repairing").innerHTML = this.responseText;
    }
    xhttp.open("GET","static/txt/Repairing.txt");
    xhttp.send();
}

function loadDocCarCleaning(){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        document.getElementById("Cleaning").innerHTML = this.responseText;
    }
    xhttp.open("GET","static/txt/Cleaning.txt");
    xhttp.send();
}
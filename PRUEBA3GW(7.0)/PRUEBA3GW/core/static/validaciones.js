function validarID(){
    var id = document.querySelector("#id");
    if(id.value.length == 6 || id.value.length == 7){
        id.classList.remove("error")
    }else{
        id.classList.add("error")
    }
}


function validarID2(){
    var id = document.querySelector("#id2");
    if(id.value.length == 6 || id.value.length == 7){
        id.classList.remove("error")
    }else{
        id.classList.add("error")
    }
}
function validarNombre(input){
    var dato = document.querySelector(input);
    if(dato.value.length >=3 && dato.value.length <= 20){
        dato.classList.remove("error")
    }else{
        dato.classList.add("error")
    }
}

function validarPrecio(){
    var dato = document.querySelector('#precio');
    if(parseInt(dato.value) >=100 && parseInt(dato.value) <= 1000000){
        dato.classList.remove("error")
    }else{
        dato.classList.add("error")
    }
}
function validarPrecio2(){
    var dato = document.querySelector('#precio2');
    if(parseInt(dato.value) >=100 && parseInt(dato.value) <= 1000000){
        dato.classList.remove("error")
    }else{
        dato.classList.add("error")
    }
}

function validarUsuario(){
    var usuario = document.querySelector("#usuario");
    if(usuario.value.length == 4 || usuario.value.length == 12){
        usuario.classList.remove("error")
    }else{
        usuario.classList.add("error")
    }
}

function validarCorreo(input){
    var dato = document.querySelector(input);
    if(dato.value.length >=3 && dato.value.length <= 20){
        dato.classList.remove("error")
    }else{
        dato.classList.add("error")
    }
}
function validar(){
    var inputs = document.querySelectorAll("input, select");
    for (var i of inputs){
       if(i.classList.contains("error")){
        document.querySelector("#msj").innerHTML = "revise el campo"+i.name;
        return false;
       }
    }
  
    return true;
}
function validar2(){
    var inputs = document.querySelectorAll("input, select");
    for (var i of inputs){
       if(i.classList.contains("error")){
        document.querySelector("#msj2").innerHTML = "revise el campo"+i.name;
        return false;
       }
    }
  
    return true;
}
function validarUserSub(input){
    var dato = document.querySelector(input);
    if(dato.value.length >=3 && dato.value.length <= 20){
        dato.classList.remove("error")
    }else{
        dato.classList.add("error")
    }
}
function validarLogin(input){
    var dato = document.querySelector(input);
    if(dato.value.length >=3 && dato.value.length <= 20){
        dato.classList.remove("error")
    }else{
        dato.classList.add("error")
    }
}
function validarRegistro(input){
    var dato = document.querySelector(input);
    if(dato.value.length >=3 && dato.value.length <= 20){
        dato.classList.remove("error")
    }else{
        dato.classList.add("error")
    }
}





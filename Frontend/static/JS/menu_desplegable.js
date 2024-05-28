// menu_desplegable.js

document.addEventListener("DOMContentLoaded", function() {
    var menuDesplegable = document.getElementById("menuDesplegable");
    var fotoPerfil = document.querySelector(".imagen_user img");

    fotoPerfil.addEventListener("click", function() {
        if (menuDesplegable.style.display === "none" || menuDesplegable.style.display === "") {
            menuDesplegable.style.display = "block";
        } else {
            menuDesplegable.style.display = "none";
        }
    });
});

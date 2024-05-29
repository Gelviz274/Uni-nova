


document.addEventListener("DOMContentLoaded", function() {
    var dropdownButton = document.getElementById("dropdownButton");
    var dropdownMenu = document.getElementById("menuDesplegable");

    if (dropdownButton && dropdownMenu) {
        dropdownButton.addEventListener("click", function(event) {
            event.stopPropagation();
            dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
        });

        document.addEventListener("click", function(event) {
            if (!dropdownMenu.contains(event.target) && event.target !== dropdownButton) {
                dropdownMenu.style.display = "none";
            }
        });

        dropdownMenu.addEventListener("click", function(event) {
            event.stopPropagation();
        });
    } else {
        console.error("No se pudo encontrar el botón de despliegue o el menú desplegable.");
    }
});


    // Obtener el botón y el modal
    var botonAbrirModal = document.getElementById("abrirModal");
    var modal = document.getElementById("myModal");

    // Obtener el elemento para cerrar el modal
    var spanCerrarModal = document.getElementById("cerrarModal");

    // Cuando se haga clic en el botón, abrir el modal
    botonAbrirModal.onclick = function() {
        modal.style.display = "flex";
    }

    // Cuando se haga clic en la 'x', cerrar el modal
    spanCerrarModal.onclick = function() {
        modal.style.display = "none";
    }

    // Cuando el usuario haga clic en cualquier parte fuera del modal, cerrarlo
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }



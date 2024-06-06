document.addEventListener('DOMContentLoaded', function() {
    const editarPerfilBtn = document.getElementById('editarPerfilBtn');
    const editarPerfilModal = new bootstrap.Modal(document.getElementById('editarPerfilModal'));
    

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

    if (editarPerfilBtn) {
        editarPerfilBtn.addEventListener('click', () => {
            editarPerfilModal.show();
        });
    }
});


    // Obtener el botón y el modal




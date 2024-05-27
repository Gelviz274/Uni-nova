document.addEventListener('DOMContentLoaded', function() {
    // Obtener el botón "Editar Perfil" por su ID
    const editarPerfilBtn = document.getElementById('editarPerfilBtn');

    // Obtener el modal de edición por su ID
    const editarPerfilModal = document.getElementById('editarPerfilModal');

    // Asegurarse de que el modal está oculto inicialmente
    editarPerfilModal.style.display = 'none';

    // Agregar un listener de evento al botón "Editar Perfil"
    if (editarPerfilBtn) {
        editarPerfilBtn.addEventListener('click', () => {
            // Mostrar el modal al hacer clic en el botón
            editarPerfilModal.style.display = 'flex';
        });
    }

    // Obtener el botón de cierre del modal por su clase "close"
    const closeModalBtn = document.querySelector('.close');

    // Agregar un listener de evento al botón de cierre del modal
    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', () => {
            // Ocultar el modal al hacer clic en el botón de cierre
            editarPerfilModal.style.display = 'none';
        });
    }

    // jQuery para manejar el envío del formulario y el cierre automático del modal
    $('#editarPerfilForm').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function(response) {
                if (response.success) {
                    setTimeout(function() {
                        editarPerfilModal.style.display = 'none';
                        location.reload();
                    }, 1000);  // Cerrar el modal después de 1 segundo
                } else {
                    alert(response.message || 'Ocurrió un error al guardar los cambios.');
                }
            },
            error: function(xhr, status, error) {
                var errorMessage = xhr.status + ': ' + xhr.statusText;
                alert('Ocurrió un error al guardar los cambios. ' + errorMessage);
            }
        });
    });

    // Manejar el cierre del modal si se hace clic fuera de él
    window.addEventListener('click', (event) => {
        if (event.target === editarPerfilModal) {
            editarPerfilModal.style.display = 'none';
        }
    });
});

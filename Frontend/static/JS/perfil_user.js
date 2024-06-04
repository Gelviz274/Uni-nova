document.addEventListener('DOMContentLoaded', function() {
    const editarPerfilBtn = document.getElementById('editarPerfilBtn');
    const editarPerfilModal = new bootstrap.Modal(document.getElementById('editarPerfilModal'));

    if (editarPerfilBtn) {
        editarPerfilBtn.addEventListener('click', () => {
            editarPerfilModal.show();
        });
    }
});

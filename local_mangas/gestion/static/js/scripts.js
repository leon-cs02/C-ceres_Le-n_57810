document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const menuToggle = document.getElementById("menu-toggle");
    const closeSidebar = document.getElementById("close-sidebar");

    menuToggle.addEventListener("click", function(e) {
        e.preventDefault();
        sidebar.style.width = "250px";
        document.body.classList.add("sidebar-open");
    });

    closeSidebar.addEventListener("click", function(e) {
        e.preventDefault();
        sidebar.style.width = "0";
        document.body.classList.remove("sidebar-open");
    });
});

// Función para mostrar la imagen seleccionada
document.getElementById("id_imagen").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const previewImage = document.getElementById("preview-image");
            previewImage.src = e.target.result;
            previewImage.classList.remove("hidden"); // Mostrar la imagen
        }
        reader.readAsDataURL(file);
    }
});

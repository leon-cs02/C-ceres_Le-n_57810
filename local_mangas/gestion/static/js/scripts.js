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

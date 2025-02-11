document.addEventListener('DOMContentLoaded', function() {
    let $tema = document.getElementById('tema');
    let $html = document.getElementsByTagName('html')[0];

    // Inicializar el tema basado en el estado del checkbox
    if ($tema.checked) {
        $html.setAttribute("data-theme", "light");
    } else {
        $html.setAttribute("data-theme", "dark");
    }

    // Escuchar cambios en el checkbox
    $tema.addEventListener('change', function() {
        if ($tema.checked) {
            $html.setAttribute("data-theme", "light");
        } else {
            $html.setAttribute("data-theme", "dark");
        }
    });
});
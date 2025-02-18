document.addEventListener('DOMContentLoaded', function() {
    let $btn_tema = document.getElementById('tema');
    let $html_tema = document.querySelector('html');

    // Tema guardado en localStorage al cargar la paguina
    const temaGuardado = localStorage.getItem('data-theme');
    if (temaGuardado) {
        $html_tema.setAttribute('data-theme', temaGuardado);
    }
    // Inicializar el tema basado en el estado del checkbox
    if ($btn_tema.checked) {
        $html.setAttribute("data-theme", "light");
    } else {
        $html.setAttribute("data-theme", "dark");
    }

    // Escuchar cambios en el checkbox
    $tema.addEventListener('change', function() {
        if ($btn_tema.checked) {
            $html_tema.setAttribute("data-theme", "light");
            localStorage.setItem('data_theme', 'light');
        } else {
            $html_tema.setAttribute("data-theme", "dark");
            localStorage.setItem('data_theme', 'dark');
        }
    });
});
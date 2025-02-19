document.addEventListener('DOMContentLoaded', function() {
    let $btn_tema = document.getElementById('tema');
    let $html_tema = document.querySelector('html');

    // Tema guardado en localStorage al cargar la página
    const temaGuardado = localStorage.getItem('data-theme');
    if (temaGuardado) {
        $html_tema.setAttribute('data-theme', temaGuardado);
        $btn_tema.checked = temaGuardado === 'light';
    }

    // Escuchar cambios en el checkbox
    $btn_tema.addEventListener('change', function() {
        if ($btn_tema.checked) {
            $html_tema.setAttribute("data-theme", "light");
            localStorage.setItem('data-theme', 'light');
        } else {
            $html_tema.setAttribute("data-theme", "dark");
            localStorage.setItem('data-theme', 'dark');
        }
    });
});
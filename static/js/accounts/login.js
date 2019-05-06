$(document).ready(function() {

    /**
     * Form Validation
     */
    var form = $('#loginForm').validate({
        rules: {
            username: {
                required: true,
                email: true,
            },
            password: {
                required: true,
            },
        },
        errorElement: "em",
        wrapper: 'div',
        errorPlacement: errorFeedback,
        highlight: fieldHighlight,
        unhighlight: fieldUnhighlight,
    });

    // Envio del formulario
    $('#loginForm').submit(function(e) {
        e.preventDefault();
        // Enviar formulario si es válido

        if (form.valid()) {
            var formulario = document.getElementById('loginForm');
            formulario.submit();
        }
    });

});

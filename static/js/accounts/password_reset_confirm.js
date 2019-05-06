$(document).ready(function() {

    /**
     * Form Validation
     */
    var form = $('#passwordResetConfirmForm').validate({
        rules: {
            new_password1: {
                required: true,
                minlength: 8,
            },
            new_password2: {
                required: true,
                equalTo: "#id_new_password1"
            },
        },
        messages: {
            new_password2: {
                equalTo: "Las contraseñas no coinciden."
            }
        },
        errorElement: "em",
        wrapper: 'div',
        errorPlacement: errorFeedback,
        highlight: fieldHighlight,
        unhighlight: fieldUnhighlight,
    });

    // Envio del formulario
    $('#passwordResetConfirmForm').submit(function(e) {
        e.preventDefault();
        // Enviar formulario si es válido

        if (form.valid()) {
            var formulario = document.getElementById('passwordResetConfirmForm');
            formulario.submit();
        }
    });

});

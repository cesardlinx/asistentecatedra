$(document).ready(function() {

    /**
     * Form Validation
     */
    var form = $('#passwordChangeForm').validate({
        rules: {
            old_password: {
                required: true,
            },
            new_password1: {
                required: true,
                minlength: 8,
                numbers: true,
                uppercase: true,
                lowercase: true
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
    $('#passwordChangeForm').submit(function(e) {
        e.preventDefault();
        // Enviar formulario si es válido

        if (form.valid()) {
            var formulario = document.getElementById('passwordChangeForm');
            formulario.submit();
        }
    });

});

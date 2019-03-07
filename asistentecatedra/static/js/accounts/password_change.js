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
        errorPlacement: function(error, element) {
            error.addClass('invalid-feedback');
            error.insertAfter(element);
        },
        highlight: function(element, errorClass, validClass) {

            // Si no tiene la clase de campo especial
            if (!$(element).hasClass('special-field')) {
                $(element).addClass("error");
            }

            // cambio de color a danger para campos floating input
            if ($(element).hasClass('floating-input')) {
                $(element).prev().addClass('label-error');
            }

            // cambio de color a danger para campos select
            if ($(element).hasClass('custom-select')) {
                $(element).parent().addClass('select-error');
            }


        },
        unhighlight: function(element, errorClass, validClass) {
            // Si no tiene la clase de campo especial
            if (!$(element).hasClass('special-field')) {
                $(element).removeClass("error");
            }

            // quitar cambio de color a danger para campos floating input
            if ($(element).hasClass('floating-input')) {
                $(element).prev().removeClass('label-error');
            }

            // quitar cambio de color a danger para campos select
            if ($(element).hasClass('custom-select')) {
                $(element).parent().removeClass('select-error');
            }
        },
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

$(document).ready(function() {

    /**
     * Form Validation
     */
    var form = $('#resetPasswordForm').validate({
        rules: {
             email: {
                 required: true,
                 email: true,
                 remote: {
                     url: "/accounts/ajax/exists_email_validator/",
                     type: "post",
                     data: {
                         'email': function() {
                             return $('#id_email').val();
                         }
                     },
                 }
             },

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

    $('#guardarCambios').on('click', function() {
        $('#resetPasswordForm').trigger('submit');
    });

    // Envio del formulario
    $('#resetPasswordForm').submit(function(e) {
        e.preventDefault();
        // Enviar formulario si es válido

        if (form.valid()) {
            var formulario = document.getElementById('resetPasswordForm');
            formulario.submit();
        }
    });

});

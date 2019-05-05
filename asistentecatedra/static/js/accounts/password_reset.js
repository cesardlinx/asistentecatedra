$(document).ready(function() {

    /**
     * Form Validation
     */
    var form = $('#passwordResetForm').validate({
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
        errorPlacement: errorFeedback,
        highlight: fieldHighlight,
        unhighlight: fieldUnhighlight,
    });

    $('#guardarCambios').on('click', function() {
        $('#passwordResetForm').trigger('submit');
    });

    // Envio del formulario
    $('#passwordResetForm').submit(function(e) {
        e.preventDefault();
        // Enviar formulario si es válido

        if (form.valid()) {
            var formulario = document.getElementById('passwordResetForm');
            formulario.submit();
        }
    });

});

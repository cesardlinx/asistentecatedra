$(document).ready(function() {


    /**
     * Form Validation
     */
    var form = $('#profileForm').validate({
        rules: {
            first_name: {
                maxlength: 30,
                minlength: 3,
                alpha: true
            },
            last_name: {
                maxlength: 30,
                minlength: 3,
                alpha: true
            },
            institution: {
                maxlength: 100,
            },

        },
        errorElement: "em",
        wrapper: 'div',
        errorPlacement: errorFeedback,
    });

    $('#guardarCambios').on('click', function(){
        $('#profileForm').trigger('submit');
    });

    // Envio del formulario
    $('#profileForm').submit(function(e) {
        e.preventDefault();
        // Enviar formulario si es válido

        if (form.valid()) {
            var formulario = document.getElementById('profileForm');
            formulario.submit();
        }
    });

});

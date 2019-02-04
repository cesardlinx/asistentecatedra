$(document).ready(function() {

    // CSRF Token for making post ajax requests
    // We add the header X-CSRFToken
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": Cookies.get('csrftoken')
        }
    });

    /**
     * Form Validation
     */
    var form = $('#signUpForm').validate({
        rules: {
            first_name: {
                required: true,
                maxlength: 30,
                minlength: 3,
                alpha: true
            },
            last_name: {
                required: true,
                maxlength: 30,
                minlength: 3,
                alpha: true
            },
            email: {
                required: true,
                email: true,
                remote: {
                    url: "/accounts/ajax/unique_email_validator/",
                    type: "post",
                    data: {
                        'email': function() {
                            return $('#id_email').val();
                        }
                    },
                }
            },
            password1: {
                required: true,
                minlength: 8,
                numbers: true,
                uppercase: true,
                lowercase: true
            },
            password2: {
                required: true,
                equalTo: "#id_password1"
            },
            institution: {
                required: true,
                maxlength: 100,
            },
            terms: {
                required: true
            },
        },
        messages: {
            email: {
                remote: "El email que has escrito ya existe."
            },
            password2: {
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
    $('#signUpForm').submit(function(e) {
        e.preventDefault();
        // Enviar formulario si es válido

        if (form.valid()) {
            var formulario = document.getElementById('signUpForm');
            formulario.submit();
        }
    });

});



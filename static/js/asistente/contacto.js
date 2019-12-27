$(document).ready(function () {

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
  var form = $('#contactForm').validate({
    rules: {
      name: {
        required: true,
        maxlength: 20,
        minlength: 3,
        alpha: true
      },
      email: {
        required: true,
        maxlength: 50,
        email: true,
      },
      subject: {
        required: true,
        maxlength: 20,
        minlength: 3,
        alpha: true
      },
      message: {
        maxlength: 500,
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
  $('#contactForm').submit(function (e) {
    e.preventDefault();
    // Enviar formulario si es válido

    if (form.valid()) {
      var formulario = document.getElementById('contactForm');
      formulario.submit();
    }
  });

});



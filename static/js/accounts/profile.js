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


    // when click on photo open the file loader
    $('#user-photo').on('click', function() {
        $('#id_photo').click();
    });

    // when click on photo open the file loader
    $('#school-logo').on('click', function() {
        $('#id_institution_logo').click();
    });

    $('#id_institution_logo').on('change', function (event) {


        var isFile = event.target.files && event.target.files[0]
        var helpText = '';

        if (isFile) {

            var reader = new FileReader();
            reader.onload = function(e) {
                $('#school-logo').attr('src', e.target.result);
            };
            reader.readAsDataURL(event.target.files[0]);

            helpText = 'Haga click en "Guardar Cambios" para almacenar';
        } else {
            helpText = 'Click en el logo para cargar uno nuevo.';
            $('#school-logo').attr('src', '/static/img/defaults/default-school-logo.png');
        }

        $('p.school-logo-help').text(helpText);
    });

    /* SCRIPT TO OPEN THE MODAL WITH THE PREVIEW */
    $("#id_photo").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#image").attr("src", e.target.result);
                $("#modalCrop").modal("show");
            }
            reader.readAsDataURL(this.files[0]);
        }
    });


    /* SCRIPTS TO HANDLE THE CROPPER BOX */

    var $image = $("#image");
    var cropBoxData;
    var canvasData;
    $("#modalCrop").on("shown.bs.modal", function () {
        $image.cropper({
            viewMode: 1,
            aspectRatio: 1 / 1,
            minCropBoxWidth: 200,
            minCropBoxHeight: 200,
            ready: function () {
                $image.cropper("setCanvasData", canvasData);
                $image.cropper("setCropBoxData", cropBoxData);
            }
        });
    }).on("hidden.bs.modal", function () {
        cropBoxData = $image.cropper("getCropBoxData");
        canvasData = $image.cropper("getCanvasData");
        $image.cropper("destroy");
    });

    // Enable zoom in button
    $(".js-zoom-in").click(function () {
        $image.cropper("zoom", 0.1);
    });

    // Enable zoom out button
    $(".js-zoom-out").click(function () {
        $image.cropper("zoom", -0.1);
    });

    // when click on the button "recortar y cargar"
    // fills the form, hides the modal and submits the data
    $(".js-crop-and-upload").click(function () {
        var cropData = $image.cropper("getData");
        $("#id_x").val(cropData["x"]);
        $("#id_y").val(cropData["y"]);
        $("#id_height").val(cropData["height"]);
        $("#id_width").val(cropData["width"]);
        $('#modalCrop').modal('hide');
        $('#photoForm').submit();
    });

    // Delete account confirmation
    $('#deleteAccount').on('click', function(e) {
        e.preventDefault();
        var message = '¿Está seguro de eliminar su cuenta?. Todos sus datos serán eliminados y no podrá recuperarlos en el futuro.';

        if (confirm(message)) {
            $('#deleteAccountForm').submit();
        }
    });

    // Delete account confirmation
    $('#cancelSubscription').on('click', function(e) {
        e.preventDefault();
        var message = '¿Está seguro de cancelar su subscripción premium?. Recuerde que perderá todos los beneficios.';

        if (confirm(message)) {
            $('#cancelSubscriptionForm').submit();
        }
    });


});

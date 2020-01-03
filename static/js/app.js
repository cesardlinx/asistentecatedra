$(document).ready(function(){
    var menu_open = false;
    var hover = false;
    var primaryColor = '#16a085';
    var secondaryColor = '#2c3e50';
    var white = '#fff';

    // Disables autofocus
    $('input').blur();

    // Menu Button
    $('#menu-button').click(function() {
        // Funcionamiento del botón para abrir el menú
        if (menu_open) {
            $('#menu-button').css('position', 'absolute');
            $(this).removeClass('cross');
            changeMenuColors(white, white, white, primaryColor);
            $('.menu').addClass('is-inactive');
            $('.menu').removeClass('is-active');
            if (hover) {
                changeMenuColors(primaryColor, primaryColor, primaryColor, white);
            }
            menu_open = false;
        } else {
            $('#menu-button').css('position', 'fixed');
            $(this).addClass('cross');
            changeMenuColors(secondaryColor, white, white, secondaryColor);
            $('.menu').show();
            $('.menu').addClass('is-active');
            $('.menu').removeClass('is-inactive');
            menu_open = true;
        }
    });

    $('#menu-button').hover(function () {


        hover = true;
        // hover fix
        if (menu_open) {
            changeMenuColors(secondaryColor, primaryColor, primaryColor, secondaryColor);
        } else {
            changeMenuColors(primaryColor, primaryColor, primaryColor, white);
        }
    }, function () {
        if (menu_open) {
            changeMenuColors(secondaryColor, white, white, secondaryColor);
        } else {
            changeMenuColors(white, white, white, primaryColor);
        }
        hover = false;
    });

    var changeMenuColors = function(barsColor, beforeColor, afterColor, background) {
        $('#menu-button').css('background', background);
        $('.bars').css('background', barsColor);
        $('.bars-before').css('background', beforeColor);
        $('.bars-after').css('background', afterColor);
    }

    $(window).on('resize', function () {
        // Animations fix on resize
        var screenWidth = window.innerWidth

        if (screenWidth >= 976) {
            menu_open = false;
            $('.bars').removeClass('cross');
            $('#menu-button').css('background', primaryColor);
            $('.menu').show();
            $('.menu').removeClass('is-inactive');
            $('.menu').removeClass('is-active');
        } else {
            $('.menu').hide();
        }
    });

    // User Dropdown Menu
    $('.dropdown-container').mouseover(function(){
        var dropdown = $(this).find('.dropdown-menu')
        $(dropdown).addClass('dropdown-active');
        $(dropdown).removeClass('dropdown-inactive');
    });


    $('.dropdown-container').mouseleave(function () {
        var dropdown = $(this).find('.dropdown-menu')
        $(dropdown).addClass('dropdown-inactive');
        $(dropdown).removeClass('dropdown-active');
    });

    /* Forms with floating placeholder */
    // Probar si estan llenos los campos de este tipo al inicio
    setTimeout(function() {
        $('.floating-input').each(function(idx, input){
            testFloatingInput(input); // en useful_functions
        });
    }, 200);


    $('.floating-input').focus(function(){
        $(this).addClass('input-focus');
        $(this).prev().addClass('placeholder-moved');
    });
    $('.floating-input').blur(function () {
        var inputValue = $(this).val();
        if (!inputValue) {
            $(this).removeClass('input-focus');
            $(this).prev().removeClass('placeholder-moved');
        }
    });


    /* Modal */
    $('.modal-opening').click(function(e){
        e.preventDefault()
        var target = $(this).attr('modal-target');

        $(target).addClass('modal-active');
        $(target).removeClass('modal-inactive');

    });

    $('.modal-dismiss').click(function () {
        var target = $(this).parents('.modal-overlay').attr('id');
        target = '#' + target;

        $(target).addClass('modal-inactive');
        $(target).removeClass('modal-active');
    });

    $('.modal-contenido').click(function (e) {
        e.stopPropagation();
    });

    $('.modal-overlay').click(function (e) {
        $(this).addClass('modal-inactive');
    });

});

// Function to test if a floating input has value
// if so, then move the label
var testFloatingInput = function(input) {
    var inputValue = $(input).val();
    if (inputValue) {
        $(input).addClass('input-focus');
        $(input).prev().addClass('placeholder-moved');
    } else {
        $(input).removeClass('input-focus');
        $(input).prev().removeClass('placeholder-moved');
    }
};

// function to make a all textarea in the page autoresizable
// Requires autosize library
var textareaResizables = function() {
    autosize($('textarea'));
    autosize.destroy($('.table-textarea'));
};


var errorFeedback = function(error, element) {
    error.addClass('invalid-feedback');
    error.insertAfter(element);
};

var fieldHighlight = function(element, errorClass, validClass) {
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
};

var fieldUnhighlight = function(element, errorClass, validClass) {
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
};

// function to make a textarea to take the parent height
// inside or out a formset
var updateTextareasSize = function(numeroFila, formsetName, fields) {
    $.each(fields, function(i, field) {
        var textareaElement;
        if (formsetName && numeroFila >= 0) {
            textareaElement = $(`#id_${formsetName}-${numeroFila}-${field}`);
        } else {
            textareaElement = $(`#id_${field}`);
        }
        var cellHeight = textareaElement.parent().height();
        textareaElement.height(cellHeight);
    });
};

var getValueFromMultipleInput = function(type, identifier) {
    if (type === 'checkbox') {
        var inputs = $(`#id_${identifier} li input[type="checkbox"]`);
        var inputsChecked = [];
        inputs.each(function() {
            if (this.checked) {
                inputsChecked.push(this.value)
            }
        });
        return inputsChecked
    } else if (type === 'select') {
        var inputs = $(`.${identifier}`);

        var inputsSelected = [];
        inputs.each(function() {
            inputsSelected.push(this.value);
        });
        return inputsSelected
    }
};





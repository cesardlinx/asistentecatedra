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
}

// function to make a all textarea in the page autoresizable
// Requires autosize library
var textareaResizables = function() {
    autosize($('textarea'));
}

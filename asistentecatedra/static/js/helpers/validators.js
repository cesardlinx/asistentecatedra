// Custom Validators
$.validator.addMethod("alpha", function(value, element) {
    return this.optional(element) || /^[a-zA-ZñÑáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ\s]+$/i.test(value);
}, "Este campo solo permite letras");
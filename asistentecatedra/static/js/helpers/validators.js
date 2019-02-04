// Custom Validators
$.validator.addMethod("numbers", function(value, element) {
    return this.optional(element) || /^.*[0-9].*$/.test(value);
}, "La contraseña debe tener la menos 1 dígito, 0-9.");

$.validator.addMethod("lowercase", function(value, element) {
    return this.optional(element) || /^.*[a-z].*$/.test(value);
}, "La contraseña debe tener la menos 1 letra minúscula, a-z.");

$.validator.addMethod("uppercase", function(value, element) {
    return this.optional(element) || /^.*[A-Z].*$/.test(value);
}, "La contraseña debe tener la menos 1 letra mayúscula, A-Z.");

$.validator.addMethod("alpha", function(value, element) {
    return this.optional(element) || /^[a-zA-ZñÑáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ\s]+$/i.test(value);
}, "Este campo solo permite letras");
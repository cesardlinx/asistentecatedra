(function(global, $){

    // La librería es una función que regresa un objeto de tipo SpecialFields.init
    var SpecialFields = function(config) {
        return new SpecialFields.init(config);
    };

    // Métodos del objeto creado
    SpecialFields.prototype = {
        // Mensaje de error
        errorBlock: function(idField) {
            var errorBlock = `<div class="${this.errorFeedbackClass}">
                                  <em class="error" id="${idField}-error">Este campo es obligatorio.</em>
                              </div>`;
            return errorBlock;
        },
        // Manejo del error
        manageErrorBlock: function(fieldName) {
            // Si el campo no es válido y no hay mensaje de error
            if ($(`#${fieldName}`).attr('isValid') === 'false' && $(`#${fieldName}-error`).length === 0) {
                // Añadir error
                $(`#${fieldName}`).after(this.errorBlock(fieldName)).addClass(this.errorClass);
            // Si el campo no es válido y ya hay mensaje de error no hacer nada
            } else if ($(`#${fieldName}`).attr('isValid') === 'false' && $(`#${fieldName}-error`).length != 0) {}
            // Si el campo es válido remover el error
            else {
                $(`#${fieldName}-error`).parent().remove();
                $(`#${fieldName}`).removeClass(this.errorClass);
            }
        },
        // Añadir evento en inputs para su validación
        addFieldsEvent: function() {

            var self = this;

            $.each(self.fields, function(index, field) {
                if ($(`#${field} option`).length) {
                    var formControl = `#${field}`;
                    var type = 'select'
                } else {
                    var formControl = `#${field} input`;
                    var type = 'checkbox'
                }

                $(`#${self.formId}`).on('change', formControl, (function() {
                    return function() {
                        // Validación y manejo del mensaje de error
                        self.validateField(field, type);
                        self.manageErrorBlock(field);
                    }
                }()));
            });
        },
        // Validación de campos checkbox y select
        validateField: function(fieldName, type='checkbox') {
            var isFieldEmpty = true;

            // Definición de variables dependiendo el tipo de campo
            if (type === 'checkbox') {
                var fieldsList = $(`#${fieldName}`).find('input');

                isFieldEmpty = fieldsList.length === 0;
                var checkedInputs = $(`#${fieldName}`).find('input:checked');
                var isInputEmpty = checkedInputs.length === 0;

            } else if (type === 'select') {
                var optionList = $(`#${fieldName}`).find('option');
                isFieldEmpty = optionList.length === 1;
                var isInputEmpty = $(`#${fieldName}`).val() === "";
            }

            // Validación
            if (isFieldEmpty) {
                $(`#${fieldName}`).attr('isValid', 'false');
                $(`#${fieldName}`).trigger('highlight');
            } else if (!isInputEmpty) {
                $(`#${fieldName}`).attr('isValid', 'true');
                $(`#${fieldName}`).trigger('unhighlight');
            } else {
                $(`#${fieldName}`).attr('isValid', 'false');
                $(`#${fieldName}`).trigger('highlight');
            }

        },
        // Añadir evento en inputs ckeditor para su validación
        addCkeditorEvent: function() {

            var self = this;

            $.each(CKEDITOR.instances, function(index, editor) {
                editor.on('key', (function() {
                    return function() {
                        setTimeout(function() {
                            // Validación y manejo del mensaje de error
                            self.validateCkeditor(editor.name, editor);
                            self.manageErrorBlock(editor.name);
                        }, 10);
                    };
                }()));
            });

        },
        // Validación de campos ckeditor
        validateCkeditor: function(editorName, editor) {
            var text = editor.document.getBody().getChild(0).getText();

            if (text === "\n") {
                // Error
                $(`#${editorName}`).attr('isValid', 'false');
            } else {
                // Remover el error
                $(`#${editorName}`).attr('isValid', 'true');
            }
        },
        // Correr todas las validaciones
        runValidations: function() {
            this.addFieldsEvent();
            if (this.ckeditorValidation) {
                this.addCkeditorEvent();
            }

        },
        // Validar objeto de configuración
        validateFunctionData: function() {
            var self = this;

            if (!$) {
                throw 'jQuery not loaded';
            }

            if (!$.isArray(self.fields)) {
                throw 'fields must be an array';
            }

            if (typeof self.formId != 'string') {
                throw 'formId must be a string';
            }

            if (typeof self.ckeditorValidation != 'boolean') {
                throw 'ckeditorValidation must be a boolean';
            }

            if (typeof self.errorFeedbackClass != 'string') {
                throw 'errorFeedbackClass must be a string';
            }

            if (typeof self.errorClass != 'string') {
                throw 'errorClass must be a string';
            }

            if (typeof self.highlight != 'function') {
                throw 'highlight must be a method';
            }

            if (typeof self.unhighlight != 'function') {
                throw 'unhighlight must be a method';
            }
        },
        // Obtener todos los campos incluidos los del ckeditor de ser necesario
        getAllFields: function() {
            var fields = this.fields;

            if (this.ckeditorValidation) {
                $.each(CKEDITOR.instances, function(editorName) {
                    fields.push(editorName);
                });
            }

            return fields;
        },
        // Método para determinar si todos los campos son válidos
        areValid: function() {
            var fields = this.getAllFields();

            return fields.reduce(function(validState, currentKey) {
                validState = (validState && $(`#${currentKey}`).attr('isValid') === 'true') ? true : false;
                return validState;
            }, true);
        },
        // Método para añadir validación en el submit del formulario
        addSubmitEvent: function() {
            var self = this;

            $(`#${self.formId}`).on('submit', function() {
                // Validación de campos
                $.each(self.fields, function(index, field) {
                    if ($(`#${field} option`).length) {
                        var type = 'select';
                    } else {
                        var type = 'checkbox';
                    }
                    self.validateField(field, type);
                    self.manageErrorBlock(field);
                });

                // Validación de campos ckeditor
                $.each(CKEDITOR.instances, function(index, editor){
                    self.validateCkeditor(editor.name, editor);
                    self.manageErrorBlock(editor.name);
                });

                // fix al bug del jquery validate
                $(`.${self.errorFeedbackClass}`).css('display', 'block');
                $(`.${self.errorFeedbackClass} em`).css('display', 'block');
                $(`.${self.errorFeedbackClass} em`).text('Este campo es obligatorio.');

            });
        },
        // Añadir clase special-fields a campos tratados con esta librería
        addClass: function() {
            var fields = this.getAllFields();

            $.each(fields, function(index, field) {
                $(`#${field}`).addClass('special-field');
            });
        },

        appendErrorEvents() {
            var self = this;
            var fields = self.getAllFields();

            $.each(fields, function(index, field) {

                $(`#${field}`).on('highlight', (function() {
                    return function() {
                        self.highlight($(`#${field}`));
                    }
                }()));

                $(`#${field}`).on('unhighlight', (function() {
                    return function() {
                        self.unhighlight($(`#${field}`));
                    }
                }()));
            });
        },
    }

    // Constructor del objeto special fields
    SpecialFields.init = function(config) {
        var self = this;

        self.fields = config.fields;
        self.formId = config.formId;

        self.ckeditorValidation = config.ckeditorValidation || false;
        self.errorFeedbackClass = config.errorFeedbackClass || 'error-feedback';
        self.errorClass = config.errorClass || 'error';

        // error methods
        self.highlight = config.highlight || function(el){};
        self.unhighlight = config.unhighlight || function(el){};

        self.validateFunctionData();
        self.addClass();
        self.appendErrorEvents();
        self.runValidations();
        self.addSubmitEvent();
    }

    // Se agrega los métodos al objeto principal
    SpecialFields.init.prototype = SpecialFields.prototype;

    // Se agrega la función a window
    global.SpecialFields = SpecialFields;

}(window, jQuery));
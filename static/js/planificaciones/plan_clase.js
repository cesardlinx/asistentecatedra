$(document).ready(function() {

    // All textarea resizables
    textareaResizables();

    var mainTitle = $('.main-title').html();

    // Extra Fields Validation
    var extraFields = SpecialFields({
        fields: [
            'id_cursos'
        ],
        formId: 'planClaseForm'
    });

    // Configuración del datepicker
    var datepicker = $("#id_fecha").datepicker({
        dateFormat: 'yy-mm-dd',
        onClose: function() {
            testFloatingInput(this); // en useful_functions
        }
    });

    // If the datepicker has no value then add actual date
    if (!datepicker.val()) {
        datepicker.datepicker("setDate", new Date());
    }

    // Delete planning confirmation
    $('#deletePlanificacion').on('click', function(e) {
        e.preventDefault();
        var message = '¿Está seguro que desea eliminar esta planificación?';

        if (confirm(message)) {
            $('#deletePlanificacionForm').submit();
        }
    });


    /**
     * Al elegir una asignatura
     * se cargan los cursos
     */
    var cargarCursos = function() {
        var asignaturaId = $('#id_asignatura').val();
        var destrezasOptions = $('.destrezas option')
        var url_cursos = $('#planClaseForm').attr('load-cursos-url');

        $('#id_objetivos').html('<span>Seleccione una asignatura y un curso.</span>');
        $('#id_cursos').html('<span>Seleccione una asignatura</span>');
        $('.destrezas').html('<option>Elija una destreza.</option>');

        if (asignaturaId) {
            $('#id_objetivos').html('<span>Seleccione un curso.</span>');
            $.ajax({
                url: url_cursos,
                data: {
                    'asignatura': asignaturaId
                },
                success: function(data) {
                    $('#id_cursos').html(data);
                    if (destrezasOptions.length > 1) {
                        $('.destrezas').html('<option>Elija una destreza.</option>');
                    }
                }
            });
        }
    };


    $("#id_asignatura").change(cargarCursos);

    /**
     * Al elegir un curso
     * Se cargan los objetivos y destrezas
     */
    $('#planClaseForm').on('change', '#id_cursos input', function(e) {
        // Obtener URLs
        var urlObjetivos = $('#planClaseForm').attr('load-objetivos-url');
        var urlDestrezas = $('#planClaseForm').attr('load-destrezas-url');
        var asignaturaId = $('#id_asignatura').val();

        // Obtiene los cursos seleccionados
        var cursos = $('#id_cursos li input[type="checkbox"]');
        var cursosChecked = [];
        cursos.each(function(){
            if (this.checked) {
                cursosChecked.push(this.value)
            }
        });

        // Cargar objetivos y objetivos generales
        if (asignaturaId) {

            // agregar a la bibliografia
            if (mainTitle === 'Nuevo Plan de Clase' && e.target.checked) {
                var book = '';
                var asignatura = $('#id_asignatura option:selected').text();

                // si hay datos previos borrar
                var editorData = CKEDITOR.instances['id_bibliografia'].getData();
                if (!editorData) {
                    // agregar curriculum a la bibliografia
                    CKEDITOR.instances['id_bibliografia'].insertHtml('<li>Ministerio de Educación (2016) Curriculo, Quito-Ecuador</li>');
                }

                var curso = e.target.nextSibling.nextSibling.textContent.trim();

                // agregar libro de curso a la bibliografia
                book = `Ministerio de Educación (2018) ${asignatura} ${curso} Texto del Estudiante, Quito-Ecuador`;
                CKEDITOR.instances['id_bibliografia'].insertHtml(`<li>${book}</li>`);
            }

            $.ajax({
                url: urlObjetivos,
                data: {
                    'asignatura': asignaturaId,
                    'cursos': cursosChecked
                },
                success: function(data) { // `data` is the return of the `load_objetivos` view function
                    data = JSON.parse(data);
                    objetivos = data.objetivos;
                    objetivosGenerales = data.objetivos_generales;

                    // Si hay objetivos y objetivos generales se los agrega al html
                    if (objetivos) {
                        var listaObjetivos = ''
                        $.each(objetivos, function(i, objetivo) {
                            var template = `<li>
                                                <input class="custom-checkbox" type="checkbox" name="objetivos" value="${objetivo.id}" id="id_objetivos_${i}">
                                                <label class="check-label" for="id_objetivos_${i}">
                                                    ${objetivo.codigo} - ${objetivo.description}
                                                </label>
                                            </li>`
                            listaObjetivos += template;
                        });
                        $('#id_objetivos').html(listaObjetivos)
                    } else {

                        $('#id_objetivos').html('')
                    }

                    if (objetivosGenerales) {
                        var listaObjetivosGenerales = ''
                        $.each(objetivosGenerales, function(i, objetivo) {
                            var templateGenerales = `<li>
                                                        <input class="custom-checkbox" type="checkbox" name="objetivos_generales" value="${objetivo.id}" id="id_objetivos_generales_${objetivo.id}">
                                                        <label class="check-label" for="id_objetivos_generales_${objetivo.id}">
                                                            ${objetivo.codigo} - ${objetivo.description}
                                                        </label>
                                                    </li>`
                            listaObjetivosGenerales += templateGenerales;
                        });
                        $('#id_objetivos_generales').html(listaObjetivosGenerales)
                    } else {
                        $('#id_objetivos_generales').html('')
                    }

                    // Si no hay objetivos ni objetivos generales es porque
                    // se deseleccionó todos los cursos
                    if (!objetivos && !objetivosGenerales) {
                        $('#id_objetivos').html('<span>Seleccione un curso.</span>');
                    }

                }
            });

            // Cargar Destrezas
            $.ajax({
                url: urlDestrezas,
                data: {
                    'asignatura': asignaturaId,
                    'cursos': cursosChecked,
                    'formset_name': 'elementos_curriculares'
                },
                success: function(data) { // `data` is the return of the `load_destrezas` view function
                    $('.destrezas').html(data);
                }
            });
        }
    });


    /**
     * Botón Agregar Destrezas
     */
    $('.formset-buttons').on('click', '#agregar-destreza', function() {

        var idUltimaFila = $('#elementos-curriculares tr:last > td select').attr('id');

        // Busqueda del id de la última fila que contenga el campo select
        var i = 0;
        while (!idUltimaFila) {
            if (i == 0) {
                var anteriorFila = $('#elementos-curriculares tr:last').prev();
                idUltimaFila = anteriorFila.find('select').attr('id');
            } else {
                anteriorFila = anteriorFila.prev()
                idUltimaFila = anteriorFila.find('select').attr('id');
            }
            i++;
        }

        var pattern = /id_elementos_curriculares-(\d+)-destreza/i;
        var numeroFila = parseInt(pattern.exec(idUltimaFila)[1]) + 1;

        var filaDestrezas = `<tr>
                        <td rowspan="1" class="elementos-form">
                            <div class="cell-wrapper-select">
                                <div class="select-wrapper">
                                    <select name="elementos_curriculares-${numeroFila}-destreza" id="id_elementos_curriculares-${numeroFila}-destreza" class="destrezas custom-select">
                                        <option value="" selected="">Elija una destreza.</option>
                                    </select>
                                </div>
                            </div>
                        </td>
                        <td rowspan="1" class="elementos-form">
                            <textarea class="table-textarea textarea-full" name="elementos_curriculares-${numeroFila}-conocimientos_asociados"
                                placeholder="Conocimientos Asociados" maxlength="100"
                                id="id_elementos_curriculares-${numeroFila}-conocimientos_asociados"
                                rows="10" cols="40"></textarea>
                        </td>
                        <input type="hidden" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-TOTAL_FORMS" value="1" id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-TOTAL_FORMS">
                        <input type="hidden" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-INITIAL_FORMS" value="0" id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-INITIAL_FORMS">
                        <input type="hidden" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-MIN_NUM_FORMS" value="0" id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-MIN_NUM_FORMS">
                        <input type="hidden" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-MAX_NUM_FORMS" value="1000" id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-MAX_NUM_FORMS">
                        <td rowspan="1" class="procesos-form procesos">
                            <div class="cell-wrapper-lg">
                                <input type="text" class="table-form-control mb-4" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-0-name"
                                    placeholder="Nombre del Proceso" maxlength="50"
                                    id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-0-name">
                                <textarea class="textarea-proceso" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-0-description"
                                    maxlength="200" placeholder="Descripción" cols="40" rows="10"
                                    id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-0-description"></textarea>
                            </div>
                            <p>
                                <a href="#" class="agregar-proceso" id="agregar-proceso-row${numeroFila}">
                                    <span class="fas fa-plus"></span> Agregar Proceso
                                </a>
                            </p>
                        </td>
                        <td rowspan="1" class="procesos-form procesos">
                            <div class="cell-wrapper-sm">
                                <input type="text" class="table-form-control" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-0-tiempo"
                                    maxlength="10" placeholder="Tiempo"
                                    id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-0-tiempo">
                            </div>
                        </td>
                        <td rowspan="1" class="procesos-form">
                            <textarea class="table-textarea textarea-full" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-0-recursos"
                                maxlength="200" placeholder="Recursos" cols="40" rows="10"
                                id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-0-recursos"></textarea>
                        </td>
                        <td rowspan="1" class="elementos-form">
                            <textarea class="table-textarea textarea-full" name="elementos_curriculares-${numeroFila}-actividades_evaluacion" maxlength="200"
                                placeholder="Actividades de Evaluación" cols="40" rows="10"
                                id="id_elementos_curriculares-${numeroFila}-actividades_evaluacion"></textarea>
                        </td>
                    </tr>`

        $('#elementos-curriculares tbody').append(filaDestrezas);

        // All textarea resizables
        textareaResizables();

        // Append del botón de "eliminar destreza si aún no existe"
        if (!$('#eliminar-destreza').length) {
            var eliminarDestrezaButton = `
                <button class="secondary-button common-btn delete-btn" type="button" id="eliminar-destreza">
                    <span class="fas fa-minus"></span> Eliminar Destreza
                </button>
            `
            $('#agregar-destreza').after(eliminarDestrezaButton);
        }

        // Actualización del campo TOTAL_FORMS del formset de Elementos Curriculares
        var totalElementosForms = parseInt($('#id_elementos_curriculares-TOTAL_FORMS').val());
        $('#id_elementos_curriculares-TOTAL_FORMS').val(totalElementosForms + 1);

        var urlDestrezas = $('#planClaseForm').attr('load-destrezas-url');
        var asignaturaId = $('#id_asignatura').val();
        var cursos = $('#id_cursos li input[type="checkbox"]');
        var cursosChecked = [];

        cursos.each(function() {
            if (this.checked) {
                cursosChecked.push(this.value)
            }
        })

        // Se agrega la lista de destrezas a la nueva fila
        if (asignaturaId && cursosChecked.length) {
            $.ajax({
                url: urlDestrezas,
                data: {
                    'asignatura': asignaturaId,
                    'cursos': cursosChecked
                },
                success: function (data) {   // `data` is the return of the `load_destrezas` view function

                    $(`#id_elementos_curriculares-${numeroFila}-destreza`).html(data);
                }
            });
        }
    });

    /**
     * Botón Eliminar Destreza
     */
    $('.formset-buttons').on('click', '#eliminar-destreza', function() {

        // ultima fila
        var lastRow = $('#elementos-curriculares tr:last td');
        var numberCells = lastRow.length;

        var rowsToBeRemoved = [];
        rowsToBeRemoved.push(lastRow);
        var subRow;

        // Busqueda de filas extras a ser removidas
        while (numberCells === 3) {
            subRow = $('#elementos-curriculares tr:last').prev();
            rowsToBeRemoved.push(subRow);
            numberCells = subRow.length;
        }

        // eliminacion de filas
        rowsToBeRemoved.forEach(function(row) {
            row.remove();
        });

        // Eliminar botón de remover si solo queda un elemento
        if ($('#elementos-curriculares tbody tr:has(td.elementos-form)').length === 1) {
            $(this).remove();
        }

        var totalElementosForms = parseInt($('#id_elementos_curriculares-TOTAL_FORMS').val());
        $('#id_elementos_curriculares-TOTAL_FORMS').val(totalElementosForms - 1);
    });


    /**
     *  Botón Agregar Procesos
     */
    $('#elementos-curriculares').on('click', '.agregar-proceso', function(e) {
        e.preventDefault();

        var fila = $(this).parent().parent().parent();
        var currentRowspan = fila.find('.elementos-form').attr('rowspan');

        // Busqueda del rowspan de la última fila que contenga el formulario de destrezas
        var i = 0;
        while (!currentRowspan) {
            if (i == 0) {
                var anteriorFila = fila.prev();
                currentRowspan = anteriorFila.find('.elementos-form').attr('rowspan');
            } else if (i > 100) {
                break;
            } else {
                anteriorFila = anteriorFila.prev();
                currentRowspan = anteriorFila.find('.elementos-form').attr('rowspan');
            }
            i++;
        }


        // Actualización del rowspan de celdas
        if (anteriorFila) {
            anteriorFila.find('.elementos-form').attr('rowspan', `${parseInt(currentRowspan) + 1}`);
            var numeroFila = getNumeroFila(anteriorFila);
        } else {
            $(fila).find('.elementos-form').attr('rowspan', `${parseInt(currentRowspan) + 1}`);
            var numeroFila = getNumeroFila(fila);
        }
        var numeroProceso = getNumeroProceso(fila);

        // Elimina botones de "agregar proceso" y "eliminar proceso" del proceso actual
        $(this).remove();
        $(`#eliminar-proceso-row${numeroFila}`).remove();

        procesoHtml = `
            <tr>
                <td rowspan="1" class="procesos-form procesos">
                    <div class="cell-wrapper-lg">
                        <input type="text" class="table-form-control mb-4" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-${numeroProceso}-name"
                                    placeholder="Nombre del Proceso" maxlength="50"
                                    id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-${numeroProceso}-name">
                        <textarea class="textarea-proceso" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-${numeroProceso}-description"
                            maxlength="200" placeholder="Descripción" cols="40" rows="10"
                            id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-${numeroProceso}-description"></textarea>
                    </div>
                    <p>
                        <a href="#" class="agregar-proceso" id="agregar-proceso-row${numeroFila}">
                            <span class="fas fa-plus"></span> Agregar Proceso
                        </a>
                    </p>
                    <p>
                        <a href="#" class="eliminar-proceso" id="eliminar-proceso-row${numeroFila}">
                            <span class="fas fa-minus"></span> Eliminar Proceso
                        </a>
                    </p>
                </td>
                <td rowspan="1" class="procesos-form procesos">
                    <div class="cell-wrapper-sm">
                        <input type="text" class="table-form-control" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-${numeroProceso}-tiempo"
                                    maxlength="10" placeholder="Tiempo"
                                    id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-${numeroProceso}-tiempo">
                    </div>
                </td>
                <td rowspan="1" class="procesos-form">
                    <textarea class="table-textarea textarea-full" name="proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-${numeroProceso}-recursos"
                        maxlength="200" placeholder="Recursos" cols="40" rows="10"
                        id="id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-${numeroProceso}-recursos"></textarea>
                </td>
            </tr>
        `;
        fila.after(procesoHtml);

        // Resizables textarea
        textareaResizables();

        // Suma 1 al valor actual del campo TOTAL_FORMS del formset de elementos curriculares
        var totalProcesosForms = parseInt($(`#id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-TOTAL_FORMS`).val());
        $(`#id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-TOTAL_FORMS`).val(totalProcesosForms + 1);

        // Reparar tamaño del anterior textarea de proceso y los demas textareas
        var formsetName = `proceso-elementos_curriculares-${numeroFila}-procesos_didacticos`;
        updateTextareasSize(numeroProceso - 1, formsetName, ['recursos']);
        updateTextareasSize(numeroFila, 'elementos_curriculares', ['conocimientos_asociados', 'actividades_evaluacion']);
    });

    /**
     * Botón Eliminar Procesos
     */
    $('#elementos-curriculares').on('click', '.eliminar-proceso', function(e) {
        e.preventDefault();
        var fila = $(this).parent().parent().parent();
        var currentRowspan = fila.find('.elementos-form').attr('rowspan');

        // Busqueda del rowspan de la última fila que contenga el formulario de destrezas
        var i = 0;

        while (!currentRowspan) {
            if (i == 0) {
                var anteriorFila = fila.prev();
                currentRowspan = anteriorFila.find('.elementos-form').attr('rowspan');
            } else if (i > 100) {
               break;
            } else {
                anteriorFila = anteriorFila.prev();
                currentRowspan = anteriorFila.find('.elementos-form').attr('rowspan');
            }
            i++;
        }

        if (anteriorFila) {
            anteriorFila.find('.elementos-form').attr('rowspan', `${parseInt(currentRowspan) - 1}`);
            var numeroFila = getNumeroFila(anteriorFila);
        } else {
            fila.find('.elementos-form').attr('rowspan', `${parseInt(currentRowspan) - 1}`);
            var numeroFila = getNumeroFila(fila);
        }

        // Botones de agregar y eliminar proceso
        if (fila.find('.agregar-proceso').length) {
            var numeroProceso = getNumeroProceso(fila);

            if (numeroProceso <= 2) {
                var botonesProcesoHtml = `
                    <p>
                        <a href="#" class="agregar-proceso" id="agregar-proceso-row${numeroFila}">
                            <span class="fas fa-plus"></span> Agregar Proceso
                        </a>
                    </p>
                `
            } else {
                var botonesProcesoHtml = `
                    <p>
                        <a href="#" class="agregar-proceso" id="agregar-proceso-row${numeroFila}">
                            <span class="fas fa-plus"></span> Agregar Proceso
                        </a>
                    </p>
                    <p>
                        <a href="#" class="eliminar-proceso" id="eliminar-proceso-row${numeroFila}">
                            <span class="fas fa-minus"></span> Eliminar Proceso
                        </a>
                    </p>
                `
            }

            // Se agrega los botones de 'agregar proceso' y 'eliminar proceso' al proceso anterior
            fila.prev().find('textarea[placeholder="Descripción"]').parent().after(botonesProcesoHtml);
        }

        // Eliminación del proceso
        fila.remove();

        // Actualización del campo TOTAL_FORMS del formset de procesos
        var totalProcesosForms = parseInt($(`#id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-TOTAL_FORMS`).val());
        $(`#id_proceso-elementos_curriculares-${numeroFila}-procesos_didacticos-TOTAL_FORMS`).val(totalProcesosForms - 1);

        // Reparar tamaño de los demas textareas
        var formsetName = `proceso-elementos_curriculares-${numeroFila}-procesos_didacticos`;
        updateTextareasSize(numeroFila, 'elementos_curriculares', ['conocimientos_asociados', 'actividades_evaluacion']);
    });

    /**
     * Helper Functions
     */
    var getNumeroFila = function(fila) {
        var idFila = fila.find('select').attr('id');
        var pattern = /id_elementos_curriculares-(\d+)-destreza/i;
        var numeroFila = parseInt(pattern.exec(idFila)[1]);
        return numeroFila;
    }

    var getNumeroProceso = function(fila) {
        var idUltimaFila = fila.find('input[type="text"]').attr('id');
        var pattern = /id_proceso-elementos_curriculares-(\d+)-procesos_didacticos-(\d+)-name/i;
        var numeroProceso = pattern.exec(idUltimaFila)[2];
        return parseInt(numeroProceso) + 1;
    }

});

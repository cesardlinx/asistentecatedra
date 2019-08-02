$(document).ready(function() {

    // All textarea resizables
    textareaResizables();

    var mainTitle = $('.main-title').html();

    var ejesTransversales = 'La interculturalidad.\nLa formación de una ciudadanía democrática.\nLa protección del medio ambiente.\nEl cuidado de la salud.\nLos hábitos de recreación de los estudiantes.\nLa educación sexual en los jóvenes.';

    // Agregar ejes transversales solo si es un nuevo plan anual
    if (mainTitle === 'Nuevo Plan Anual') {
        $('#id_ejes_transversales').text(ejesTransversales);
    }

    /**
     * Al elegir una asignatura
     * se cargan los cursos y los objetivos de area
     */
    var cargarCursos = function() {
        var asignaturaId = $('#id_asignatura').val();
        var url_cursos = $('#planAnualForm').attr('load-cursos-url');
        var urlObjetivosArea = $('#planAnualForm').attr('load-objetivos-area-url');

        $('#id_curso').html('<option>Elija un curso.</option>');
        $('#id_objetivos_generales').html('<span>Seleccione una asignatura.</span>');
        clearFields();

        if (asignaturaId) {
            $.ajax({
                url: url_cursos,
                data: {
                    'asignatura': asignaturaId
                },
                success: function(data) {
                    $('#id_curso').html(data);
                }
            });

            // Objetivos de area
            $.ajax({
                url: urlObjetivosArea,
                data: {
                    'asignatura': asignaturaId,
                },
                success: function(data) { // `data` is the return of the `load_objetivos` view function
                    data = JSON.parse(data);
                    objetivosGenerales = data.objetivos_generales;

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
                }
            });
        }
    };


    $("#id_asignatura").change(cargarCursos);

    /**
     * Al elegir un curso
     * Se cargan los objetivos y las unidades
     */
    $('#planAnualForm').on('change', '#id_curso', function(e) {
        // Obtener URLs
        var urlObjetivos = $('#planAnualForm').attr('load-objetivos-url');
        var urlUnidades = $('#planAnualForm').attr('load-unidades-url');

        var asignaturaId = $('#id_asignatura').val();
        var cursoId = $('#id_curso').val();

        clearFields();

        // Cargar objetivos y objetivos generales
        if (asignaturaId && cursoId) {

            // agregar a la bibliografia
            if (mainTitle === 'Nuevo Plan Anual') {
                var book = '';
                var asignatura = $('#id_asignatura option:selected').text();
                var curso = $('#id_curso option:selected').text();

                if (curso !== 'Elija un curso.') {
                    // agregar libros a la bibliografia
                    var curriculo = 'Ministerio de Educación (2016) Curriculo, Quito-Ecuador';
                    book = `Ministerio de Educación (2018) ${asignatura} ${curso} Texto del Estudiante, Quito-Ecuador`;
                    CKEDITOR.instances['id_bibliografia'].setData(`<li>${book}</li><li>${curriculo}</li>`);
                }

            }

            $.ajax({
                url: urlObjetivos,
                data: {
                    'asignatura': asignaturaId,
                    'curso': cursoId
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
                                                <input class="custom-checkbox" type="checkbox" name="objetivos_curso" value="${objetivo.id}" id="id_objetivos_curso_${i}">
                                                <label class="check-label" for="id_objetivos_curso_${i}">
                                                    ${objetivo.codigo} - ${objetivo.description}
                                                </label>
                                            </li>`
                            listaObjetivos += template;
                        });
                        $('#id_objetivos_curso').html(listaObjetivos)
                    } else {

                        $('#id_objetivos_curso').html('')
                    }

                    if (objetivosGenerales) {
                        var listaObjetivosGenerales = ''
                        $.each(objetivosGenerales, function(i, objetivo) {
                            var templateGenerales = `<li>
                                                        <input class="custom-checkbox" type="checkbox" name="objetivos_generales_curso" value="${objetivo.id}" id="id_objetivos_generales_curso_${objetivo.id}">
                                                        <label class="check-label" for="id_objetivos_generales_curso_${objetivo.id}">
                                                            ${objetivo.codigo} - ${objetivo.description}
                                                        </label>
                                                    </li>`
                            listaObjetivosGenerales += templateGenerales;
                        });
                        $('#id_objetivos_generales_curso').html(listaObjetivosGenerales)
                    } else {
                        $('#id_objetivos_generales_curso').html('')
                    }
                }
            });

            // Cargar Unidades
            $.ajax({
                url: urlUnidades,
                data: {
                    'asignatura': asignaturaId,
                    'curso': cursoId
                },
                success: function(data) { // `data` is the return of the `load_destrezas` view function
                    $('.unidades').html(data);
                }
            });

        }
    });

    /**
     * Al elegir una unidad
     * Se cargan los objetivos de la unidad y las destrezas
     */
    $('#planAnualForm').on('change', '.unidades', function() {
        // Obtener URL
        var urlObjetivosUnidad = $('#planAnualForm').attr('load-objetivos-unidad-url');
        var urlDestrezas = $('#planAnualForm').attr('load-destrezas-url');

        var idUnidades = $(this).attr('id');
        var pattern = /(id_desarrollo_unidades-(\d+)-)unidad/i
        var nameObjetivos = pattern.exec(idUnidades)[1] + 'objetivos'
        var nameObjetivosGenerales = pattern.exec(idUnidades)[1] + 'objetivos_generales';
        var nameDestrezas = pattern.exec(idUnidades)[1] + 'destrezas';
        var numeroFila = pattern.exec(idUnidades)[2];

        var unidadId = $(`#${idUnidades}`).val();
        var asignaturaId = $('#id_asignatura').val();
        var cursoId = $('#id_curso').val();

        $(`#${nameObjetivos}`).html('')
        $(`#${nameObjetivosGenerales}`).html('')
        $(`#${nameDestrezas}`).html('');

        if (unidadId) {
            // cargar objetivos de unidad
            $.ajax({
                url: urlObjetivosUnidad,
                data: {
                    'unidad': unidadId,
                },
                success: function(data) {
                    data = JSON.parse(data);
                    objetivos = data.objetivos;
                    objetivosGenerales = data.objetivos_generales;

                    // Si hay objetivos y objetivos generales se los agrega al html
                    if (objetivos) {
                        var listaObjetivos = ''
                        $.each(objetivos, function(i, objetivo) {
                            var template = `<li>
                                            <input class="custom-checkbox"
                                                type="checkbox"
                                                name="desarrollo_unidades-${numeroFila}-objetivos"
                                                value="${objetivo.id}"
                                                id="${nameObjetivos}_${i}" >
                                            <label class="check-label"
                                                for="${nameObjetivos}_${i}" >
                                                ${objetivo.codigo} - ${objetivo.description}
                                            </label>
                                        </li>`
                            listaObjetivos += template;
                        });
                        $(`#${nameObjetivos}`).html(listaObjetivos)
                        updateTextareas(numeroFila);
                    }

                    if (objetivosGenerales) {
                        var listaObjetivosGenerales = ''
                        $.each(objetivosGenerales, function(i, objetivo) {
                            var templateGenerales = `<li>
                                                    <input class="custom-checkbox"
                                                        type="checkbox"
                                                        name="desarrollo_unidades-${numeroFila}-objetivos_generales"
                                                        value="${objetivo.id}"
                                                        id="${nameObjetivosGenerales}_${i}" >
                                                    <label class="check-label"
                                                        for="${nameObjetivosGenerales}_${i}" >
                                                        ${objetivo.codigo} - ${objetivo.description}
                                                    </label>
                                                </li>`
                            listaObjetivosGenerales += templateGenerales;
                        });
                        $(`#${nameObjetivosGenerales}`).html(listaObjetivosGenerales)
                        updateTextareas(numeroFila);
                    }
                }
            });

            if (asignaturaId && cursoId) {
                // Cargar Destrezas
                $.ajax({
                    url: urlDestrezas,
                    data: {
                        'asignatura': asignaturaId,
                        'curso': cursoId,
                        'numero_fila': numeroFila,
                        'formset_name': 'desarrollo_unidades'
                    },
                    success: function(data) { // `data` is the return of the `load_destrezas` view function
                        $(`#${nameDestrezas}`).html(data);
                        updateTextareas(numeroFila);
                    }
                });
            }
        }
    });


    /**
     * Botón Agregar Unidad
     */
    $('.formset-buttons').on('click', '#agregar-unidad', function() {

        var idLastRow = $('#desarrollo-unidades tr:last > td select').attr('id');

        // Busqueda del id de la última fila que contenga el campo select
        var i = 0;
        while (!idLastRow) {
            if (i == 0) {
                var previousRow = $('#desarrollo-unidades tr:last').prev();
                idLastRow = previousRow.find('select').attr('id');
            } else {
                previousRow = previousRow.prev()
                idLastRow = previousRow.find('select').attr('id');
            }
            i++;
        }

        var pattern = /id_desarrollo_unidades-(\d+)-unidad/i;
        var rowNumber = parseInt(pattern.exec(idLastRow)[1]) + 1;

        var newRow = `<tr>
                        <td>
                            <div class="select-wrapper">
                                <select name="desarrollo_unidades-${rowNumber}-unidad" id="id_desarrollo_unidades-${rowNumber}-unidad" class="custom-select unidades">
                                    <option value="" selected="">Elija una unidad.</option>
                                </select>
                            </div>
                        </td>

                        <td class="checklist objetivos">
                            <ul id="id_desarrollo_unidades-${rowNumber}-objetivos"></ul>
                            <ul id="id_desarrollo_unidades-${rowNumber}-objetivos_generales"></ul>
                        </td>

                        <td class="checklist destrezas">
                            <ul id="id_desarrollo_unidades-${rowNumber}-destrezas"></ul>
                        </td>

                        <td>
                            <textarea name="desarrollo_unidades-${rowNumber}-orientaciones_metodologicas"
                            placeholder="Orientaciones Metodológicas"
                            id="id_desarrollo_unidades-${rowNumber}-orientaciones_metodologicas"
                            class="table-textarea textarea-full"></textarea>
                        </td>

                        <td>
                            <div class="cell-wrapper-select">
                                <div class="form-group-float">
                                    <select name="desarrollo_unidades-${rowNumber}-semanas" id="id_desarrollo_unidades-0-semanas" class="form-control floating-input input-focus">
                                        <option value="1" selected="">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                    </select>
                                </div>
                            </div>
                        </td>
                    </tr>`;

        $('#desarrollo-unidades tbody').append(newRow);

        // All textarea resizables
        textareaResizables();

        // Append del botón de "eliminar unidad si aún no existe"
        if (!$('#eliminar-unidad').length) {
            var eliminarUnidadButton = `
                <button class="secondary-button common-btn delete-btn" type="button" id="eliminar-unidad">
                    <span class="fas fa-minus"></span> Eliminar Unidad
                </button>
            `
            $('#agregar-unidad').after(eliminarUnidadButton);
        }

        // Actualización del campo TOTAL_FORMS del formset de Desarrollo de unidades
        var totalUnidadesForms = parseInt($('#id_desarrollo_unidades-TOTAL_FORMS').val());
        $('#id_desarrollo_unidades-TOTAL_FORMS').val(totalUnidadesForms + 1);

        var asignaturaId = $('#id_asignatura').val();
        var cursoId = $('#id_curso').val();
        var urlUnidades = $('#planAnualForm').attr('load-unidades-url');

        // Se agrega la lista de unidades a la nueva fila
        if (asignaturaId && cursoId) {
            // Cargar Unidades
            $.ajax({
                url: urlUnidades,
                data: {
                    'asignatura': asignaturaId,
                    'curso': cursoId
                },
                success: function (data) { // `data` is the return of the `load_destrezas` view function
                    $(`#id_desarrollo_unidades-${rowNumber}-unidad`).html(data);
                }
            });
        }
    });

    /**
     * Botón Eliminar Unidad
     */
    $('.formset-buttons').on('click', '#eliminar-unidad', function() {
        $('#desarrollo-unidades tr:last').remove()

        // Eliminar botón de remover si solo queda un elemento
        if ($('#desarrollo-unidades tbody tr').length === 1) {
            $(this).remove();
        }

        var totalUnidadesForms = parseInt($('#id_desarrollo_unidades-TOTAL_FORMS').val());
        $('#id_desarrollo_unidades-TOTAL_FORMS').val(totalUnidadesForms - 1);
    });


    /**
     * Helper Functions
     */
    var clearFields = function() {
        $('.objetivos ul').html('');
        $('.destrezas ul').html('');
        $('.unidades').html('<option>Elija una unidad didáctica.</option>');
        $('#id_objetivos_curso').html('<span>Seleccione una asignatura y un curso.</span>');
        $('#id_objetivos_generales_curso').html('');
    };

    var updateTextareas = function(numeroFila) {
        updateTextareasSize(numeroFila, 'desarrollo_unidades', ['orientaciones_metodologicas']);
    };

});

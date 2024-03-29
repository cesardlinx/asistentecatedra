$(document).ready(function() {

    // All textarea resizables
    textareaResizables();

    /**
     * Al elegir una asignatura
     * se cargan los cursos
     */
    var cargarCursos = function() {
        var asignaturaId = $('#id_asignatura').val();
        var url_cursos = $('#planUnidadForm').attr('load-cursos-url');

        $('#id_curso').html('<option>Elija un curso.</option>');
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
        }
    };


    $("#id_asignatura").change(cargarCursos);

    /**
     * Al elegir un curso
     * Se cargan las unidades y las destrezas de la primera fila
     */
    $('#planUnidadForm').on('change', '#id_curso', function() {
        // Obtener URLs
        var urlUnidades = $('#planUnidadForm').attr('load-unidades-url');
        var urlDestrezas = $('#planUnidadForm').attr('load-destrezas-url');

        var asignaturaId = $('#id_asignatura').val();
        var cursoId = $('#id_curso').val();

        clearFields();

        // Cargar objetivos y objetivos generales
        if (asignaturaId && cursoId) {

            // Cargar Unidades
            $.ajax({
                url: urlUnidades,
                data: {
                    'asignatura': asignaturaId,
                    'curso': cursoId
                },
                success: function(data) { // `data` is the return of the `load_destrezas` view function
                    $('#id_unidad').html(data);
                }
            });

            var totalUnidadesForms = parseInt($('#id_actividades_aprendizaje-TOTAL_FORMS').val());

            for (let i = 0; i < totalUnidadesForms; i++) {
                // Cargar Destrezas
                $.ajax({
                    url: urlDestrezas,
                    data: {
                        'asignatura': asignaturaId,
                        'curso': cursoId,
                        'numero_fila': i,
                        'formset_name': 'actividades_aprendizaje'
                    },
                    success: function(data) { // `data` is the return of the `load_destrezas` view function
                        $(`#id_actividades_aprendizaje-${i}-destrezas`).html(data);
                        updateTextareas(i);
                    }
                });
            }
        }
    });

    /**
     * Al elegir una unidad
     * Se cargan los objetivos de la unidad
     */
    $('#planUnidadForm').on('change', '#id_unidad', function() {
        // Obtener URL
        var urlObjetivosUnidad = $('#planUnidadForm').attr('load-objetivos-url');
        var unidadId = $('#id_unidad').val();


        $('#id_objetivos').html('<span>Seleccione una asignatura, un curso y una unidad.</span>');
        $('#id_objetivos_generales').html('');

        if (unidadId) {
            // cargar objetivos de unidad
            $.ajax({
                url: urlObjetivosUnidad,
                data: {
                    'unidad': unidadId,
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
                }
            });
        }
    });

    /**
     * Botón Agregar Actividad de Aprendizaje
     */
    $('.formset-buttons').on('click', '#agregar-actividad', function() {

        var idLastRow = $('#actividades-aprendizaje tr:last > td textarea').attr('id');

        var pattern = /id_actividades_aprendizaje-(\d+)-estrategias_metodologicas/i;
        var rowNumber = parseInt(pattern.exec(idLastRow)[1]) + 1;

        var newRow = `<tr>
                        <td class="checklist destrezas">
                            <ul id="id_actividades_aprendizaje-${rowNumber}-destrezas"></ul>
                        </td>

                        <td>
                            <textarea name="actividades_aprendizaje-${rowNumber}-estrategias_metodologicas"
                            id="id_actividades_aprendizaje-${rowNumber}-estrategias_metodologicas"
                            class="table-textarea textarea-full"
                            placeholder="Estrategias Metodológicas"></textarea>
                        </td>

                        <td>
                            <textarea name="actividades_aprendizaje-${rowNumber}-recursos"
                            id="id_actividades_aprendizaje-${rowNumber}-recursos"
                            class="table-textarea textarea-full"
                            placeholder="Recursos"></textarea>
                        </td>

                        <td>
                            <textarea name="actividades_aprendizaje-${rowNumber}-instrumentos_evaluacion"
                            id="id_actividades_aprendizaje-${rowNumber}-instrumentos_evaluacion"
                            class="table-textarea textarea-full"
                            placeholder="Técnicas e Instrumentos de Evaluación"></textarea>
                        </td>
                    </tr>`;

        $('#actividades-aprendizaje tbody').append(newRow);

        // All textarea resizables
        textareaResizables();

        // Append del botón de "eliminar unidad si aún no existe"
        if (!$('#eliminar-actividad').length) {
            var eliminarActividadButton = `
                <button class="secondary-button common-btn delete-btn" type="button" id="eliminar-actividad">
                    <span class="fas fa-minus"></span> Eliminar Actividad
                </button>
            `
            $('#agregar-actividad').after(eliminarActividadButton);
        }

        // Actualización del campo TOTAL_FORMS del formset de Desarrollo de unidades
        var totalUnidadesForms = parseInt($('#id_actividades_aprendizaje-TOTAL_FORMS').val());
        $('#id_actividades_aprendizaje-TOTAL_FORMS').val(totalUnidadesForms + 1);

        var asignaturaId = $('#id_asignatura').val();
        var cursoId = $('#id_curso').val();
        var urlDestrezas = $('#planUnidadForm').attr('load-destrezas-url');

        // Se agrega la lista de unidades a la nueva fila
        if (asignaturaId && cursoId) {
            // Cargar Destrezas
            $.ajax({
                url: urlDestrezas,
                data: {
                    'asignatura': asignaturaId,
                    'curso': cursoId,
                    'numero_fila': rowNumber,
                    'formset_name': 'actividades_aprendizaje'
                },
                success: function(data) { // `data` is the return of the `load_destrezas` view function
                    $(`#id_actividades_aprendizaje-${rowNumber}-destrezas`).html(data);
                    updateTextareas(rowNumber);
                }
            });

        }
    });

    /**
     * Botón Eliminar Actividad de Aprendizaje
     */
    $('.formset-buttons').on('click', '#eliminar-actividad', function() {
        $('#actividades-aprendizaje tr:last').remove()

        // Eliminar botón de remover si solo queda un elemento
        if ($('#actividades-aprendizaje tbody tr').length === 1) {
            $(this).remove();
        }

        var totalActividadesForms = parseInt($('#id_actividades_aprendizaje-TOTAL_FORMS').val());
        $('#id_actividades_aprendizaje-TOTAL_FORMS').val(totalActividadesForms - 1);
    });

    /**
     * Helper Functions
     */
    var clearFields = function() {
        $('#id_unidad').html('<option>Elija una unidad didáctica.</option>');
        $('#id_objetivos').html('<span>Seleccione una asignatura, un curso y una unidad.</span>');
        $('.destrezas ul').html('<span>Seleccione una asignatura y un curso.</span>');
        $('#id_objetivos_generales').html('');
    }

    var updateTextareas = function(numeroFila) {
        var fields = ['estrategias_metodologicas', 'recursos', 'instrumentos_evaluacion'];
        updateTextareasSize(numeroFila, 'actividades_aprendizaje', fields);
    };
});

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
        $('#id_unidad').html('<option>Elija una unidad didáctica.</option>');
        $('#id_objetivos').html('<span>Seleccione una asignatura, un curso y una unidad.</span>');
        $('#id_objetivos_generales').html('<span>Seleccione una asignatura, un curso y una unidad.</span>');

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

        $('#id_unidad').html('<option>Elija una unidad didáctica.</option>');
        $('#id_objetivos').html('<span>Seleccione una asignatura, un curso y una unidad.</span>');
        $('#id_objetivos_generales').html('<span>Seleccione una asignatura, un curso y una unidad.</span>');

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

            // Cargar Destrezas
            $.ajax({
                url: urlDestrezas,
                data: {
                    'asignatura': asignaturaId,
                    'curso': cursoId,
                    'numero_fila': 0
                },
                success: function(data) { // `data` is the return of the `load_destrezas` view function
                    $('#id_actividades_aprendizaje-0-destrezas').html(data);
                }
            });
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
        $('#id_objetivos_generales').html('<span>Seleccione una asignatura, un curso y una unidad.</span>');

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
     * Al elegir las destrezas
     * Se cargan los criterios
     */
    $('#planUnidadForm').on('change', '.destrezas input', function() {
        // Obtener URL
        var urlCriterios = $('#planUnidadForm').attr('load-criterios-url');

        var idDestrezas = $(this).attr('id');

        var pattern = /(id_actividades_aprendizaje-(\d+)-)destrezas/i;
        var idCriterios = pattern.exec(idDestrezas)[1] + 'criterios_evaluacion';
        var numeroFila = pattern.exec(idDestrezas)[2];

        // Obtiene las destrezas seleccionados
        var destrezas = $(`#id_actividades_aprendizaje-${numeroFila}-destrezas li input[type="checkbox"]`);
        var destrezasChecked = [];
        destrezas.each(function() {
            if (this.checked) {
                destrezasChecked.push(this.value)
            }
        })

        $.ajax({
            url: urlCriterios,
            data: {
                'destrezas': destrezasChecked,
                'numero_fila': numeroFila,
                'formset_name': 'actividades_aprendizaje'
            },
            success: function(data) {
                $(`#${idCriterios}`).html(data);
            }
        });
    });

    /**
     * Al elegir los criterios
     * Se cargan los indicadores
     */
    $('#planUnidadForm').on('change', '.criterios input', function() {
        // Obtener URL
        var urlIndicadores = $('#planUnidadForm').attr('load-indicadores-url');

        var idCriterios = $(this).attr('id');
        var pattern = /(id_actividades_aprendizaje-(\d+)-)criterios/i;
        var idIndicadores = pattern.exec(idCriterios)[1] + 'indicadores';
        var numeroFila = pattern.exec(idCriterios)[2];

        // Obtiene las criterios seleccionados
        var criterios = $(`#id_actividades_aprendizaje-${numeroFila}-criterios_evaluacion li input[type="checkbox"]`);
        var criteriosChecked = [];
        criterios.each(function() {
            if (this.checked) {
                criteriosChecked.push(this.value)
            }
        })

        $.ajax({
            url: urlIndicadores,
            data: {
                'criterios': criteriosChecked,
                'numero_fila': numeroFila,
            },
            success: function(data) {
                $(`#${idIndicadores}`).html(data);
            }
        });
    });


    /**
     * Botón Agregar Actividad de Aprendizaje
     */
    $('.formset-buttons').on('click', '#agregar-actividad', function() {

        var idLastRow = $('#actividades-aprendizaje tr:last > td textarea').attr('id');

        // Busqueda del id de la última fila que contenga el campo select
        // var i = 0;
        // while (!idLastRow) {
        //     if (i == 0) {
        //         var previousRow = $('#actividades-aprendizaje tr:last').prev();
        //         idLastRow = previousRow.find('select').attr('id');
        //     } else {
        //         previousRow = previousRow.prev()
        //         idLastRow = previousRow.find('select').attr('id');
        //     }
        //     i++;
        // }

        var pattern = /id_actividades_aprendizaje-(\d+)-estrategias_metodologicas/i;
        var rowNumber = parseInt(pattern.exec(idLastRow)[1]) + 1;

        var newRow = `<tr>
                        <td class="checklist destrezas">
                            <ul id="id_actividades_aprendizaje-${rowNumber}-destrezas"></ul>
                        </td>

                        <td class="checklist criterios">
                            <ul id="id_actividades_aprendizaje-${rowNumber}-criterios_evaluacion"></ul>
                        </td>

                        <td>
                            <div class="cell-wrapper-lg">
                                <textarea name="actividades_aprendizaje-${rowNumber}-estrategias_metodologicas" maxlength="600" id="id_actividades_aprendizaje-${rowNumber}-estrategias_metodologicas" class="table-textarea textarea-full" placeholder="Estrategias Metodológicas" cols="40" rows="10" style="overflow: hidden; overflow-wrap: break-word; resize: none; height: 200px;"></textarea>
                            </div>
                        </td>

                        <td>
                            <div class="cell-wrapper-lg">
                                <textarea name="actividades_aprendizaje-${rowNumber}-recursos" maxlength="400" id="id_actividades_aprendizaje-0-recursos" class="table-textarea textarea-full" placeholder="Recursos" cols="40" rows="10" style="overflow: hidden; overflow-wrap: break-word; resize: none; height: 200px;"></textarea>
                            </div>
                        </td>

                        <td class="checklist">
                            <ul id="id_actividades_aprendizaje-${rowNumber}-indicadores"></ul>
                        </td>

                        <td>
                            <div class="cell-wrapper-lg">
                                <textarea name="actividades_aprendizaje-${rowNumber}-instrumentos_evaluacion" maxlength="600" id="id_actividades_aprendizaje-${rowNumber}-instrumentos_evaluacion" class="table-textarea textarea-full" placeholder="Técnicas e Instrumentos de Evaluación" cols="40" rows="10" style="overflow: hidden; overflow-wrap: break-word; resize: none; height: 200px;"></textarea>
                            </div>
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
                    'numero_fila': rowNumber
                },
                success: function(data) { // `data` is the return of the `load_destrezas` view function
                    $(`#id_actividades_aprendizaje-${rowNumber}-destrezas`).html(data);
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

});

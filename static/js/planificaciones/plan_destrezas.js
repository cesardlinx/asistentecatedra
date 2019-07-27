$(document).ready(function() {

    // All textarea resizables
    textareaResizables();

    // fix ejes transversales textarea width
    $('#id_ejes_transversales').width('87%');

    var mainTitle = $('.main-title').html();
    var ejesTransversales = 'La interculturalidad.\nLa formación de una ciudadanía democrática.\nLa protección del medio ambiente.\nEl cuidado de la salud.\nLos hábitos de recreación de los estudiantes.\nLa educación sexual en los jóvenes.';

    // Agregar ejes transversales solo si es un nuevo plan anual
    if (mainTitle === 'Nuevo Plan de Destrezas') {
        $('#id_ejes_transversales').text(ejesTransversales);
    }

    /**
     * Al elegir una asignatura
     * se cargan los cursos
     */
    var cargarCursos = function() {
        var asignaturaId = $('#id_asignatura').val();
        var url_cursos = $('#planDestrezasForm').attr('load-cursos-url');

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
    $('#planDestrezasForm').on('change', '#id_curso', function() {
        // Obtener URLs
        var urlUnidades = $('#planDestrezasForm').attr('load-unidades-url');
        var urlDestrezas = $('#planDestrezasForm').attr('load-destrezas-url');

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

            // Cargar Destrezas
            $.ajax({
                url: urlDestrezas,
                data: {
                    'asignatura': asignaturaId,
                    'curso': cursoId,
                },
                success: function(data) { // `data` is the return of the `load_destrezas` view function
                    $('#id_destrezas').html(data);
                }
            });
        }
    });

    /**
     * Al elegir una unidad
     * Se cargan los objetivos de la unidad
     */
    $('#planDestrezasForm').on('change', '#id_unidad', function() {
        // Obtener URL
        var urlObjetivosUnidad = $('#planDestrezasForm').attr('load-objetivos-url');
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
     * Al elegir las destrezas
     * Se cargan los criterios
     */
    $('#planDestrezasForm').on('change', '#id_destrezas input', function() {
        // Obtener URL
        var urlCriterios = $('#planDestrezasForm').attr('load-criterios-url');

        // Obtiene las destrezas seleccionados
        var destrezas = $(`#id_destrezas li input[type="checkbox"]`);
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
            },
            success: function(data) {
                $('#id_criterios_evaluacion').html(data);
            }
        });
    });

    /**
     * Al elegir los criterios
     * Se cargan los indicadores
     */
    $('#planDestrezasForm').on('change', '#id_criterios_evaluacion input', function() {
        // Obtener URL
        var urlIndicadores = $('#planDestrezasForm').attr('load-indicadores-url');

        // Obtiene las criterios seleccionados
        var criterios = $(`#id_criterios_evaluacion li input[type="checkbox"]`);
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
            },
            success: function(data) {
                $('#id_indicadores').html(data);
                updateTextareas();
            }
        });
    });

    /**
     * Helper Functions
     */
    var clearFields = function() {
        $('#id_unidad').html('<option>Elija una unidad didáctica.</option>');
        $('#id_objetivos').html('<span>Seleccione una asignatura, un curso y una unidad.</span>');
        $('#id_destrezas').html('<span>Seleccione una asignatura y un curso.</span>');
        $('#id_objetivos_generales').html('');
        $('#id_criterios_evaluacion').html('');
        $('.indicadores ul').html('');
    }

    var updateTextareas = function() {
        var fields = ['estrategias_metodologicas', 'recursos', 'actividades_evaluacion'];
        updateTextareasSize('', '', fields);
    };
});
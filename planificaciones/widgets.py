from django.forms import CheckboxSelectMultiple


class EnhancedCheckboxSelectMultiple(CheckboxSelectMultiple):
    template_name = 'planificaciones/forms/widgets/'\
                    'enhanced_multiple_checkbox.html'
    option_template_name = 'planificaciones/forms/widgets/'\
                           'enhanced_checkbox_input.html'

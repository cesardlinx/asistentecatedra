import re
from django.core.exceptions import ValidationError


def validate_alpha(value):
    if not re.findall(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚäëïöüÄËÏÖÜ\s]+$', value):
        raise ValidationError(
            'Este campo solo permite letras',
            params={'value': value},
        )

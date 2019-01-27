import re

from django.core.exceptions import ValidationError


class NumberValidator:
    def validate(self, password, user=None):
        if not len(re.findall(r'\d', password)) >= 1:
            raise ValidationError(
                self.get_help_text(),
                code='password_no_number',
            )

    def get_help_text(self):
        return "La contraseña debe tener la menos 1 dígito, 0-9."


class UppercaseValidator:
    def validate(self, password, user=None):
        if not re.findall(r'[A-Z]', password):
            raise ValidationError(
                self.get_help_text(),
                code='password_no_upper',
            )

    def get_help_text(self):
        return "La contraseña debe tener la menos 1 letra mayúscula, A-Z."


class LowercaseValidator:
    def validate(self, password, user=None):
        if not re.findall(r'[a-z]', password):
            raise ValidationError(
                self.get_help_text(),
                code='password_no_lower',
            )

    def get_help_text(self):
        return "La contraseña debe tener la menos 1 letra minúscula, a-z."

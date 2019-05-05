from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # Sobreescribe el método para no tomar en cuenta si el
        # Usuario se ha logeado o no
        return str(user.pk) + user.password + str(timestamp)


account_token_generator = TokenGenerator()

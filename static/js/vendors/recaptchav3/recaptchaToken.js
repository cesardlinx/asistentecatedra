$(document).ready(function() {
    // reCaptcha v3 protection
    grecaptcha.ready(function() {
        grecaptcha.execute('6Leq1I0UAAAAACZSr9Fa8VaVs7vEeSepcq-a97L6', {
                action: 'signup'
            })
            .then(function(token) {
                document.getElementById('g-recaptcha-response').value = token;
            });
    });
});

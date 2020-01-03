
# CKEditor configuration
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_DEFAULT_LANGUAGE = 'es'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_CustomToolbarConfig': [

            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                       'Superscript', '-', 'RemoveFormat']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar',
                       'PageBreak']},
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent',
                       'Indent', '-', 'Blockquote', '-', 'JustifyLeft',
                       'JustifyCenter', 'JustifyRight', 'JustifyBlock',
                       '-', 'BidiLtr', 'BidiRtl']},
        ],
        'toolbar': 'CustomToolbarConfig',  # put selected toolbar config here
        'width': '99%',
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # 'devtools',
            'autogrow',
        ]),
    },
    'basic': {
        'skin': 'moono',
        'toolbar_CustomToolbarConfig': [

            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                       'Superscript', '-', 'RemoveFormat']},
            {'name': 'insert',
             'items': ['SpecialChar']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
            ]},
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent',
                       'Indent', '-', 'JustifyLeft',
                       'JustifyCenter', 'JustifyRight', 'JustifyBlock',
                       '-', 'BidiLtr', 'BidiRtl']},
        ],
        'toolbar': 'CustomToolbarConfig',  # put selected toolbar config here
        'width': '99%',
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'autogrow',
        ]),
    }
}

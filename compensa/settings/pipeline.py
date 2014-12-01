# -*- coding: utf-8 -*-
PIPELINE_CSS = {
    'com_local': {
        'source_filenames': (
            'com_local/css/base.sass',
        ),
        'output_filename': 'css/cb.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'datatables': {
        'source_filenames': (
            'com_local/plugins/dataTables/css/jquery.dataTables.css',
            'com_local/plugins/dataTables/css/dataTables.bootstrap.css',
        ),
        'output_filename': 'css/dt.css',
    },
}

PIPELINE_JS = {
    'html5': {
        'source_filenames': {
            #'jquery/jquery-1.11.1.min.js',
            'jquery/html5shiv.js',
            'jquery/respond.min.js',
        },
        'output_filename': 'js/html5.js',
    },
    'datatables': {
        'source_filenames': {
            'com_local/plugins/dataTables/js/jquery.dataTables.min.js',
            'com_local/plugins/dataTables/js/dataTables.bootstrap.js',
        },
        'output_filename': 'js/dt.js',
    }
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)
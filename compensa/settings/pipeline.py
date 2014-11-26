# -*- coding: utf-8 -*-
PIPELINE_CSS = {
    'com_local': {
        'source_filenames': (
            'com_local/base.sass',
        ),
        'output_filename': 'css/cb.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'jquery': {
        'source_filenames': {
            'jquery/jquery-1.11.1.min.js',
            'jquery/html5shiv.js',
            'jquery/respond.min.js',
        },
        'output_filename': 'js/jq.js',
    },

}

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)
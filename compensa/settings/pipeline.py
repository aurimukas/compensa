PIPELINE = {
    #'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
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
                'com_local/plugins/dataTables/css/dataTables.min.css',
            ),
            'output_filename': 'css/dt.css',
        },
    },

    'JAVASCRIPT': {
        'html5': {
            'source_filenames': {
                #'jquery/jquery-1.11.1.min.js',
                'jquery/html5shiv.js',
                'jquery/respond.min.js',
            },
            'output_filename': 'js/html5.js',
        },
        'components': {
            'source_filenames': {
                'jquery/dist/jquery.js',
            },
            'output_filename': 'js/components.js',
        },
        'datatables': {
            'source_filenames': {
                'com_local/plugins/dataTables/js/dataTables.min.js',
            },
            'output_filename': 'js/dt.js',
        },
        'app': {
            'source_filenames': {
                'com_local/js/homepage_table.js',
            },
            'output_filename': 'js/ap.js',
        },
    },

    #'CSS_COMPRESSOR': 'pipeline.compressors.yui.YUICompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',

    'PIPELINE_COMPILERS': (
        'pipeline.compilers.sass.SASSCompiler',
    ),
    'SASS_BINARY': '/usr/local/bin/sass',
    #'PIPELINE_AUTO': True
}
# -*- coding: utf-8 -*-

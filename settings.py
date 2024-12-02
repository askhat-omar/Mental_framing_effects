from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 5.00,
    'doc': "",
}

APP_KITS = {
    0: {
        'color': 'green',
        'sequence': [
            'introduction',
            'task1_instructions',
            'task1_prac_tr1',
            'task1_quiz_tr12',
            'task1_tr1',
            'task1_results_tr12',
            'task2_instructions',
            'task2_prac_tr13',
            'task2_quiz',
            'task2_tr1',
            'task2_results',
            'task3_tr13',
            'static_portfolio_results',
            'task4_tr13',
            'static_portfolio_b_results',
            'crt',
            'survey',
            'finalpage'
        ]
    },
    1: {
        'color': 'blue',
        'sequence': [
            'introduction',
            'task1_instructions',
            'task1_prac_tr2',
            'task1_quiz_tr12',
            'task1_tr2',
            'task1_results_tr12',
            'task2_instructions',
            'task2_prac_tr2',
            'task2_quiz',
            'task2_tr2',
            'task2_results',
            'static_portfolio_chp',
            'static_portfolio_results',
            'task4_tr2',
            'static_portfolio_b_results',
            'crt',
            'survey',
            'finalpage'
        ]
    },
    2: {
        'color': 'red',
        'sequence': [
            'introduction',
            'task1_instructions',
            'tr3_dynamic_pooled_practice',
            'tr3_dynamic_pooled_quiz',
            'tr3_dynamic_pooled',
            'tr3_dynamic_pooled_results',
            'task2_instructions',
            'task2_prac_tr13',
            'task2_quiz',
            'task2_tr1',
            'task2_results',
            'task3_tr13',
            'static_portfolio_results',
            'task4_tr13',
            'static_portfolio_b_results',
            'crt',
            'survey',
            'finalpage'
        ]
    },
}

SESSION_CONFIGS = [
    dict(
        name='DynPort',
        display_name="Experiment",
        num_demo_participants=1,
        app_sequence=['introduction',
                      'task1_instructions',
                      'task1_prac_tr1',
                      'task1_prac_tr2',
                      'tr3_dynamic_pooled_practice',
                      'task1_quiz_tr12',
                      'tr3_dynamic_pooled_quiz',
                      'task1_tr1',
                      'task1_tr2',
                      'tr3_dynamic_pooled',
                      'task1_results_tr12',
                      'tr3_dynamic_pooled_results',
                      'task2_instructions',
                      'task2_prac_tr13',
                      'task2_prac_tr2',
                      'task2_quiz',
                      'task2_tr1',
                      'task2_tr2',
                      'task2_results',
                      'task3_tr13',
                      'static_portfolio_chp',
                      'static_portfolio_results',
                      'task4_tr13',
                      'task4_tr2',
                      'static_portfolio_b_results',
                      'crt',
                      'survey',
                      'finalpage'
                      ],
        round1_T=3,
        round2_T=4
    )
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'SEK'
USE_POINTS = True

ROOMS = [
    dict(
        name='experiment',
        display_name='Financial Choice Experiment'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '@p7=^gv5pzv0udwk!c0b0hboi#0z5t0-#8v&!*y=zj4km!t@-^'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

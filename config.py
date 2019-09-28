# Server Specific Configurations
from pecan_test_project.my_hooks import SimpleHook
server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'pecan_test_project.controllers.root.RootController',
    #'hooks': lambda: [SimpleHook],
    'modules': ['pecan_test_project'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/pecan_test_project/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}

logging = {
    'root': {'level': 'INFO', 'handlers': ['logfile']},
    'loggers': {
        'pecan_test_project': {'level': 'DEBUG', 'handlers': ['logfile'], 'propagate': False},
        'pecan': {'level': 'DEBUG', 'handlers': ['logfile'], 'propagate': False},
        'py.warnings': {'handlers': ['logfile']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        },
        'logfile': {
            'level': 'DEBUG',
            'filename': '/var/log/test.log',
            'class': 'logging.FileHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s]'
                       '[%(threadName)s] %(message)s'),
        '__force_dict__': True
        }
    }
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf

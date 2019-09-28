from pecan import make_app
from pecan_test_project import model
from pecan_test_project import my_hooks


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        hooks = [my_hooks.SimpleHook()],
        logging=getattr(config, 'logging', {}),
        **app_conf
    )

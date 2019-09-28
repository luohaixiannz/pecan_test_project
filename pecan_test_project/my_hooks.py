from pecan.hooks import PecanHook

class SimpleHook(PecanHook):

    def on_route(self, state):
        print 'it is on route'

    def before(self, state):
        print 'it is before exec'

    def after(self, state):
        print 'it is after exec'

    def on_error(self, state):
        print 'it is on error'

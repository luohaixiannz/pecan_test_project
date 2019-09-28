from pecan import expose, redirect
from webob.exc import status_map
from pecan import rest

import logging

logger = logging.getLogger(__name__)

class BaseMethodController(object):

    # HTTP GET /
    @expose(generic=True, template='json')
    def index(self):
        return dict()

    # HTTP POST /
    @index.when(method='POST', template='json')
    def index_POST(self, **kw):
        return kw

class BooksController(object):
    @expose()
    def index(self):
        return "Welcome to book section."

    @expose()
    def bestsellers(self):
        return "We have 5 books in the top 10."

class CatalogController(object):
    @expose()
    def index(self):
        return "Welcome to the catalog."

    books = BooksController()

class Student(object):
    def __init__(self, name):
        self.name = name

class StudentController(object):
    def __init__(self, student):
        self.student = student

    @expose()
    def name(self):
        return self.student.name

    @expose()
    def _default(self):
        return 'enter _default'

class LookupTest(object):
    @expose()
    def _lookup(self, name, *remainder):
        print 'enr'
        student = Student(name)
        if student:
            return StudentController(student), remainder
        else:
            abort(404)

class MyRestController(rest.RestController):
    @expose()
    def get(self, id):
        logger.error('abc')
        return id

class RootController(object):

    @expose(generic=True, template='index.html')
    def index(self):
        return dict()

    @index.when(method='POST')
    def index_post(self, q):
        redirect('https://pecan.readthedocs.io/en/latest/search.html?q=%s' % q)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)

    catalog = CatalogController()
    basemethod = BaseMethodController()
    look_test = LookupTest()
    my_restcontroller = MyRestController()



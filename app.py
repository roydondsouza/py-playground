# pyramid_hello_world/app.py

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    print('Request inbound!')
    return Response('Docker works with Pyramid!')

def health(request):
    print('Request inbound!')
    return Response('Health Metrics!')

def site_view(request):
    if request.params.has_key('key'):
        return Response(request.matchdict['id']+request.params['key'])
    else:
        return Response(request.matchdict['id'])

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')

    config.add_route('health', '/health')
    config.add_view(health, route_name='health')

    config.add_route('site_view', '/hello/{id}')
    config.add_view(site_view, route_name='site_view')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
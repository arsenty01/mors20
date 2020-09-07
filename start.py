from main_module import main_app
from livereload import Server

if __name__ == '__main__':
    server = Server(main_app.wsgi_app)
    server.serve()
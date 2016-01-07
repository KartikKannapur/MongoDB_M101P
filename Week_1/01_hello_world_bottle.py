from bottle import route, run, template

# #Decorators to setup URLs for the web server to listen to
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
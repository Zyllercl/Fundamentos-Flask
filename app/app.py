from flask import Flask, redirect, render_template, request, url_for
# from flask_mysqldb import MySQL

app = Flask(__name__) # Inicializacion de la aplicacion

"""
    Conexion a Base de Datos MySQL

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'USUARIO'
    app.config['MYSQL_PASSWORD'] = 'PASSWORD'
    app.config['MYSQL_DB'] = 'NOMBRE_DB'

    conexion = MySQL(app) # Vinculo de la App con MySQL
"""

""" 
    Los decoradores before_request / after_request permiten realizar acciones antes o despues de que se ejecute una peticion
"""
@app.before_request
def before_request():
    print('Antes de la peticion...')

@app.after_request
def after_request(response):
    print('Despues de la peticion...')
    return response

# Decorador que indica la ruta raiz de la app
@app.route('/') 
def index():
    cursos = ['JavaScript', 'Python', 'Dark', 'PHP', 'Java']
    data = {
        'titulo': 'Principios de Flask',
        'mensaje': 'Cursos disponibles',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)

# Decorador de URL dinamica
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)

# Query String -> Se le puede pasar a una URL parametros variables (url/query_string?PARAMETROS_EXTRAS)
def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1')) # Obtener un valor de un parametro
    print(request.args.get('param2')) # Obtener un valor de un parametro
    return 'OK'


"""
    Creacion de una ruta para la base de datos
    @app.route('/cursos')
    def listar_cursos():
        data = {}

        try:
            cursor = conexion.connection.cursor()
            sql = "SELECT * FROM curso ORDER BY nombre ASC"
            cursor.execute(sql)
            cursos = cursor.fetchall() # Convertir los datos de la DB
            print(cursos)
            data['cursos'] = cursos
            data['mensaje'] = 'Exito'
        except Exception as ex:
            data['mensaje] = 'Error...'
        
        return jsonify(data)
"""



# Definir pagina personalizada 404
def pagina_no_encontrada(error):
    # return render_template('404.html'), 404 # Retorno de un template especifico
    return redirect(url_for('index')) # Retornar una redireccion hacia index

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada) # Manejar el error
    # debug=True permite activar el modo de depuracion, es decir, los cambios se muestran instantaneamente
    app.run(debug=True, port=5000)
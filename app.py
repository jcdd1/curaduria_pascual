from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza el archivo HTML que pondremos en la carpeta templates
    return render_template('chat.html')

if __name__ == '__main__':
    # debug=True permite ver cambios sin reiniciar el servidor manualmente
    app.run(debug=True)
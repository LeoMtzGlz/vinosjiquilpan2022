from src import create_app

app = create_app()

# Ruta principal

@app.route('/')
def index():
    return '<h1> Principal </h1>'

if __name__ == '__main__':
    app.run() #debug=True, port=5000
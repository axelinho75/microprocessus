from flask import Flask, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Loups</h1>'

@app.route('/games')
def list_games():
    return '<h1>Games</h1>'

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        title = request.form['title']
        app.logger.debug(title)
        return redirect(url_for('list_games'))
    return '''
    <form method="POST">
        <input type="text" name="title">
        <input type="submit" value="create game">
    </form>
    '''
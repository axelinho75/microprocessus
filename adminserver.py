from flask import Flask, request, redirect, url_for
from database import db_session, init_db
from models import game


app = Flask(__name__)
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    return '<h1>Loups</h1>'

@app.route('/games')
def list_games():
    result = game.query.all()
    app.logger.debug(result)
    html_output = '<p>' + '</p><p>'.join(list(map(lambda game: game.title, result)))
    return '<h1>Games</h1>' + html_output

@app.route('/game', methods=['GET', 'POST'])
def create_game():
    if request.method == 'POST':
        title = request.form['title']
        new_game = game(title=title)
        app.logger.debug(new_game)
        db_session.add(new_game)
        db_session.commit()
        return redirect(url_for('list_games'))
    return '''
    <form method="POST">
        <input type="text" name="title">
        <input type="submit" value="create game">
    </form>
    '''
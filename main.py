from flask import Flask, render_template, request, url_for, redirect, session
from werkzeug.utils import secure_filename
from functools import wraps
import json

import config
from bookmarks import bookmarks
from themes import themes
from settings import settings
from user import user
import db as db

app = Flask(__name__)

app.secret_key = config.SECRET_KEY

app.register_blueprint(bookmarks)
app.register_blueprint(themes)
app.register_blueprint(settings)
app.register_blueprint(user)

@app.route('/')
def index():
    if 'id' in session:
        user = db.getUser()
        #if user['wizard']:
        #    return redirect(url_for('settings.wizard'), code=302)
        #else:
        session.pop('preview_id', None)
        session.pop('preview_css', None)
        session.pop('editor_id', None)
        session.pop('editor_css', None)
        session.pop('editor_title', None)
        session['css'] = db.getUsersCSS()
        session['bookmarks'] = db.getBookmarks()
        return render_template('mypage.html')
    return render_template('index.html', name="name")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.template_filter('is_url')
def is_url(field):
    if field.startswith("http://") or field.startswith("https://"):
            return True
    return False

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=config.DEBUG)

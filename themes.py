from flask import Blueprint, request, redirect, url_for, session, flash, render_template
import db as db
import json

themes = Blueprint('themes', __name__)

@themes.route('/themes', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        json = request.data.decode("utf-8")
        #db.setTheme(id, title, json)
        return "1"
    else:
        return db.getThemes()

@themes.route('/settheme/<int:id>', methods=['GET'])
def settheme(id):
    db.setUsersTheme(id)
    return redirect(url_for('settings.themes'), code=302)

@themes.route('/createtheme', methods=['POST'])
def createtheme():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        title = json_data['editor_title']
        css = json_data['editor_css']
        if session.get('editor_id'):
            #update
            id = session['editor_id']
            db.setTheme(id, title, css)
        else:
            #createtheme
            id = 1#db.insertTheme(title, css)
        db.setUsersTheme(id)
        return "1"

@themes.before_request
def check_valid_login():
    if 'id' not in session:
        return redirect(url_for('index'), code=302)

from flask import Blueprint, request, redirect, url_for, session, flash, render_template
import db as db
import json

themes = Blueprint('themes', __name__)

@themes.route('/theme', methods=['POST', 'GET', 'PUT', 'DELETE'])
def index():
    if request.method == 'POST': # Set theme
        json_data = request.get_json(force=True)
        id = json_data['theme_id']
        db.setUsersTheme(id)
        return "1"
    elif request.method == 'GET': # Get current theme
        return db.getThemes()
    elif request.method == 'PUT': # Create of update
        json_data = request.get_json(force=True)
        title = json_data['editor_title']
        css = json_data['editor_css']
        if session.get('editor_id'):
            #update
            id = session['editor_id']
            db.setTheme(id, title, css)
        else:
            id = db.insertTheme(title, css)
        db.setUsersTheme(id)
        return "1"
    elif request.method == 'DELETE': # Remove theme
        json_data = request.get_json(force=True)
        id = json_data['theme_id']
        db.removeTheme(id)
        return "1"

@themes.route('/themes', methods=['POST', 'GET', 'PUT', 'DELETE'])
def funcThemes():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return db.getThemes()
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass

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
            # TODO Insert new there to DB
            id = db.insertTheme(title, css)

            print(id)

        db.setUsersTheme(id)
        return "1"

@themes.before_request
def check_valid_login():
    if 'id' not in session:
        return redirect(url_for('index'), code=302)

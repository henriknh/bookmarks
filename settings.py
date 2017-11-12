from flask import Blueprint, request, redirect, url_for, session, flash, render_template
import db as db
import json

settings = Blueprint('settings', __name__)

menu_items = ['Profile', 'Bookmarks', 'Themes', 'Search Engines', 'About']

@settings.route('/settings', methods=['POST', 'GET'])
def index():
    return render_template('settings.html', active="profile", menu_items=menu_items)

@settings.route('/settings/profile', methods=['POST', 'GET'])
def profile():
    return render_template('settings.html', active="profile", menu_items=menu_items)

@settings.route('/settings/bookmarks', methods=['POST', 'GET'])
def bookmarks():
    return render_template('settings.html', active="bookmarks", menu_items=menu_items, bookmarks=db.getBookmarks())

@settings.route('/settings/themes', methods=['POST', 'GET'])
def themes():
    themes = db.getThemes()
    return render_template('settings.html', active="themes", menu_items=menu_items, themes=themes)

@settings.route('/settings/search+engines', methods=['POST', 'GET'])
def search_engines():
    return render_template('settings.html', active="search engines", menu_items=menu_items)

@settings.route('/settings/about', methods=['POST', 'GET'])
def about():
    return render_template('settings.html', active="about", menu_items=menu_items)

@settings.route('/wizard', methods=['POST', 'GET'])
def wizard():
    return render_template('wizard.html', bookmarks=db.getBookmarks(), displayname=db.getUser()['displayname'])

@settings.route('/preview', methods=['POST', 'GET'])
def preview():
    if request.method == 'POST':
        session.pop('editor_preview', None)
        session.pop('editor_css', None)
        json_data = request.get_json(force=True)
        if 'preview_id' in json_data:
            print("id")
            session.pop('editor_id', None)
            session['preview_id'] = json_data['preview_id']
            session['editor_css'] = db.getCSS(json_data['preview_id'])
        else:
            print("!id")
            session['editor_preview'] = True
            session['editor_css'] = json_data['editor_css']
        return "1"
    else:
        return render_template('mypage.html')

@settings.route('/editor', methods=['POST', 'GET'])
def editor():
    if request.method == 'POST':
        session.pop('editor_id', None)
        session.pop('editor_css', None)
        session.pop('editor_title', None)
        json_data = request.get_json(force=True)
        if 'editor_id' in json_data:
            session['editor_id'] = json_data['editor_id']
            theme = db.getTheme(json_data['editor_id'])
            if theme:
                session['editor_css']=theme['css']
                session['editor_title']=theme['title']
        return "1"
    else:
        return render_template('editor.html')

@settings.before_request
def check_valid_login():
    if 'id' not in session:
        return redirect(url_for('index'), code=302)

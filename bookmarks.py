from flask import Blueprint, request, redirect, url_for, session, flash, render_template
import db as db
import json

bookmarks = Blueprint('bookmarks', __name__)

@bookmarks.route('/bookmarks', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        json = request.data.decode("utf-8")
        db.setBookmarks(json)
        return "1"
    else:
        return db.getBookmarks()

@bookmarks.before_request
def check_valid_login():
    if 'id' not in session:
        return redirect(url_for('index'), code=302)

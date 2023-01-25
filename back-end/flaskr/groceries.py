from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, request
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import random

bp = Blueprint('groceries', __name__)

@bp.route('/groceries')
def index():
    db = get_db()
    groceries = db.execute(
        'SELECT name'
        ' FROM groceries'
    ).fetchall()
    results = [tuple(row) for row in groceries]

    return results
    
@bp.route('/groceries/add')
def test():
    db = get_db()
    category = request.args.get('name')
    if not category:
        print('give me a name or I crash')
    kanji = db.execute(
        'select name'
        ' from groceries'
        ' where category = \'{}\''.format(category)
    ).fetchall()
    results = [tuple(row) for row in kanji]
    tested_kanji = scramble_list(results)

    return tested_kanji


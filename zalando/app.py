#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import flask

from zalando import get_category

app = flask.Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if flask.request.method == 'POST':
        path = flask.request.form.get('category_path')
        return flask.redirect(flask.url_for('get_category_from_zalando', category_path=path))
    else:
        return flask.render_template('index.html')

@app.route('/get_category')
def get_category_from_zalando():
    path = flask.request.args.get('category_path')
    if path:
        category_dict = get_category(path)
        return flask.jsonify(**category_dict)
    return 'Please enter valid category!'

def cli_options(args):
    description = 'Run flask app to scrap zalando.de'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--port', type=int)
    return parser.parse_args()

def main(args=sys.argv):
    args = cli_options(sys.argv)
    app.run(port=args.port)

if __name__ == '__main__':
    main()
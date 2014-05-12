#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from flask import Flask, request, jsonify

from zalando import get_category

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_category')
def get_category_from_zalando():
    path = 'damenbekleidung-jeans-straight-leg'
    category_dict = get_category(path)
    return jsonify(**category_dict)
    # return 'Please enter valid category!'

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
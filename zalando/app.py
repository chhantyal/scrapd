#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

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
#! /usr/bin/env python
import bottle

app = application = bottle.Bottle()

@app.route('/hello')
def hello():
    return 'Hello from Bottle'


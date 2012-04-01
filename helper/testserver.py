from bottle import route, run, response
import bottle
import sys
import json


def loadapi(file):
    ''' Helper to load files '''
    datafile = open(sys.argv[1])
    datatxt = "".join([line.strip() for line in datafile.readlines()])
    datajson = json.loads(datatxt)

@route('/api/<filename>')
def index(filename=''):
    datafile = open("./api/"+filename)
    datatxt = "".join([line.strip() for line in datafile.readlines()])
    datajson = json.loads(datatxt)
    return json.dumps(datajson)

@route('/static/:filename#.*#')
def static(filename):
    return bottle.static_file(filename, root='./static/')

@route('/:filename#.*#')
def static(filename):
    return bottle.static_file(filename, root='./site/')


run(host='localhost', port=8080)

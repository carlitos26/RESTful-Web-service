from app import app
from flask.json import jsonify
from modules import *

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    return '{}\n{}\n{}\n{}\n{}\n'.format('Welcome in the Query DB Web Service!', 'How to use it:', \
                                     '1) Total entries: curl http://<Server_address>/entries', \
                                     '2) Total entries for name: curl --request GET http://<Server_address>/entry_name/"name"', \
                                     '3) Insert new name: curl --request POST http://<Server_address>/insert/"name","year","gender(M/F)","count"')

@app.route("/entries")
def entries():
    entries = total_entries()
    return '{}\n'.format('{}\n'.format(entries)[1:-3])

@app.route("/entry_name/<name>", methods=["GET"])
def entry_name(name):
    entries = select_entries_by_name(name)
    return jsonify({'Entries for %s' % name: entries})

@app.route("/insert/<name>,<year>,<gender>,<count>", methods=["POST"])
def insert(name,year,gender,count):
    new_id = insert_name(name,year,gender,count)
    return '{}\n'.format(str(new_id))
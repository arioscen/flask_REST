from flask import Flask, request, send_file
import os
import json
app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello World!'


@app.route("/profile/")
@app.route("/profile/<userid>", methods=['GET', 'PUT', 'POST', 'DELETE'])
def uid(userid=None):
    if request.method == 'GET':
        if userid:
            try:
                get_file = send_file('profile/%s.json' % userid, attachment_filename='%s.json' % userid)
                return get_file
            except FileNotFoundError as e:
                return str(e.__class__)
        else:
            return '<p>'.join(os.listdir('profile/'))
    if request.method == 'PUT':
        # print(request.headers['Authorization']) {"message":"Authentication Failed."}
        try:
            put_data = json.loads(request.data)
            put_data_dumps = json.dumps(put_data)
            with open('profile/%s.json' % userid, 'w') as file:
                file.write(put_data_dumps)
            return put_data_dumps
        except json.decoder.JSONDecodeError as e:
            return str(e.__class__)

    if request.method == 'POST':
        if userid + ".json" in os.listdir('profile/'):
            return "profile of %s has already existed." % userid
        else:
            try:
                put_data = json.loads(request.data)
                put_data_dumps = json.dumps(put_data)
                with open('profile/%s.json' % userid, 'w') as file:
                    file.write(put_data_dumps)
                return put_data_dumps
            except json.decoder.JSONDecodeError as e:
                return str(e.__class__)

    if request.method == 'DELETE':
        if userid + ".json" in os.listdir('profile/'):
            os.remove('profile/%s.json' % userid)
            return "profile of %s  was DELETE." % userid
        else:
            return "profile of %s  doesn't exist." % userid


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002)

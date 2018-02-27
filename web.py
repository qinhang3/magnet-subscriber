from flask import Flask, url_for, redirect, request, render_template
from flask.ext import restful
import database
import requestnode
import json

app = Flask(__name__)
api = restful.Api(app)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/test/<name>')
def test(name=None):
    return render_template('list.html', datas=requestnode.work('http://cilifanhao.org/q/' + name + '/1/4/0.html', 10))


@app.route('/search/<name>')
def search(name):
    datas = requestnode.work('http://cilifanhao.org/q/' + name + '/1/4/0.html', 10)
    database.save_nodes(datas, name)
    return render_template('list.html', datas=datas)


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}


class Task(restful.Resource):
    def get(self, offset=0, count=10):
        data = database.get_tasks(offset, count)
        for item in data:
            nodes = database.get_nodes(item['keyword'])
            for node in nodes:
                node['choose'] = node['magnet'] == item['magnet']
            item['nodes'] = nodes
        return data

    def put(self, name):
        magnet = json.loads(request.data)['magnet']
        if not magnet:
            database.add_task(name)
            datas = requestnode.work('http://cilifanhao.org/q/' + name + '/1/4/0.html', 10)
            database.save_nodes(datas, name)
        else:
            database.add_task(name, magnet)

    def delete(self, name):
        database.delete_task(name)


api.add_resource(Task, '/ajax/task', '/ajax/task/<name>', '/ajax/task/<offset>/<count>')

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(host='0.0.0.0', port=80)

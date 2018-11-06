# from werkzeug.contrib.fixers import ProxyFix

from flask import Flask, Response
from git import Repo

app = Flask('gitstatic')
app.config.from_pyfile('config.cfg')
repository_path = app.config.get('REPOSITORY_PATH')
# app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
@app.route("/<path:path>")
def home(**kw):
    status = 200
    mime_type = 'text/html'

    try:
        path = kw.get('path', '').split('/')

        user = path[0:1][0]
        repo = path[1:2][0]
        index = '/'.join(path[2:])

        if (not (user and repo)):
            return

        repo = Repo('{repo_path}/{user}/{repo}'.format(repo_path=repository_path, user=user, repo=repo))
        branch = repo.heads['gh-pages']
        blob = branch.object.tree[index]

        resp = Response(blob.data_stream.read(), status)
        resp.headers['Content-Type'] = '{type}; charset=utf-8'.format(type=blob.mime_type or mime_type)
        resp.headers['Content-Length'] = blob.size

        return resp
    except:
        return 'Not Found', 404, { 'Content-Type': mime_type }



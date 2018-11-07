from flask import Flask, Response, redirect
from git import Repo

app = Flask(__name__)
app.config.from_envvar('GITSTATIC_CONF')

repository_path = app.config.get('REPOSITORY_PATH')
default_branch = app.config.get('BRANCH')

@app.route('/', defaults={'path': ''})
@app.route('/<string:path>')
@app.route('/<path:path>')
def home(**kw):
    status = 200
    mime_type = 'text/html'

    try:
        path = kw.get('path', '').split('/')

        # e.g:
        # user/repo/xxx.html
        # user/repo/resource/index.html
        user = path[0:1][0]
        repo = path[1:2][0]
        index = '/'.join(path[2:])

        if len(path) == 2:
            return redirect(request.host_url + kw.get('path') + '/index.html')

        if len(path) == 3 and index == '':
            return redirect(request.host_url + kw.get('path') + 'index.html')

        if (not (user and repo)):
            return 'Not Found', 404

        repo = Repo('{repo_path}/{user}/{repo}.git'.format(repo_path=repository_path, user=user, repo=repo))
        branch = repo.heads[default_branch]
        blob = branch.object.tree[index]

        resp = Response(blob.data_stream.read(), status)
        resp.headers['Content-Type'] = blob.mime_type or mime_type
        resp.headers['Content-Length'] = blob.size

        return resp
    except:
        return 'Not Found', 404

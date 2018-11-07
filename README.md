# Git pages static

A github pages implements for any git repository hosting

## Usage

up command

```
export GITSTATIC_CONF=/etc/gitstatic/config.cfg
gunicorn -w 4 -b 127.0.0.1:5000 app:app
```

config.cfg

```
REPOSITORY_PATH = "/Users/timothy/Workspace"
BRANCH = "gh-pages"
```

# License MIT

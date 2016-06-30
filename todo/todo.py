
import json
from os.path import expanduser

_DEFAULT_FILE = expanduser("~") + '/.todo/app.json'
_DEFAULT_NOTEBOOK = 'default'


class TodoMananger(object):

    def _load(self):
        return json.load(open(_DEFAULT_FILE, 'r+'))

    def _save(self, app_data):
        with open(_DEFAULT_FILE, 'r+') as appfile:
            appfile.write(json.dumps(app_data))

    def add_item(self, title, notebook=None):
        if not title:
            raise Exception('you have to provider a title to your todo item')

        notebook = _DEFAULT_NOTEBOOK if not notebook else notebook

        appdata = self._load()

        if notebook not in appdata:
            appdata[notebook] = []

        appdata[notebook].append({'title': title})
        self._save(appdata)

    def list_all(self):
        return self._load()

    def list(self, notebook):
        if not notebook:
            raise Exception('you have to provider a notebook name')

        appdata = self._load()
        if notebook not in appdata:
            raise Exception('This notebook does not exists')

        return appdata[notebook]

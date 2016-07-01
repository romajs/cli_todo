
import json, os
from os.path import expanduser
from . import notify

_DEFAULT_DIR = expanduser("~") + '/.todo'
_DEFAULT_FILE = _DEFAULT_DIR + '/app.json'
_DEFAULT_NOTEBOOK = 'default'


class TodoMananger(object):

    def _load(self):
        return json.load(open(_DEFAULT_FILE, 'r+'))

    def _save(self, app_data):
        with open(_DEFAULT_FILE, 'r+') as appfile:
            appfile.write(json.dumps(app_data))

    def add_item(self, title, notebook=None, cron=None):
        if not title:
            raise Exception('you have to provider the title to your todo item')

        notebook = _DEFAULT_NOTEBOOK if not notebook else notebookz

        appdata = self._load()

        if notebook not in appdata:
            appdata[notebook] = []

        if cron is not None:
            notify.schedule(notebook, title, cron)

        appdata[notebook].append({'title': title})
        self._save(appdata)

    def list_all(self):
        return self._load()

    def list(self, notebook):
        if not notebook:
            raise Exception('you have to provider the notebook name')

        appdata = self._load()
        if notebook not in appdata:
            raise Exception('This notebook does not exists')

        return appdata[notebook]

    def delete_notebook(self, notebook_name):
        if not notebook_name:
            raise Exception('you have to provider the name of the notebook')

        appdata = self._load()
        del appdata[notebook_name]

    def delete(self, notebook_name, item_title):
        if not notebook_name or not item_title:
            raise Exception('you have to provider the name of the notebook and the title of the item')

        appdata = self._load()
        if item_title not in appdata[notebook_name]:
            raise Exception('There is no item with this title in the %s notebook' % (notebook_name))

        del appdata[notebook_name][item_title]


import json
from os.path import expanduser

_DEFAULT_FILE = expanduser("~") + '/.todo/app.json'


class TodoMananger(object):

    def __load(self):
        return json.load(open(_DEFAULT_FILE, 'r+'))

    def _save(self, app_data):
        with open(_DEFAULT_FILE, 'r+') as appfile:
            appfile.write(json.dumps(app_data))

    def add_item(self, title, notebook=None):
        appdata = self.__load()

        if notebook not in appdata:
            appdata[notebook] = []

        appdata[notebook].append({'title': title})
        self._save(appdata)

    def list_all(self):
        return self.__load()

    def list(self, notebook):
        appdata = self.__load()
        if notebook not in appdata:
            raise Exception('This notebook does not exists')

        return appdata[notebook]

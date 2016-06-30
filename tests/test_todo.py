
import unittest
from todo.todo import TodoMananger


class TestTodo(unittest.TestCase):

    appdata = {}

    def _load(self):
        return self.appdata

    def _save(self, data):
        self.appdata = data

    def setUp(self):
        self.appdata = {}

    def test_add_item(self):
        TodoMananger._load = self._load
        TodoMananger._save = self._save

        todo = TodoMananger()
        todo.add_item('new')

        expected = {
            "default": [{"title": "new"}],
        }
        self.assertEqual(expected, self.appdata)

        todo = TodoMananger()
        todo.add_item('fix projects bugs', notebook='today')

        expected = {
            "default": [{"title": "new"}],
            "today": [{"title": "fix projects bugs"}]
        }
        self.assertEqual(expected, self.appdata)

        with self.assertRaises(Exception):
            todo.add_item()

    def test_list(self):
        TodoMananger._load = self._load
        TodoMananger._save = self._save

        todo = TodoMananger()
        with self.assertRaises(Exception):
            todo.list()

        todo.add_item('fix projects bugs', notebook='today')
        with self.assertRaises(Exception):
            todo.list('false_notebook')

        self.assertEqual(self.appdata, todo.list_all())
        self.assertEqual([{"title": "fix projects bugs"}], todo.list('today'))

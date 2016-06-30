
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
        TodoMananger._load = self._load
        TodoMananger._save = self._save

    def test_add_item(self):
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
        todo = TodoMananger()
        with self.assertRaises(Exception):
            todo.list()

        todo.add_item('fix projects bugs', notebook='today')
        with self.assertRaises(Exception):
            todo.list('false_notebook')

        self.assertEqual(self.appdata, todo.list_all())
        self.assertEqual([{"title": "fix projects bugs"}], todo.list('today'))

    def test_delete(self):
        todo = TodoMananger()
        todo.add_item('fix projects bugs', notebook='today')
        todo.add_item('send that email',)
        todo.delete_notebook('today')

        self.assertEqual({'default': [{'title': 'send that email'}]}, todo.list_all())

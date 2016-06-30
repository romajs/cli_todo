import click
from todo.todo import TodoMananger


@click.command()
@click.option('-nt', default=None, help='notebook name')
@click.option('-t', help='the name of the todo item')
def cli(t, nt=None):
    if not t:
        raise Exception('you have to provider a title to your todo item')

    todo = TodoMananger()
    todo.add_item(t, notebook=nt)

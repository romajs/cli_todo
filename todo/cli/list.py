import click
from todo.todo import TodoMananger


@click.command()
@click.option('-nt', default=None, help='notebook name')
def cli(nt=None):
    todo = TodoMananger()

    if not nt:
        appdata = todo.list_all()

        for notebook_name, items in appdata.items():
            print 'Items from %s' % (notebook_name,)

            for todo_item in items:
                print todo_item['title']

            print '\n\n'

    else:
        appdata = todo.list(notebook=nt)
        print 'Items from %s' % (nt,)

        for todo_item in appdata:
            print todo_item['title']

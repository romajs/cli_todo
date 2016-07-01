# cli_todo
A *really* simple command line interface to maintain a todo list

## How to use

**Install it**
```bash
pip install todo_cli
```

**Configure it**
```bash
mkdir ~/.todo
echo "{}" > ~/.todo/app.json
```

## Use it
#### Create your fist todo
If you dont use the -nt argument, your todo item will be saved in the *default* notebook.
```bash
todo new -t my first todo item
```

Also, you can specify a notebook
```bash
todo new -t my first todo item -nt today
```

And finally, you can schedule to receive a notification using cron format time
```bash
todo new -t "scheduled todo item" -c "30 12 * * *"
```

### List
You can list all items from all notebooks
```bash
todo list
```

You can list all items of one specified notebook
```bash
todo list -nt today
```

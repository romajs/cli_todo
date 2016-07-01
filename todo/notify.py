
import os

def __register_cron(crontab_cmd, crontab_file):
    with open(crontab_file, 'wb') as file:
        file.write(crontab_cmd)
    os.system('crontab %s' % crontab_file)

def schedule(title, body, cron=None):        
    __register_cron(' '.join(['%s' % cron,
        'export DBUS_SESSION_BUS_ADDRESS="%s"' % os.environ['DBUS_SESSION_BUS_ADDRESS'],
        '&&', 
        '/usr/bin/notify-send "%s" "%s"' % (title, body),
        '\n'
    ]), os.path.expanduser("~") + '/.todo/crontab')


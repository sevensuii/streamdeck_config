import sqlite3
import sys
from plyer import notification
# from termcolor import colored

conn = sqlite3.connect('/home/sevensuii/streamdeck_config/programs/pomodoro/pomodoro.db')
cursor = conn.cursor()

timer_type = sys.argv[1]

############
# TIMERS   #
############
if ('timer' == timer_type):
    timer = sys.argv[2]
    mode = sys.argv[3]

    estado = cursor.execute('SELECT estado FROM relojes WHERE nombre = ?', ('timer'+timer,)).fetchone()[0]

    if ('estado' == mode):
        if ( 'A' == estado ):
            datos = cursor.execute('UPDATE relojes SET transcurrido = time(transcurrido, \'+1 seconds\')  WHERE nombre = ? RETURNING transcurrido;', ('timer'+timer,)).fetchone()
            conn.commit()
            print(datos[0])
        else:
            datos = cursor.execute('SELECT transcurrido FROM relojes WHERE nombre = ?;', ('timer'+timer,)).fetchone()
            print(datos[0], end='')

    # Play/Pause
    elif ('play-pause' == mode):
        if ( 'A' == estado ):
            nuevo_estado = 'P'
        else:
            nuevo_estado = 'A'

        cursor.execute("UPDATE relojes SET estado = ? WHERE nombre = ?", (nuevo_estado, 'timer'+timer))
        conn.commit()

    # Reset
    elif ('reset' == mode):
        cursor.execute("UPDATE relojes SET transcurrido = time('00:00:00') WHERE nombre = ?", ('timer'+timer,))
        conn.commit()

############
# POMODORO #
############
elif ('pomodoro' == timer_type):
    mode = sys.argv[2]
    estado = cursor.execute('SELECT estado FROM relojes WHERE nombre = ?', ('pomodoro',)).fetchone()[0]

    if ('estado' == mode):
        if (estado in ('A', 'D')):
            if ('00:00:00' != cursor.execute('SELECT transcurrido FROM relojes WHERE nombre = ?', ('pomodoro',)).fetchone()[0]):
                datos = cursor.execute('UPDATE relojes SET transcurrido = time(transcurrido, \'-1 seconds\') WHERE nombre = ? RETURNING transcurrido,estado;', ('pomodoro',)).fetchone()
            
            else:
                if ('A' == estado):
                    datos = cursor.execute('UPDATE relojes SET estado = "D", transcurrido = descanso WHERE nombre = ? RETURNING transcurrido, estado', ('pomodoro',)).fetchone()
                    notification.notify(title='Pomodoro', message='Rest time\n\n\n\n\n\n\n\n\n\n┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿  ┬──┬ ノ(ò_óノ)', timeout=10)
                elif ('D' == estado):
                    datos = cursor.execute('UPDATE relojes SET estado = "P", transcurrido = trabajo WHERE nombre = ? RETURNING transcurrido, estado', ('pomodoro',)).fetchone()
                    notification.notify(title='Pomodoro', message='Work time\n\n\n\n\n\n\n\n\n\n┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿  ┬──┬ ノ(ò_óノ)', timeout=10)
                
            print(datos[0].split(':', 1)[1]+'-'+datos[1], end='')
            conn.commit()

        else:
            datos = cursor.execute('SELECT transcurrido, estado FROM relojes WHERE nombre = ?;', ('pomodoro',)).fetchone()
            print(datos[0].split(':', 1)[1]+'-'+datos[1], end='')

    # Play/Pause
    elif ('play-pause' == mode):
        if ( 'A' == estado):
            nuevo_estado = 'P'
        elif ('D' == estado):
            nuevo_estado = 'DP'
        elif ('DP' == estado):
            nuevo_estado = 'D'
        else:
            nuevo_estado = 'A'

        cursor.execute("UPDATE relojes SET estado = ? WHERE nombre = ?", (nuevo_estado, 'pomodoro'))
        conn.commit()

    # Reset
    elif ('reset' == mode):
        cursor.execute("UPDATE relojes SET transcurrido = trabajo, estado = 'P' WHERE nombre = ?", ('pomodoro',))
        conn.commit()

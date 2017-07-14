import ccircle
import connection

con = connection.create()
con.send('set_name', {'name': 'Ambrosius'})


args = {
    'vx': -43,
    'vy': -24,
}

con.send('set_velocity', args)

while True:
    if ccircle.isKeyDown('left'):
        args['vy'] = 0
        args['vx'] = -50
        con.send('set_velocity', args)
    if ccircle.isKeyDown('right'):
        args['vy'] = 0
        args['vx'] = 50
        con.send('set_velocity', args)
    if ccircle.isKeyDown('up'):
        args['vy'] = -50
        args['vx'] = 0
        con.send('set_velocity', args)
    if ccircle.isKeyDown('down'):
        args['vy'] = 50
        args['vx'] = 0
        con.send('set_velocity', args)


# Write code to make money and kill the evil cat!
# See readme.txt !
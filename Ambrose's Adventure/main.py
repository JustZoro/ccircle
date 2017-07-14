import ccircle

window = ccircle.Window("Ambroses Adventure")
window.toggleMaximized()

while window.isOpen():
    window.clear(0, 0, 0)
for i in range():
        window.draw('AA_AmbroseSideStop.png')
        window.draw('AA_AmbroseSideW.png')
        window.draw('AA_AmbroseSideStop.png')
        window.draw('AA_AmbroseSideW(2).png')
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
window.update()
import simplegui
minut =  0
secund = 0
msecund = 0
win_count = 0
lose_count = 0

def convert(val):
    global msecund 
    secund = int(val)
    msecund = int(round(10 * (val - secund)) % 10)
    return msecund

def trancfer():
    global secund, minut
    if secund >= 59.9:
        secund = 0
        minut += 1
    return str(minut)

def start():
    global timer
    timer.start()
    
def stop():
    global timer,win_count,lose_count,msecund
    if convert(secund) == 0:
        win_count += 1
    else:
        lose_count += 1
    timer.stop()

def restart():
    global secund, minut, win_count,lose_count
    minut = 0
    secund = 0
    win_count = 0
    lose_count = 0
    timer.stop()

def draw(canvas):
    if secund <=0:
        canvas.draw_text("00." + str(secund), [140,112], 48, "Orange")
    else:
        if secund <= 9.9:   
            canvas.draw_text("0"+str(secund), [140,112], 48, "Red")
        else:
            canvas.draw_text(str(secund), [140,112], 48, "Orange")
    canvas.draw_text(str(minut )+ ":", [103,112], 48, "Orange")

    canvas.draw_text(str(win_count) +"/"+ str(lose_count), [230,25], 20, "Yellow")
def timer():
    global secund, minut
    secund += 0.1 
    trancfer()
    
frame = simplegui.create_frame("Timer", 300, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Restart",restart)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer)
 
frame.start()

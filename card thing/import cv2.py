import cv2
from tkinter import PhotoImage
import numpy as np 
from ffpyplayer.player import MediaPlayer 
import turtle as trtl
from turtle import Shape, Screen, Turtle
import time
wn = trtl.Screen()
wn.setup(width =1920,height =1080)




def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap


def running_videos(sourcePath):
   
    camera = getVideoSource(sourcePath, 720, 480)
    player = MediaPlayer(sourcePath)

    while True:
        ret, frame = camera.read()
        audio_frame, val = player.get_frame()

        if (ret == 0):
            print("End of video")
            break

        frame = cv2.resize(frame, (1920, 1080))
        cv2.imshow('Camera', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        #if val != 'eof' and audio_frame is not None:
            #frame, t = audio_frame
            #print("Frame:" + str(frame) + " T: " + str(t))

    camera.release()
    cv2.destroyAllWindows()
    wn.bgpic(r"0250.png")


if __name__ == "__main__":
    running_videos( r"new thing0001-0250.mp4")










def card():
    pic=PhotoImage(file=r'checkerboard-removebg-preview-_1_.gif').zoom(2,2)
    wn.addshape('board', Shape('image', pic))
    board = trtl.Turtle()
    board.shape('board')
    wn.screensize(800,600)
    checker0 = trtl.Turtle()
    checker1 = trtl.Turtle()
    checker2 = trtl.Turtle()
    checker3 = trtl.Turtle()
    checker4 = trtl.Turtle()
    checker5 = trtl.Turtle()
    checker6 = trtl.Turtle()
    checker7 = trtl.Turtle()
    checker8 = trtl.Turtle()
    checker9 = trtl.Turtle()
    checker10 = trtl.Turtle()
    checker11 = trtl.Turtle()


    yellowcheckers=[checker0,checker1,checker2,checker3,checker4,checker5,checker6,checker7,checker8,checker9,checker10,checker11]
    num=0
    for checker in yellowcheckers:
        pic=PhotoImage(file=r'yellowchecker - Copy.gif').zoom(1,1)
        wn.addshape('checker'+str(num), Shape('image', pic))
        checker.speed('fastest')
        checker.shape('checker'+str(num))
        checker.penup()
        if num<4:
            checker.goto(-185+num*160,-283)
        elif num<8:
            checker.goto(-185-80+(num-4)*160,-283+80)
        elif num<12:
            checker.goto(-185+(num-8)*160,-283+160)
        num=num+1
    pchecker0 = trtl.Turtle()
    pchecker1 = trtl.Turtle()
    pchecker2 = trtl.Turtle()
    pchecker3 = trtl.Turtle()
    pchecker4 = trtl.Turtle()
    pchecker5 = trtl.Turtle()
    pchecker6 = trtl.Turtle()
    pchecker7 = trtl.Turtle()
    pchecker8 = trtl.Turtle()
    pchecker9 = trtl.Turtle()
    pchecker10 = trtl.Turtle()
    pchecker11 = trtl.Turtle()
    pcheckers=[pchecker0,pchecker1,pchecker2,pchecker3,pchecker4,pchecker5,pchecker6,pchecker7,pchecker8,pchecker9,pchecker10,pchecker11]
    num=0
    for pchecker in pcheckers:
        ppic=PhotoImage(file=r'purplemmino-removebg-preview_-_Copy-removebg-preview.gif').subsample(2,2)
        wn.addshape('pchecker'+str(num), Shape('image', ppic))
        pchecker.shape('pchecker'+str(num))
        pchecker.speed('fastest')
        pchecker.penup()
        if num<4:
            pchecker.goto(-185-80+num*160-10,-283+5*80+7)
        elif num<8:
            pchecker.goto(-185+(num-4)*160-10,-283+80+5*80+7)
        elif num<12:
            pchecker.goto(-185-80+(num-8)*160-10,-283+160+5*80+7)
        num=num+1


    def ur(turtlename):
        turtlename.speed(3)
        turtlename.goto(turtlename.xcor()+80,turtlename.ycor()+80)
        #time.sleep(.3)
    def ul(turtlename):
        turtlename.speed(3)
        turtlename.goto(turtlename.xcor()-80,turtlename.ycor()+80)
        #time.sleep(.3)
    def dr(turtlename):
        turtlename.speed(3)
        turtlename.goto(turtlename.xcor()+80,turtlename.ycor()-80)
        #time.sleep(.3)
    def dl(turtlename):
        turtlename.speed(3)
        turtlename.goto(turtlename.xcor()-80,turtlename.ycor()-80)
        #time.sleep(.3)
    def kingme(turtlename):
        if 'p' not in str(turtlename):
            wn.addshape(r'purplemmino-removebg-preview_-_Copy-removebg-preview.gif')
            turtlename.shape(r'purplemmino-removebg-preview_-_Copy-removebg-preview.gif')


            numbers = ''.join([char for char in str(turtlename) if char.isdigit()])


            ppic=PhotoImage(file=r'Untitled-removebg-preview.gif')
            wn.addshape('checker'+str(numbers), Shape('image', ppic))
            turtlename.shape('checker'+str(numbers))




        
    
    #START MOVE ANIMATION
    time.sleep(1.5)
    ur(checker9)
    dr(pchecker2)


    ul(checker6)
    dr(pchecker0)


    ur(checker10)
    dr(pchecker5)


    ul(checker7)
    dl(pchecker0)


    ur(checker10)
    dl(pchecker1)


    ur(checker7)
    dl(pchecker4)


    ur(checker8)
    dl(pchecker9)


    ur(checker1)
    dl(pchecker10)


    ur(checker1)
    dl(pchecker10)


    ur(checker4)
    dl(pchecker5)


    ur(checker8)
    ur(checker8)
    pchecker5.hideturtle()
    dl(pchecker6)
    dl(pchecker6)
    checker8.hideturtle()


    ul(checker7)
    ul(checker7)
    pchecker2.hideturtle()
    dl(pchecker3)


    ur(checker9)
    ur(checker9)
    pchecker3.hideturtle()
    dl(pchecker7)
    dl(pchecker7)
    checker9.hideturtle()


    ul(checker7)
    dl(pchecker11)


    ul(checker7)
    kingme(checker7)
    dl(pchecker11)


    ul(checker10)
    # TODO figure out best move for purple
    dr(pchecker1)


    ul(checker6)
    ul(checker6)
    pchecker1.hideturtle()
    ur(checker6)
    ur(checker6)
    pchecker10.hideturtle()
    dr(pchecker9)


    ur(checker6)
    kingme(checker6)
    dl(pchecker9)


    dl(checker6)
    dl(checker6)
    dl(pchecker7)


    ul(checker10)
    dr(pchecker7)
    dr(pchecker7)
    checker1.hideturtle()


    ul(checker3)
    ul(checker3)
    pchecker7.hideturtle()
    dr(pchecker9)


    dr(checker6)
    dr(checker6)
    pchecker6.hideturtle()
    dl(pchecker9)
    dl(pchecker9)
    checker4.hideturtle()


    ur(checker10)
    kingme(checker10)
    dr(pchecker4)


    dl(checker10)
    dl(pchecker11)


    ul(checker6)
    ul(checker6)
    pchecker11.hideturtle()
    dr(pchecker0)


    dl(checker10)
    dl(checker10)
    dr(pchecker10)


    ur(checker6)
    dr(pchecker8)


    ul(checker5)
    ul(checker5)
    pchecker0.hideturtle()
    ur(checker5)
    ur(checker5)
    pchecker4.hideturtle()
    ul(checker5)
    ul(checker5)
    kingme(checker5)
    pchecker8.hideturtle()
    pchecker9.hideturtle()

    card_image = r"Happy Birthday (1).gif"
    wn.addshape(card_image)

    card = trtl.Turtle()

    def draw_image(active_card):
        active_card.shape(card_image)
        wn.update()

    card.penup()
    card.goto(-1000, 0)


    draw_image(card)
    card.goto(0,0)
    time.sleep(3.5)
    wn.bye()

click_to_play = trtl.Turtle()
click_to_play.hideturtle()
click_to_play.penup()
click_to_play.goto(600,0)
click_to_play.write('Click "a" to \n    Play', font=("Times New Roman", 50, "normal"))

click_to_play.goto(600, -30)
click_to_play.write("    (Capslock off)", font=("Times New Romans", 25, 'normal'))
wn.onkeypress(card,"a")
wn.listen()
wn.mainloop()






running_videos(r"newthing0001-0250-ezgif.com-reverse-video.mp4")
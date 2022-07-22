import turtle
window = turtle.Screen()
turtle.title("LECC+")
window.setup(width=579,height=592)
window.bgpic('FRONT.png')
window.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor('#111111')
pen.color('black')
pen.pensize(8)

#Button for C at first page
Button_x_c = -262
Button_y_c = 24
ButtonLength_c = 101
ButtonWidth_c = 65

#Button for CPP at first page
Button_x_cpp = -262
Button_y_cpp = -60
ButtonLength_cpp = 101
ButtonWidth_cpp = 65

#Button for ABOUT US at first page
Button_x_aboutus_circle = -210
Button_y_aboutus_cirlce = -126
Button_R_aboutus_circle = 44

#Return button (around us page)
Button_x_aboutus_return_circle = -237
Button_y_aboutus_return_circle = -230
Button_R_aboutus_return_circle = 23


#Button for HOW TO PLAY BUTTON
Button_x_how = -178
Button_y_how = -7
ButtonLength_how = 359
ButtonWidth_how = 94

#Button for PLAY BUTTON page 2
Button_x_play2 = -125
Button_y_play2 = 138
ButtonLength_play2 = 254
ButtonWidth_play2 = 91

#Return button (from Play button)
Button_x_play_return_circle = -241
Button_y_play_return_circle = -219
Button_R_play_return_circle = 34


#Return button (from How to play )
Button_x_how_return_circle = -233
Button_y_how_return_circle = -212
Button_R_how_return_circle = 27

#Return button (what is programming page)
Button_x_returnwip = -235
Button_y_returnwip = -221
Button_R_returnwip = 25

#Return button (why should we learn programming page)
Button_x_returnwswlp = -252
Button_y_returnwswlp = -245
Button_R_returnwswlp = 18

#Button for PLAY GAME at first page
Button_x_play = -123
Button_y_play = -285
ButtonLength_play = 264
ButtonWidth_play = 73

#Button for WHAT IS PROGRAMMING at first page
Button_x_what = 91
Button_y_what = 7
ButtonLength_what = 177
ButtonWidth_what = 80

#Button for WHAT IS PROGRAMMING at first page
Button_x_what_circle = 181
Button_y_what_cirlce = 0
Button_R_what_circle = 23

#Button for WHY LEARN PROGRAMMING at first page
Button_x_why = 91
Button_y_why = -128
ButtonLength_why = 177
ButtonWidth_why = 80

#Button for WHY LEARN PROGRAMMING at first page
Button_x_why_circle = 178
Button_y_why_cirlce = -136
Button_R_why_circle = 23

#Button for beginner C - second page
Button_x_begc = -275
Button_y_begc = 73
ButtonLength_begc = 197
ButtonWidth_begc = 80

#Button for advanced C - second page
Button_x_advc = -275
Button_y_advc = -95
ButtonLength_advc = 197
ButtonWidth_advc = 80

#Button for beginner CPP - second page
Button_x_begcpp = -275
Button_y_begcpp = 73
ButtonLength_begcpp = 197
ButtonWidth_begcpp = 80

#Button for advanced CPP - second page
Button_x_advcpp = -275
Button_y_advcpp = -95
ButtonLength_advcpp = 197
ButtonWidth_advcpp = 80

#Button for lecture 1 - third page
Button_x_lec1 = -203
Button_y_lec1 = 187
ButtonLength_lec1 = 195
ButtonWidth_lec1 = 66

#Button for lecture 2 - third page
Button_x_lec2 = -265
Button_y_lec2 = 101
ButtonLength_lec2 = 195
ButtonWidth_lec2 = 66

#Button for lecture 3 - third page
Button_x_lec3 = -282
Button_y_lec3 = 6
ButtonLength_lec3 = 195
ButtonWidth_lec3 = 66

#Button for lecture 4 - third page
Button_x_lec4 = -265
Button_y_lec4 = -87
ButtonLength_lec4 = 195
ButtonWidth_lec4 = 66

#Button for lecture 5 - third page
Button_x_lec5 = -203
Button_y_lec5 = -176
ButtonLength_lec5 = 195
ButtonWidth_lec5 = 66

#Button for Return Home Page  - third page
Button_x_returnhm = -68
Button_y_returnhm = -266
ButtonLength_returnhm = 182
ButtonWidth_returnhm = 68

#Button for Return Home Page  - third page
Button_x_returnhmcircle1 = -60
Button_y_returnhmcircle1 = -231
Button_R_returnhmcircle1 = 35

#Button for Return Home Page  - third page
Button_x_returnhmcircle2 = 111
Button_y_returnhmcircle2 = -231
Button_R_returnhmcircle2 = 35

#Button for next page on lectures
Button_x_lecture_circle1_next = 200
Button_y_lecture_circle1_next = -266
Button_R_lecture_circle1_next = 24

#Button for previous page on lectures
Button_x_lecture_circle2_prev = -197
Button_y_lecture_circle2_prev = -265
Button_R_lecture_circle2_prev = 24

#Button for return to lectures (to third page)
Button_x_lecture_circle3_center = 49
Button_y_lecture_circle3_center = -266
Button_R_lecture_circle3_center = 23

#Button for return to lectures (to third page)
Button_x_returntolecture = -53
Button_y_returntolecture = -283
ButtonLength_returntolecture = 91
ButtonWidth_returntolecture = 35

#Button to play game from end of lectures
Button_x_playfromlecture = 125
Button_y_playfromlecture = -290
ButtonLength_playfromlecture = 97
ButtonWidth_playfromlecture = 36

#Button to return home from end of lectures
Button_x_returnhm_lec = -35
Button_y_returnhm_lec = -282
ButtonLength_returnhm_lec = 86
ButtonWidth_returnhm_lec = 30

#Button to return home from end of lectures
Button_x_returnhm_lec_circle1_right = 48
Button_y_returnhm_lec_circle1_right = -268
Button_R_returnhm_lec_circle1_right = 11

#Button to return home from end of lectures
Button_x_returnhm_lec_circle1_left = -40
Button_y_returnhm_lec_circle1_left = -269
Button_R_returnhm_lec_circle1_left = 17







#calculating the distance between two points
def distance (p1,p2):
    return(p2[0] - p1[0])**2 + (p2[1]-p1[1])**2

#printing coordinatesto help with placing buttons
def printcoordinates(x,y):
    print(x,y)

#Function of first page and buttons inside
def btnclickfirstpage(x,y):

    if Button_x_cpp <= x <= Button_x_cpp + ButtonLength_cpp:
        if Button_y_cpp <= y <= Button_y_cpp + ButtonWidth_cpp:

            window.clear()
            window.bgpic('LEC C & C++ BCG.png')
            turtle.onscreenclick(btnclicksecondpage,1)
            turtle.listen()

    if Button_x_c <= x <= Button_x_c + ButtonLength_c:
        if Button_y_c <= y <= Button_y_c + ButtonWidth_c:

            window.clear()
            window.bgpic('LEC C & C++ BCG.png')
            turtle.onscreenclick(btnclicksecondpageC,1)
            turtle.listen()

    if distance((Button_x_aboutus_circle,Button_y_aboutus_cirlce),(x,y)) <= Button_R_aboutus_circle**2:

            window.clear()
            window.bgpic('ABOUT US.png')
            turtle.onscreenclick(btnclickaboutusreturn,1)
            turtle.listen()

    if Button_x_what <= x <= Button_x_what + ButtonLength_what:
        if Button_y_what <= y <= Button_y_what + ButtonWidth_what:

            window.clear()
            window.bgpic('WHAT IS PROGRAMMING.png')
            turtle.onscreenclick(btnclickwip,1)
            turtle.listen()

    if distance((Button_x_what_circle,Button_y_what_cirlce),(x,y)) <= Button_R_what_circle**2:

            window.clear()
            window.bgpic('WHAT IS PROGRAMMING.png')
            turtle.onscreenclick(btnclickwip,1)
            turtle.listen()

    if Button_x_why <= x <= Button_x_why + ButtonLength_why:
        if Button_y_why <= y <= Button_y_why + ButtonWidth_why:

            window.clear()
            window.bgpic('WHY SHOULD WE LEARN PROGRAMMING.png')
            turtle.onscreenclick(btnclickwswlp,1)
            turtle.listen()

    if distance((Button_x_why_circle,Button_y_why_cirlce),(x,y)) <= Button_R_why_circle**2:

            window.clear()
            window.bgpic('WHY SHOULD WE LEARN PROGRAMMING.png')
            turtle.onscreenclick(btnclickwswlp,1)
            turtle.listen()

    if Button_x_play <= x <= Button_x_play + ButtonLength_play:
        if Button_y_play <= y <= Button_y_play + ButtonWidth_play:

            window.clear()
            window.bgpic('GAME_FRONT_PAGE.png')
            turtle.onscreenclick(btnclickplay,1)
            turtle.listen()







#Function that returns you back to homepage from button "play"
def btnclickplay(x,y):
    if distance((Button_x_play_return_circle,Button_y_play_return_circle),(x,y)) <= Button_R_play_return_circle**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if Button_x_how <= x <= Button_x_how + ButtonLength_how:
        if Button_y_how <= y <= Button_y_how + ButtonWidth_how:

            window.clear()
            window.bgpic('HOW TO PLAY.png')
            turtle.onscreenclick(btnclickhowtoplayreturn,1)
            turtle.listen()

    if Button_x_play2 <= x <= Button_x_play2 + ButtonLength_play2:
        if Button_y_play2 <= y <= Button_y_play2 + ButtonWidth_play2:

            window.clear()
            window.bgpic('GAME!!!')
            turtle.onscreenclick(printcoordinates,1)
            turtle.listen()



#Function that returns you back from how to play
def btnclickhowtoplayreturn(x,y):
    if distance((Button_x_how_return_circle,Button_y_how_return_circle),(x,y)) <= Button_R_how_return_circle**2:

            window.clear()
            window.bgpic('GAME_FRONT_PAGE.png')
            turtle.onscreenclick(btnclickplay,1)
            turtle.listen()


#Function that returns you back from about us to home
def btnclickaboutusreturn(x,y):
    if distance((Button_x_aboutus_return_circle,Button_y_aboutus_return_circle),(x,y)) <= Button_R_aboutus_return_circle**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#Return button function for WHAT IS PROGRAMMING page
def btnclickwip(x,y):

    if distance((Button_x_returnwip,Button_y_returnwip),(x,y)) <= Button_R_returnwip**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#Return button function for WHY SHOULD WE LEARN PROGRAMMING page
def btnclickwswlp(x,y):

    if distance((Button_x_returnwswlp,Button_y_returnwswlp),(x,y)) <= Button_R_returnwswlp**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#Function of the second page with buttons beginner and advanced C button
def btnclicksecondpageC(x,y):

    if Button_x_begc <= x <= Button_x_begc + ButtonLength_begc:
        if Button_y_begc <= y <= Button_y_begc + ButtonWidth_begc:

            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegc,1)
            turtle.listen()

    if Button_x_advc <= x <= Button_x_advc + ButtonLength_advc:
        if Button_y_advc <= y <= Button_y_advc + ButtonWidth_advc:

            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvC,1)
            turtle.listen()

#Function of the second page with buttons beginner and advanced Cpp button
def btnclicksecondpage(x,y):


    if Button_x_begcpp <= x <= Button_x_begcpp + ButtonLength_begcpp:
        if Button_y_begcpp <= y <= Button_y_begcpp + ButtonWidth_begcpp:

            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegcpp,1)
            turtle.listen()

    if Button_x_advcpp <= x <= Button_x_advcpp + ButtonLength_advcpp:
        if Button_y_advcpp <= y <= Button_y_advcpp + ButtonWidth_advcpp:

            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvCpp,1)
            turtle.listen()

#Function of the third page beginner C - ENRIKETA's lectures

def btnclickthirdpagebegc(x,y):
    if Button_x_lec1 <= x <= Button_x_lec1 + ButtonLength_lec1:
        if Button_y_lec1 <= y <= Button_y_lec1 + ButtonWidth_lec1:

            window.clear()
            window.bgpic('LESSON 1 ENRIKETA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial1_begc,1)
            turtle.listen()

    if Button_x_lec2 <= x <= Button_x_lec2 + ButtonLength_lec2:
        if Button_y_lec2 <= y <= Button_y_lec2 + ButtonWidth_lec2:

            window.clear()
            window.bgpic('LESSON 2 ENRIKETA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial2_begc,1)
            turtle.listen()

    if Button_x_lec3 <= x <= Button_x_lec3 + ButtonLength_lec3:
        if Button_y_lec3 <= y <= Button_y_lec3 + ButtonWidth_lec3:

            window.clear()
            window.bgpic('LESSON 3 ENRIKETA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial3_begc,1)
            turtle.listen()

    if Button_x_lec4 <= x <= Button_x_lec4 + ButtonLength_lec4:
        if Button_y_lec4 <= y <= Button_y_lec4 + ButtonWidth_lec4:

            window.clear()
            window.bgpic('LESSON 4 ENRIKETA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial4_begc,1)
            turtle.listen()

    if Button_x_lec5 <= x <= Button_x_lec5 + ButtonLength_lec5:
        if Button_y_lec5 <= y <= Button_y_lec5 + ButtonWidth_lec5:

            window.clear()
            window.bgpic('LESSON 5 ENRIKETA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial5_begc,1)
            turtle.listen()

    if Button_x_returnhm <= x <= Button_x_returnhm + ButtonLength_returnhm:
        if Button_y_returnhm <= y <= Button_y_returnhm + ButtonWidth_returnhm:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if distance((Button_x_returnhmcircle1,Button_y_returnhmcircle1),(x,y)) <= Button_R_returnhmcircle1**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if distance((Button_x_returnhmcircle2,Button_y_returnhmcircle2),(x,y)) <= Button_R_returnhmcircle2**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#The following functions are Enriketa's lectures and the buttons for each page
#From lecture 1 till 5 (The last lecture)
#Inside the functions are included buttons: nextpage, previouspage, turntohomescreen, turntolectures, playagame(This one is located in the last lecture)

def btnclick_part1_tutorial1_begc(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 1 ENRIKETA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial1_begc,1)
        turtle.listen()

def btnclick_part2_tutorial1_begc(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 ENRIKETA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial2_begc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 1 ENRIKETA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial1_begc,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegc,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpagebegc,1)
        turtle.listen()

def btnclick_part1_tutorial2_begc(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 ENRIKETA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial2_begc,1)
        turtle.listen()

def btnclick_part2_tutorial2_begc(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 ENRIKETA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial3_begc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 2 ENRIKETA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial2_begc,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegc,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpagebegc,1)
        turtle.listen()

def btnclick_part1_tutorial3_begc(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 ENRIKETA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_begc,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegc,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpagebegc,1)
        turtle.listen()

def btnclick_part1_tutorial4_begc(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 ENRIKETA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial4_begc,1)
        turtle.listen()

def btnclick_part2_tutorial4_begc(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 ENRIKETA-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial4_begc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 4 ENRIKETA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial3_begc,1)
        turtle.listen()

def btnclick_part3_tutorial4_begc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 ENRIKETA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_begc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 4 ENRIKETA-3.png')
        turtle.onscreenclick(btnclick_part2_tutorial4_begc,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegc,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpagebegc,1)
        turtle.listen()

def btnclick_part1_tutorial5_begc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 ENRIKETA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial5_begc,1)
        turtle.listen()

def btnclick_part2_tutorial5_begc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 ENRIKETA-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial5_begc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 5 ENRIKETA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_begc,1)
        turtle.listen()

def btnclick_part3_tutorial5_begc(x,y):
    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 5 ENRIKETA-2.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_begc,1)
        turtle.listen()

    if Button_x_playfromlecture <= x <= Button_x_playfromlecture+ButtonLength_playfromlecture:
        if Button_y_playfromlecture <= y <= Button_y_playfromlecture+ButtonWidth_playfromlecture:
            window.clear()
            window.bgpic('GAME_FRONT_PAGE.png')
            turtle.onscreenclick(btnclickplay,1)
            turtle.listen()

    if distance((Button_x_returnhm_lec_circle1_left,Button_y_returnhm_lec_circle1_left),(x,y)) <= Button_R_returnhm_lec_circle1_left**2:
        window.clear()
        window.bgpic('FRONT.png')
        turtle.onscreenclick(btnclickfirstpage,1)
        turtle.listen()

    if distance((Button_x_returnhm_lec_circle1_right,Button_y_returnhm_lec_circle1_right),(x,y)) <= Button_R_returnhm_lec_circle1_right**2:
        window.clear()
        window.bgpic('FRONT.png')
        turtle.onscreenclick(btnclickfirstpage,1)
        turtle.listen()

    if Button_x_returnhm_lec <= x <= Button_x_returnhm_lec+ButtonLength_returnhm_lec:
        if Button_y_returnhm_lec <= y <= Button_y_returnhm_lec+ButtonWidth_returnhm_lec:
            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#Function of the third page advanced C - EVA's lectures

def btnclickthirdpageadvC(x,y):
    if Button_x_lec1 <= x <= Button_x_lec1 + ButtonLength_lec1:
        if Button_y_lec1 <= y <= Button_y_lec1 + ButtonWidth_lec1:

            window.clear()
            window.bgpic('LESSON 1 EVA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial1_advc,1)
            turtle.listen()

    if Button_x_lec2 <= x <= Button_x_lec2 + ButtonLength_lec2:
        if Button_y_lec2 <= y <= Button_y_lec2 + ButtonWidth_lec2:

            window.clear()
            window.bgpic('LESSON 2 EVA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial2_advc,1)
            turtle.listen()

    if Button_x_lec3 <= x <= Button_x_lec3 + ButtonLength_lec3:
        if Button_y_lec3 <= y <= Button_y_lec3 + ButtonWidth_lec3:

            window.clear()
            window.bgpic('LESSON 3 EVA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial3_advc,1)
            turtle.listen()

    if Button_x_lec4 <= x <= Button_x_lec4 + ButtonLength_lec4:
        if Button_y_lec4 <= y <= Button_y_lec4 + ButtonWidth_lec4:

            window.clear()
            window.bgpic('LESSON 4 EVA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial4_advc,1)
            turtle.listen()

    if Button_x_lec5 <= x <= Button_x_lec5 + ButtonLength_lec5:
        if Button_y_lec5 <= y <= Button_y_lec5 + ButtonWidth_lec5:

            window.clear()
            window.bgpic('LESSON 5 EVA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial5_advc,1)
            turtle.listen()

    if Button_x_returnhm <= x <= Button_x_returnhm + ButtonLength_returnhm:
        if Button_y_returnhm <= y <= Button_y_returnhm + ButtonWidth_returnhm:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if distance((Button_x_returnhmcircle1,Button_y_returnhmcircle1),(x,y)) <= Button_R_returnhmcircle1**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if distance((Button_x_returnhmcircle2,Button_y_returnhmcircle2),(x,y)) <= Button_R_returnhmcircle2**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#The following functions are EVA's lectures and the buttons for each page
#From lecture 1 till 5 (The last lecture)
#Inside the functions are included buttons: nextpage, previouspage, turntohomescreen, turntolectures, playagame(This one is located in the last lecture)

def btnclick_part1_tutorial1_advc(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 1 EVA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial1_advc,1)
        turtle.listen()

def btnclick_part2_tutorial1_advc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 1 EVA-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial1_advc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 1 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial1_advc,1)
        turtle.listen()

def btnclick_part3_tutorial1_advc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial2_advc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 1 EVA-3.png')
        turtle.onscreenclick(btnclick_part2_tutorial1_advc,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvC,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpageadvC,1)
        turtle.listen()

def btnclick_part1_tutorial2_advc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial3_advc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 2 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial2_advc,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvC,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpageadvC,1)
        turtle.listen()

def btnclick_part1_tutorial3_advc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 EVA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial3_advc,1)
        turtle.listen()

def btnclick_part2_tutorial3_advc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_advc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 3 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial3_advc,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvC,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpageadvC,1)
        turtle.listen()

def btnclick_part1_tutorial4_advc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 EVA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial4_advc,1)
        turtle.listen()

def btnclick_part2_tutorial4_advc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_advc,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 4 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_advc,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvC,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpageadvC,1)
        turtle.listen()

def btnclick_part1_tutorial5_advc(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 EVA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial5_advc,1)
        turtle.listen()

def btnclick_part2_tutorial5_advc(x,y):

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 5 EVA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_advc,1)
        turtle.listen()

    if Button_x_playfromlecture <= x <= Button_x_playfromlecture+ButtonLength_playfromlecture:
        if Button_y_playfromlecture <= y <= Button_y_playfromlecture+ButtonWidth_playfromlecture:
            window.clear()
            window.bgpic('GAME_FRONT_PAGE.png')
            turtle.onscreenclick(btnclickplay,1)
            turtle.listen()

    if distance((Button_x_returnhm_lec_circle1_left,Button_y_returnhm_lec_circle1_left),(x,y)) <= Button_R_returnhm_lec_circle1_left**2:
        window.clear()
        window.bgpic('FRONT.png')
        turtle.onscreenclick(btnclickfirstpage,1)
        turtle.listen()

    if distance((Button_x_returnhm_lec_circle1_right,Button_y_returnhm_lec_circle1_right),(x,y)) <= Button_R_returnhm_lec_circle1_right**2:
        window.clear()
        window.bgpic('FRONT.png')
        turtle.onscreenclick(btnclickfirstpage,1)
        turtle.listen()

    if Button_x_returnhm_lec <= x <= Button_x_returnhm_lec+ButtonLength_returnhm_lec:
        if Button_y_returnhm_lec <= y <= Button_y_returnhm_lec+ButtonWidth_returnhm_lec:
            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#Function of the third page beginner CPP - KLAUDIA's lectures

def btnclickthirdpagebegcpp(x,y):
    if Button_x_lec1 <= x <= Button_x_lec1 + ButtonLength_lec1:
        if Button_y_lec1 <= y <= Button_y_lec1 + ButtonWidth_lec1:

            window.clear()
            window.bgpic('LESSON 1 KLAUDIA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial1_begcpp,1)
            turtle.listen()

    if Button_x_lec2 <= x <= Button_x_lec2 + ButtonLength_lec2:
        if Button_y_lec2 <= y <= Button_y_lec2 + ButtonWidth_lec2:

            window.clear()
            window.bgpic('LESSON 2 KLAUDIA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial2_begcpp,1)
            turtle.listen()

    if Button_x_lec3 <= x <= Button_x_lec3 + ButtonLength_lec3:
        if Button_y_lec3 <= y <= Button_y_lec3 + ButtonWidth_lec3:

            window.clear()
            window.bgpic('LESSON 3 KLAUDIA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial3_begcpp,1)
            turtle.listen()

    if Button_x_lec4 <= x <= Button_x_lec4 + ButtonLength_lec4:
        if Button_y_lec4 <= y <= Button_y_lec4 + ButtonWidth_lec4:

            window.clear()
            window.bgpic('LESSON 4 KLAUDIA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial4_begcpp,1)
            turtle.listen()

    if Button_x_lec5 <= x <= Button_x_lec5 + ButtonLength_lec5:
        if Button_y_lec5 <= y <= Button_y_lec5 + ButtonWidth_lec5:

            window.clear()
            window.bgpic('LESSON 5 KLAUDIA-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial5_begcpp,1)
            turtle.listen()

    if Button_x_returnhm <= x <= Button_x_returnhm + ButtonLength_returnhm:
        if Button_y_returnhm <= y <= Button_y_returnhm + ButtonWidth_returnhm:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if distance((Button_x_returnhmcircle1,Button_y_returnhmcircle1),(x,y)) <= Button_R_returnhmcircle1**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if distance((Button_x_returnhmcircle2,Button_y_returnhmcircle2),(x,y)) <= Button_R_returnhmcircle2**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#The following functions are KLAUDIA's lectures and the buttons for each page
#From lecture 1 till 5 (The last lecture)
#Inside the functions are included buttons: nextpage, previouspage, turntohomescreen, turntolectures, playagame(This one is located in the last lecture)

def btnclick_part1_tutorial1_begcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 1 KLAUDIA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial1_begcpp,1)
        turtle.listen()


def btnclick_part2_tutorial1_begcpp(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial2_begcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 1 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial1_begcpp,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegcpp,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpagebegcpp,1)
        turtle.listen()

def btnclick_part1_tutorial2_begcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 KLAUDIA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial2_begcpp,1)
        turtle.listen()

def btnclick_part2_tutorial2_begcpp(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial3_begcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 2 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial2_begcpp,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegcpp,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpagebegcpp,1)
        turtle.listen()

def btnclick_part1_tutorial3_begcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 KLAUDIA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial3_begcpp,1)
        turtle.listen()

def btnclick_part2_tutorial3_begcpp(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 KLAUDIA-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial3_begcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 3 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial3_begcpp,1)
        turtle.listen()

def btnclick_part3_tutorial3_begcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_begcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 3 KLAUDIA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial3_begcpp,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegcpp,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpagebegcpp,1)
        turtle.listen()

def btnclick_part1_tutorial4_begcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 KLAUDIA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial4_begcpp,1)
        turtle.listen()

def btnclick_part2_tutorial4_begcpp(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 KLAUDIA-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial4_begcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 4 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_begcpp,1)
        turtle.listen()

def btnclick_part3_tutorial4_begcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 KLAUDIA-4.png')
        turtle.onscreenclick(btnclick_part4_tutorial4_begcpp,1)
        turtle.listen()

def btnclick_part4_tutorial4_begcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_begcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 4 KLAUDIA-3.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_begcpp,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpagebegcpp,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpagebegcpp,1)
        turtle.listen()

def btnclick_part1_tutorial5_begcpp(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 KLAUDIA-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial5_begcpp,1)
        turtle.listen()

def btnclick_part2_tutorial5_begcpp(x,y):
    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 KLAUDIA-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial5_begcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 5 KLAUDIA-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_begcpp,1)
        turtle.listen()

def btnclick_part3_tutorial5_begcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 KLAUDIA-4.png')
        turtle.onscreenclick(btnclick_part4_tutorial5_begcpp,1)
        turtle.listen()

def btnclick_part4_tutorial5_begcpp(x,y):

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 5 KLAUDIA-3.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_begcpp,1)
        turtle.listen()

    if Button_x_playfromlecture <= x <= Button_x_playfromlecture+ButtonLength_playfromlecture:
        if Button_y_playfromlecture <= y <= Button_y_playfromlecture+ButtonWidth_playfromlecture:
            window.clear()
            window.bgpic('GAME_FRONT_PAGE.png')
            turtle.onscreenclick(btnclickplay,1)
            turtle.listen()

    if distance((Button_x_returnhm_lec_circle1_left,Button_y_returnhm_lec_circle1_left),(x,y)) <= Button_R_returnhm_lec_circle1_left**2:
        window.clear()
        window.bgpic('FRONT.png')
        turtle.onscreenclick(btnclickfirstpage,1)
        turtle.listen()

    if distance((Button_x_returnhm_lec_circle1_right,Button_y_returnhm_lec_circle1_right),(x,y)) <= Button_R_returnhm_lec_circle1_right**2:
        window.clear()
        window.bgpic('FRONT.png')
        turtle.onscreenclick(btnclickfirstpage,1)
        turtle.listen()

    if Button_x_returnhm_lec <= x <= Button_x_returnhm_lec+ButtonLength_returnhm_lec:
        if Button_y_returnhm_lec <= y <= Button_y_returnhm_lec+ButtonWidth_returnhm_lec:
            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#Function of the third page advanced CPP - ENSILD's lectures
def btnclickthirdpageadvCpp(x,y):
    if Button_x_lec1 <= x <= Button_x_lec1 + ButtonLength_lec1:
        if Button_y_lec1 <= y <= Button_y_lec1 + ButtonWidth_lec1:

            window.clear()
            window.bgpic('LESSON 1 ENSILD-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial1_advcpp,1)
            turtle.listen()

    if Button_x_lec2 <= x <= Button_x_lec2 + ButtonLength_lec2:
        if Button_y_lec2 <= y <= Button_y_lec2 + ButtonWidth_lec2:

            window.clear()
            window.bgpic('LESSON 2 ENSILD-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial2_advcpp,1)
            turtle.listen()

    if Button_x_lec3 <= x <= Button_x_lec3 + ButtonLength_lec3:
        if Button_y_lec3 <= y <= Button_y_lec3 + ButtonWidth_lec3:

            window.clear()
            window.bgpic('LESSON 3 ENSILD-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial3_advcpp,1)
            turtle.listen()

    if Button_x_lec4 <= x <= Button_x_lec4 + ButtonLength_lec4:
        if Button_y_lec4 <= y <= Button_y_lec4 + ButtonWidth_lec4:

            window.clear()
            window.bgpic('LESSON 4 ENSILD-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial4_advcpp,1)
            turtle.listen()

    if Button_x_lec5 <= x <= Button_x_lec5 + ButtonLength_lec5:
        if Button_y_lec5 <= y <= Button_y_lec5 + ButtonWidth_lec5:

            window.clear()
            window.bgpic('LESSON 5 ENSILD-1.png')
            turtle.onscreenclick(btnclick_part1_tutorial5_advcpp,1)
            turtle.listen()

    if Button_x_returnhm <= x <= Button_x_returnhm + ButtonLength_returnhm:
        if Button_y_returnhm <= y <= Button_y_returnhm + ButtonWidth_returnhm:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if distance((Button_x_returnhmcircle1,Button_y_returnhmcircle1),(x,y)) <= Button_R_returnhmcircle1**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

    if distance((Button_x_returnhmcircle2,Button_y_returnhmcircle2),(x,y)) <= Button_R_returnhmcircle2**2:

            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()

#The following functions are Ensildi's lectures and the buttons for each page
#From lecture 1 till 5 (The last lecture)
#Inside the functions are included buttons: nextpage, previouspage, turntohomescreen, turntolectures, playagame(This one is located in the last lecture)

def btnclick_part1_tutorial1_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 1 ENSILD-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial1_advcpp,1)
        turtle.listen()

def btnclick_part2_tutorial1_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial2_advcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 1 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial1_advcpp,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvCpp,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpageadvCpp,1)
        turtle.listen()

def btnclick_part1_tutorial2_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 ENSILD-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial2_advcpp,1)
        turtle.listen()

def btnclick_part2_tutorial2_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 ENSILD-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial2_advcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 2 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial2_advcpp,1)
        turtle.listen()

def btnclick_part3_tutorial2_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 2 ENSILD-4.png')
        turtle.onscreenclick(btnclick_part4_tutorial2_advcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 2 ENSILD-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial2_advcpp,1)
        turtle.listen()

def btnclick_part4_tutorial2_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial3_advcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 2 ENSILD-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial2_advcpp,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvCpp,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpageadvCpp,1)
        turtle.listen()

def btnclick_part1_tutorial3_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 ENSILD-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial3_advcpp,1)
        turtle.listen()

def btnclick_part2_tutorial3_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 3 ENSILD-3.png')
        turtle.onscreenclick(btnclick_part3_tutorial3_advcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 3 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial3_advcpp,1)
        turtle.listen()

def btnclick_part3_tutorial3_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_advcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 3 ENSILD-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial3_advcpp,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvCpp,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpageadvCpp,1)
        turtle.listen()

def btnclick_part1_tutorial4_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 4 ENSILD-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial4_advcpp,1)
        turtle.listen()

def btnclick_part2_tutorial4_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_advcpp,1)
        turtle.listen()

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 4 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial4_advcpp,1)
        turtle.listen()

    if Button_x_returntolecture <= x <= Button_x_returntolecture+ButtonLength_returntolecture:
        if Button_y_returntolecture <= y <= Button_y_returntolecture+ButtonWidth_returntolecture:
            window.clear()
            window.bgpic('LEC BCG.png')
            turtle.onscreenclick(btnclickthirdpageadvCpp,1)
            turtle.listen()

    if distance((Button_x_lecture_circle3_center,Button_y_lecture_circle3_center),(x,y)) <= Button_R_lecture_circle3_center**2:
        window.clear()
        window.bgpic('LEC BCG.png')
        turtle.onscreenclick(btnclickthirdpageadvCpp,1)
        turtle.listen()

def btnclick_part1_tutorial5_advcpp(x,y):

    if distance((Button_x_lecture_circle1_next,Button_y_lecture_circle1_next),(x,y)) <= Button_R_lecture_circle1_next**2:
        window.clear()
        window.bgpic('LESSON 5 ENSILD-2.png')
        turtle.onscreenclick(btnclick_part2_tutorial5_advcpp,1)
        turtle.listen()

def btnclick_part2_tutorial5_advcpp(x,y):

    if distance((Button_x_lecture_circle2_prev,Button_y_lecture_circle2_prev),(x,y)) <= Button_R_lecture_circle2_prev**2:
        window.clear()
        window.bgpic('LESSON 5 ENSILD-1.png')
        turtle.onscreenclick(btnclick_part1_tutorial5_advcpp,1)
        turtle.listen()

    if Button_x_playfromlecture <= x <= Button_x_playfromlecture+ButtonLength_playfromlecture:
        if Button_y_playfromlecture <= y <= Button_y_playfromlecture+ButtonWidth_playfromlecture:
            window.clear()
            window.bgpic('GAME_FRONT_PAGE.png')
            turtle.onscreenclick(btnclickplay,1)
            turtle.listen()

    if distance((Button_x_returnhm_lec_circle1_left,Button_y_returnhm_lec_circle1_left),(x,y)) <= Button_R_returnhm_lec_circle1_left**2:
        window.clear()
        window.bgpic('FRONT.png')
        turtle.onscreenclick(btnclickfirstpage,1)
        turtle.listen()

    if distance((Button_x_returnhm_lec_circle1_right,Button_y_returnhm_lec_circle1_right),(x,y)) <= Button_R_returnhm_lec_circle1_right**2:
        window.clear()
        window.bgpic('FRONT.png')
        turtle.onscreenclick(btnclickfirstpage,1)
        turtle.listen()

    if Button_x_returnhm_lec <= x <= Button_x_returnhm_lec+ButtonLength_returnhm_lec:
        if Button_y_returnhm_lec <= y <= Button_y_returnhm_lec+ButtonWidth_returnhm_lec:
            window.clear()
            window.bgpic('FRONT.png')
            turtle.onscreenclick(btnclickfirstpage,1)
            turtle.listen()









turtle.onscreenclick(btnclickfirstpage,1)
turtle.listen()


turtle.done()
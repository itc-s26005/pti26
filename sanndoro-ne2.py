import turtle
import random
import math

# ==========================================================
# maid_v3.py
# Part 1
# 基本設定・背景・共通関数
# ==========================================================

WIDTH = 700
HEIGHT = 700

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("#74B8DA")
screen.title("Maid Character V3")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

screen.tracer(False)


# ==========================================================
# 共通関数
# ==========================================================

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def fill_polygon(points, color):

    t.color(color)

    move(points[0][0], points[0][1])

    t.begin_fill()

    for p in points[1:]:
        t.goto(p)

    t.goto(points[0])

    t.end_fill()


def fill_circle(x, y, r, color):

    t.color(color)

    move(x, y-r)

    t.begin_fill()

    t.circle(r)

    t.end_fill()


def line(points, color, width=2):

    t.color(color)
    t.width(width)

    move(points[0][0], points[0][1])

    for p in points[1:]:
        t.goto(p)

    t.width(2)


# ==========================================================
# 背景
# ==========================================================

def sparkle(x, y, size):

    move(x, y)

    t.color("white")

    for _ in range(8):
        t.forward(size)
        t.backward(size * 2)
        t.forward(size)
        t.left(45)


def draw_background():

    random.seed(100)

    # 小さな光
    for _ in range(80):

        x = random.randint(-330,330)
        y = random.randint(-330,330)

        r = random.randint(1,3)

        fill_circle(x,y,r,"white")

    # 少し大きい光
    for _ in range(20):

        x = random.randint(-320,320)
        y = random.randint(-320,320)

        fill_circle(x,y,5,"#DDF8FF")

    # キラキラ
    sparkle(-260,-180,18)
    sparkle(240,170,12)
    sparkle(-180,220,10)
    sparkle(80,280,9)
    sparkle(250,-240,11)

    # グロー
    for r in [40,30,20]:

        fill_circle(-260,-180,r,"#AEE9FF")

    fill_circle(-260,-180,8,"white")


# ==========================================================
# カラーパレット
# ==========================================================

HAIR = "#8F8376"
HAIR_DARK = "#6F6458"
HAIR_LIGHT = "#B7AEA4"

SKIN = "#F5DDC8"

WHITE = "#FDFDFD"

BLACK = "#1D1D1D"

BLUE1 = "#8EA7FF"
BLUE2 = "#6B7BFF"
BLUE3 = "#3347B8"

RED = "#A11E2C"

GOLD = "#D5B04A"

PINK = "#F4A7B7"


# ==========================================================
# メイン
# ==========================================================

draw_background()

# Part2からここに追加していく

# ==========================================================
# Part 2
# 顔・首
# draw_background() の下に追加
# ==========================================================

def draw_face():

    # 輪郭
    face = [

        (-78,120),
        (-90,95),
        (-96,60),
        (-98,20),
        (-96,-20),
        (-90,-60),
        (-78,-98),

        (-60,-122),
        (-35,-142),
        (0,-148),

        (35,-142),
        (60,-122),

        (78,-98),
        (90,-60),
        (96,-20),
        (98,20),
        (96,60),
        (90,95),
        (78,120),

        (50,150),
        (20,168),
        (0,172),

        (-20,168),
        (-50,150)

    ]

    fill_polygon(face, SKIN)

    # あごを少し丸く見せる
    fill_circle(0,-132,18,SKIN)

    # 首
    neck = [

        (-18,-142),
        (18,-142),
        (16,-190),
        (-16,-190)

    ]

    fill_polygon(neck, SKIN)

    # 首の影
    shadow = [

        (-12,-145),
        (12,-145),
        (8,-172),
        (-8,-172)

    ]

    fill_polygon(shadow, "#E7C6AF")


def draw_ears():

    fill_circle(-92,28,12,SKIN)
    fill_circle(92,28,12,SKIN)


def draw_face_shadow():

    t.color("#EFCDB8")

    # 左影
    line([
        (-70,95),
        (-82,40),
        (-76,-20),
        (-60,-80)
    ], "#E8C4AC", 3)

    # 右影
    line([
        (70,95),
        (82,40),
        (76,-20),
        (60,-80)
    ], "#E8C4AC", 3)

    # あご
    line([
        (-25,-120),
        (0,-128),
        (25,-120)
    ], "#E8C4AC", 2)


def draw_cheeks():

    fill_circle(-48,-8,8,"#F7B8C5")
    fill_circle(48,-8,8,"#F7B8C5")


# ==========================================================
# Part2 描画
# ==========================================================
# ==========================================================
# Part 3
# 後ろ髪
# Part2の下（draw_cheeks()の後）に追加
# ==========================================================

def draw_back_hair():

    hair = [

        (-120,135),
        (-115,175),
        (-95,210),
        (-70,235),
        (-35,248),
        (0,252),
        (35,248),
        (70,235),
        (95,210),
        (115,175),
        (120,135),

        (118,90),
        (112,40),
        (108,-10),
        (100,-70),
        (92,-130),
        (78,-185),
        (58,-235),
        (32,-275),
        (0,-292),

        (-32,-275),
        (-58,-235),
        (-78,-185),
        (-92,-130),
        (-100,-70),
        (-108,-10),
        (-112,40),
        (-118,90)

    ]

    fill_polygon(hair, HAIR)


def draw_hair_shadow():

    shadow = [

        (-88,175),
        (-60,205),
        (-20,220),
        (20,220),
        (60,205),
        (88,175),

        (72,120),
        (55,70),
        (35,10),
        (20,-55),
        (10,-115),
        (0,-170),

        (-10,-115),
        (-20,-55),
        (-35,10),
        (-55,70),
        (-72,120)

    ]

    fill_polygon(shadow, HAIR_DARK)


def draw_hair_highlight():

    t.color(HAIR_LIGHT)
    t.width(4)

    line([
        (-25,205),
        (-18,150),
        (-15,90),
        (-12,20),
        (-10,-40)
    ], HAIR_LIGHT, 4)

    line([
        (0,215),
        (0,160),
        (0,95),
        (0,30),
        (0,-35)
    ], HAIR_LIGHT, 4)

    line([
        (25,205),
        (18,150),
        (15,90),
        (12,20),
        (10,-40)
    ], HAIR_LIGHT, 4)


def draw_side_hair():

    left = [

        (-92,125),
        (-120,70),
        (-118,10),
        (-110,-55),
        (-90,-105),
        (-70,-115),
        (-62,-40),
        (-68,35)

    ]

    fill_polygon(left, HAIR)

    right = [

        (92,125),
        (120,70),
        (118,10),
        (110,-55),
        (90,-105),
        (70,-115),
        (62,-40),
        (68,35)

    ]

    fill_polygon(right, HAIR)


# ==========================================================
# Part3 描画
# ※ draw_face() より前に描く
# ==========================================================

# 一番下の描画順をこのように変更してください。

draw_background()

draw_back_hair()
draw_hair_shadow()
draw_hair_highlight()
draw_side_hair()

draw_face()
draw_ears()
draw_face_shadow()
draw_cheeks()

screen.update()
screen.mainloop()
draw_face()
draw_ears()
draw_face_shadow()
draw_cheeks()
screen.update()
screen.mainloop()

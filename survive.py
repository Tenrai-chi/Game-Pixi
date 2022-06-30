import pygame
import random

pygame.init()
win_width = 1100  # Ширина окна
win_height = 700  # Высота окна
display = (win_width, win_height)  # Группировка ширины и высоты в одну переменную
win = pygame.display.set_mode(display)  # Дисплей

pygame.display.set_caption("Pixi")  # Шапка для программы
donut = pygame.image.load('images/ponchik.png')  # Спрайт пончика
walkRight = pygame.image.load('images/hero/pravo.png')  # Спрайт вправо
walkLeft = pygame.image.load('images/hero/levo.png')  # Спрайт влево
bg = pygame.image.load('images/bg/bg_score.jpg')  # Задний фон
playerStand = pygame.image.load('images/hero/idle.png')  # Спрайт стоя
font = "images/Maestroc.otf"
paw = pygame.image.load('images/life.png')  # Лапка

clock = pygame.time.Clock()  # Таймер
FPS = 30


x = 500  # Начальное положение игрока по х
y = 570  # Начальное положение игрока по у
width = 90  # Ширина игрока
height = 60  # высота игрока
speed = 18  # Ворость пикси
bust_pixi = 0.005  # Ускорение пикси
speed_donut = 6  # Скорость падения пончика
sp = 60  # Размер пончика
max_donut = 6  # Максимальное количество пончиков на экране
m_time_donut = 50  # Время для проявления пончика
time_donut = 0  # Таймер для пончика
score = 0
bust = 0.005  # Ускорение падения
bust_time = 0.01  # Уменьшение кулдауна падения
life = 3
s_paw = 52

white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

is_jump = False  # Проверка прыжка
jump_count = 10  # Задает параболу для прыжка
on_ground = True  # Проверка наличия земли под ногами


left = False  # Начальное положениие (смотрит на игрока)
right = False

donuts = []  # Массив с координатами пончиков


def text_format(message, text_font, text_size, text_color):
    """ Создание нового формата текста для отображения надписей """

    new_font = pygame.font.Font(text_font, text_size)
    new_text = new_font.render(message, False, text_color)

    return new_text


def food_coordinates():
    """ Создание координат пончиков """

    yp = 0  # Начальное положения по у
    xp = random.uniform(2, 1032)  # Начальное положение по х
    donuts.append([xp, yp])  # Запоминание начальных координат в списке


def food_draw():
    """ Отрисовка пончиков """

    for i in donuts:  # Для каждого пончика отрисовка по координатам
        win.blit(donut, (i[0], i[1]))


def life_draw():
    """ Отрисовка жизней """

    i = 1
    while i <= life:  # для каждой жизни отрисовка по координатами
        x_paw = 230 + s_paw * (i - 1) + 25 * (i - 1)
        i += 1
        win.blit(paw, (x_paw, 16))


def update_donut():
    """ Обновление координат пончика за 1 единицу времени """

    global score
    global speed_donut
    global bust
    global life
    for i, k in enumerate(donuts):
        speed_donut += bust
        k[1] += speed_donut  # Увеличение у для каждого пончика
        if k[1] >= 600:  # Если пончик коснулся земли, то он исчезает
            life -= 1
            del donuts[i]


# Main Menu
def main_menu():
    menu = True
    selected = "start"
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        #menu = False
                        return 1
                    if selected == "quit":
                        pygame.quit()
                        quit()

        win.fill(blue)
        title = text_format("Pixi", font, 90, yellow)
        if selected == "start":
            text_start = text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        win.blit(title, (win_width/2 - (title_rect[2]/2), 80))
        win.blit(text_start, (win_width/2 - (start_rect[2]/2), 300))
        win.blit(text_quit, (win_width/2 - (quit_rect[2]/2), 380))
        pygame.display.update()
        clock.tick(FPS)


def GameOver():
    menu = True
    selected = "quit"
    global life
    life = 3
    donuts.clear()
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        #menu = False
                        return 1
                    if selected == "quit":
                        pygame.quit()
                        quit()

        win.fill(blue)
        title = text_format("Pixi", font, 90, yellow)
        if selected == "start":
            text_start = text_format("Restart", font, 75, white)
        else:
            text_start = text_format("Restart", font, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        win.blit(title, (win_width/2 - (title_rect[2]/2), 80))
        win.blit(text_start, (win_width/2 - (start_rect[2]/2), 300))
        win.blit(text_quit, (win_width/2 - (quit_rect[2]/2), 380))
        pygame.display.update()
        clock.tick(FPS)


def drawWindow():
    """ Рисование """
    win.blit(bg, (0, 0))  # Фон
    food_draw()  # Отрисовка еды отдельной процедурой
    if left:
        win.blit(walkLeft, (x, y))  # Рисование бега влево
    elif right:
        win.blit(walkRight, (x, y))  # Рисование бега вправо
    else:
        win.blit(playerStand, (x, y))  # Рисование статики
    title = text_format("Score: " + str(score), font, 30, yellow)
    life_draw()
    win.blit(title, (75, 32))
    pygame.display.update()  # Обновление и вывод всех изменений на экран


def GameStart():
    global x
    global y
    global width
    global height
    global max_donut
    global m_time_donut
    global time_donut
    global is_jump
    global jump_count
    global left
    global right
    global score
    global bust_time

    run = True  # Основной цикл программы
    while run:
        if life <= 0:
            GameOver()

        else:
            clock.tick(30)  # Таймер обновления (30 кадров в секунду)
            update_donut()  # Идет обновление координат пончиков

            time_donut += 1  # Обновляется таймер
            if len(donuts) < max_donut:  # Проверка количества пончиков и таймера
                if time_donut >= m_time_donut - bust_time:
                    time_donut = 0
                    food_coordinates()  # Если проверка успешная, то создается новый пончик

            for i, k in enumerate(donuts):  # Проверка соприкасания пончика и кота
                if ((x + width >= k[0] and x + width <= k[0] + sp) or (x <= k[0] + sp and x >= k[0])
                   or (k[0] > x and k[0]+sp < x + width)) and (y <= k[1] + sp):
                    score += 1
                    del donuts[i]

            for event in pygame.event.get():  # Обрабатывание событий
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > 5:  # Нажатие влево
                x -= speed + bust_pixi
                left = True
                right = False
            elif keys[pygame.K_RIGHT] and x < win_width - 5 - width:  # Нажатие вправо
                x += speed+bust_pixi
                left = False
                right = True
            else:
                left = False
                right = False
            if on_ground:
                if not is_jump:
                    if keys[pygame.K_SPACE]:  # Прыжок
                        is_jump = True
                    elif keys[pygame.K_UP]:  # Прыжок
                        is_jump = True
                else:  # Описание параболы прыжка
                    if jump_count >= -10:
                        if jump_count < 0:
                            y += (jump_count ** 2) / 2
                        else:
                            y -= (jump_count ** 2) / 2
                        jump_count -= 1
                    else:
                        is_jump = False and on_ground is True
                        jump_count = 10

            drawWindow()


main_menu()
GameStart()
pygame.quit()

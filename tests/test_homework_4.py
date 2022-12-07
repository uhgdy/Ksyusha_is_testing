import random
from time import sleep


# 1. Написать тест перехода в рандомное видео для любой страницы из банеров(например /news) - получаем список всех
# банеров, выбираем любое видео, переходим на страницу видео тут можно добаввить асерт (сравнить название видео со
# страницы /news с названием в карточке видео если такая возможность есть

# 2. написать аналогичный тест для перехода в любое видео со страницы /news (можно взять доругую) из списка видео

# 1 - открытие активного баннера. Способ 1
def test_banner_active_1(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/")

    # пауза на рандомное число секунд, чтобы выбрать активный слайд
    sleep(random.randint(1, 100))
    page.locator("//*[@class='pen-video-carousel__slide pen-video-carousel__slide_short-active']").click()


# 1 - открытие активного баннера. Способ 2
def test_banner_active_2(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/")

    # рандомное число нажатий вправо
    r = random.randint(1, 10)

    # рандомное число нажатий влево
    l = random.randint(1, 10)

    while l != 0 and r != 0:
        if l != 0:
            page.get_by_role("button", name="Предыдущий слайд").first.click()
            l -= 1
        if r != 0:
            page.get_by_role("button", name="Следующий слайд").first.click()
            r -= 1

    page.locator("//*[@class='pen-video-carousel__slide pen-video-carousel__slide_short-active']").click()


# 1 - открытие неактивного баннера
def test_banner_active(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/feeds/auto/")
    page.get_by_role("button", name="Хорошо, продолжим").click()

    buf = page.locator("//*[@class='pen-video-carousel__slides-container']/./div")
    count = buf.count()
    banner = []

    for i in range(count):
        banner.append(buf.nth(i).get_attribute("data-slide"))

    video = []
    buf = page.locator("//*[@class='wdp-card-poster-module__image']")
    count = buf.count()
    for i in range(count):
        element = buf.nth(i)
        # get the text of the element/tag alt
        text = element.get_attribute("alt")
        # print the text
        video.append(text)

    # сравнение названий видео в баннерах и карточках
    # но тут что-то не уверна что правильно выводит
    banner1 = set(banner)
    video1 = set(video)
    print("\n*****************************\nОбщие видео: ", banner1.intersection(video1))

    t = True
    while t:
        banner_ = random.choice(banner)
        i = page.locator("//*[@data-slide = '" + banner_ + "']").get_attribute("class")
        if i != "pen-video-carousel__slide pen-video-carousel__slide_short-active":
            page.locator("//*[@data-slide = '" + banner_ + "']").click()
            t = False

    print("\n********************************************\n", banner)


# 2 написать аналогичный тест для перехода в любое видео со страницы /news (можно взять доругую) из списка видео
def test_open_video(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/feeds/auto/")
    page.get_by_role("button", name="Хорошо, продолжим").click()

    video = []
    buf = page.locator("//*[@class='wdp-card-poster-module__image']")
    count = buf.count()
    for i in range(count):
        element = buf.nth(i)
        # get the text of the element/tag alt
        text = element.get_attribute("alt")
        # print the text
        video.append(text)

    page.locator("//*[@alt = '" + random.choice(video) + "']").click()

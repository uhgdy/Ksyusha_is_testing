import random
from time import sleep
import playwright


# 1. Написать тест перехода в рандомное видео для любой страницы из банеров(например /news) - получаем список всех
# банеров, выбираем любое видео, переходим на страницу видео тут можно добаввить асерт (сравнить название видео со
# страницы /news с названием в карточке видео если такая возможность есть

# 2. написать аналогичный тест для перехода в любое видео со страницы /news (можно взять доругую) из списка видео

# 1 - открытие активного баннера. Способ 1
def test_banner_active_1(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/")

    # пауза на рандомное число секунд, чтобы выбрать активный слайд
    sleep(random.randint(1, 100)) # так нельзя!!!!
    page.locator("//*[@class='pen-video-carousel__slide pen-video-carousel__slide_short-active']").click()


# 1 - открытие активного баннера. Способ 2
# слишком сложно
def test_banner_active_2(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/")

    # рандомное число нажатий вправо
    r = random.randint(1, 10)

    # рандомное число нажатий влево
    l = random.randint(1, 10)

    while l != 0 and r != 0: # так нельзя!!!! переносить в функцию \ лучше через for
        if l != 0:
            page.get_by_role("button", name="Предыдущий слайд").first.click()
            l -= 1
        if r != 0:
            page.get_by_role("button", name="Следующий слайд").first.click()
            r -= 1

    page.locator("//*[@class='pen-video-carousel__slide pen-video-carousel__slide_short-active']").click()


# 1 - открытие неактивного баннера
def test_banner_active(creating_page):
    # Шаг1 - открытие страницы
    page = creating_page
    page.goto("https://rutube.ru/feeds/auto/")
    page.get_by_role("button", name="Хорошо, продолжим").click()

    # Шаг 2 - Получить список навзаний баннеров
    carousel_list = page.locator("//*[@class='pen-video-carousel__slides-container']/./div")

    # Шаг 3 - Выбрать любое видео и перейти на него
    active_banner_index = page.locator(
        "//*[@class='pen-video-carousel__slide pen-video-carousel__slide_inline-short-active']/./div/img").get_attribute(
        'data-key')
    index_lst = list(range(carousel_list.count()))
    index_lst.pop(int(active_banner_index))
    banner_index = random.choice(index_lst)
    element_banner = page.locator("//*[@class='pen-video-carousel__slides-container']/./div").nth(banner_index)
    banner_name = element_banner.get_attribute('data-slide')
    element_banner.click()

    # Шаг 4 - Проверить, что название видео с главной страницы совпадает с названием видео из карточки
    name_video = page.locator(
        "//*[@class='pen-page-header_video-options-header-wide pen-page-header_color-default pen-page-header_size-default']").get_attribute(
        "title")

    assert banner_name.partition('_')[2] == name_video, 'Название видео с главной страницы не совпадает с названием видео из карточки'



# 2 написать аналогичный тест для перехода в любое видео со страницы /news (можно взять доругую) из списка видео
def test_open_video(creating_page):
    # открытие страницы
    page = creating_page
    page.goto("https://rutube.ru/feeds/auto/")
    page.get_by_role("button", name="Хорошо, продолжим").click()

    # получение списка навзаний видео
    video_list = page.locator("//*[@class='wdp-card-poster-module__image']")

    # открытие рандомного видео
    banner_index = random.choice(list(range(video_list.count())))
    element_banner = page.locator("//*[@class='wdp-card-poster-module__image']/./div").nth(banner_index)
    name_video = element_banner.get_attribute("alt")
    element_banner.click()

    # получение название открытого видео

    name_open_video = page.locator(
        "//*[@class='pen-page-header_video-options-header-wide pen-page-header_color-default pen-page-header_size-default']").get_attribute(
        "title")

    assert name_video == name_open_video



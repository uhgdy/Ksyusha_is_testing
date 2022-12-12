import pytest
from playwright.sync_api import Playwright
from time import sleep

# отображение автарки на странице канала
def test_img_1(authorization_ru):
    authorization_ru.locator(".freyja_char-header-user-menu__userAvatar__p5-3v").click()
    #authorization.get_by_role("link", name="Тестовый тест").first.click()
    authorization_ru.locator("//*[@title='Тестовый тест']").click()
    authorization_ru.get_by_role("img",
                              name="https://pic.rutubelist.ru/user/db/44/db44ca5899cf73c015643b642ca57a33.jpg").click()
    name_img = authorization_ru.query_selector("//*[@class='pen-feed-banner__avatar-image']").get_attribute("alt")
    print(name_img)
    assert name_img != " " or len(name_img) != 0


# отображение автарки в шапке справа
# проверка сделана некорректно
def test_img_2(authorization_ru):
    name_img = authorization_ru.query_selector(
        "//*[@class='freyja_char-header-user-menu__userAvatar__p5-3v']").get_attribute("style")
    print(name_img)
    assert name_img != " " or len(name_img) != 0


# проверка беннеров / yt hf,jnftn )))))):
# 4. Вернуться на главную страницу
# 5. Нажать кнопку назад на карусели
# 6. Проверить, что произошла смена слайдов
# 7. Нажать кнопку далее на карусели
# 8. Поверить, что активный слайд из ш. 4 совпадает со активнм слайдом из после выполнения ш. 7
def test_banner(creating_page):
    page = creating_page
    page.goto("https://rutube.ru/")

    buf_1 = page.locator("//*[@class='pen-video-carousel__slide pen-video-carousel__slide_short-active']").get_attribute(
        "data-slide")
    page.get_by_role("button", name="Предыдущий слайд").first.click()

    buf_2 = page.locator("//*[@class='pen-video-carousel__slide pen-video-carousel__slide_short-active']").get_attribute(
        "data-slide")
    # пауза на 1 секунду
    sleep(1)
    page.get_by_role("button", name="Следующий слайд").first.click()

    buf_3 = page.locator("//*[@class='pen-video-carousel__slide pen-video-carousel__slide_short-active']").get_attribute(
        "data-slide")

    # шаг 6
    assert buf_1 != buf_2
    # шаг 8
    assert buf_1 == buf_3

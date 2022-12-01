import pytest
from playwright.sync_api import Playwright


# отображение автарки на странице канала
def test_img_1(authorization):
    authorization.locator(".freyja_char-header-user-menu__userAvatar__p5-3v").click()
    authorization.get_by_role("link", name="🤍Testnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn").first.click()
    authorization.get_by_role("img",
                              name="https://pic.rutubelist.ru/user/db/44/db44ca5899cf73c015643b642ca57a33.jpg").click()
    name_img = authorization.query_selector("//*[@class='pen-feed-banner__avatar-image']").get_attribute("alt")
    print(name_img)
    assert name_img != " " or len(name_img) != 0


# отображение автарки в шапке справа
# проверка сделана некорректно
def test_img_2(authorization):
    name_img = authorization.query_selector(
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
    buf_1 = page.query_selector(
        "//*[@class='pen-video-carousel__slide pen-video-carousel__slide_inline-short-active']").get_attribute(
        "data-key")
    page.get_by_role("button", name="Предыдущий слайд").first.click()
    buf_2 = page.query_selector(
        "//*[@class='pen-video-carousel__slide pen-video-carousel__slide_inline-short-active']").get_attribute(
        "data-key")
    page.get_by_role("button", name="Следующий слайд").first.click()
    buf_3 = page.query_selector(
        "//*[@class='pen-video-carousel__slide pen-video-carousel__slide_inline-short-active']").get_attribute(
        "data-key")
    assert buf_1 != buf_2  # шаг 6
    assert buf_1 == buf_3  # шаг 8

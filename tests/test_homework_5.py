import random

import pytest


# 1. Недоступность раздела "посмотреть позже" для неавторизованного пользователя:
# Предусловие:
#  - Пользователь не авторизован
# тест-кейс:
#  1. Перейти в боковое меню (слева)
#  2. Проверить, что раздел "посмотреть позже" отсутствует на странице

def test_partition_unavailable(creating_page):
    # Шаг1 - открытие страницы
    page = creating_page
    page.goto("https://rutube.ru/")
    page.get_by_role("button", name="Хорошо, продолжим").click()

    # Шаг1 - Перейти в боковое меню (слева)
    page.get_by_role("banner").get_by_role("button").first.click()

    # Шаг2 - Поиск раздела
    icon = page.locator("//*[@aria-label = 'Посмотреть позже']")

    assert icon.count() == 0


# 2. Добавление видео в "Посмотреть позже"
# Предусловие: пользователь авторизован

# тест-кейс:
#  1. Открыть любую страницу из бокового меню (games, podcasts, main,...etc)
#  2. Выбрать любое видео со страницы
#  3. Перейти в карточку видео
#  4. нажать на кнопку "Сохранить" под видео
#  5. Перейти в раздел "ПОсмотреть позже"
#  6. Проверить, что видео из ш.4 присутствует в списке на просмотр позже.

def random_video(page):
    # получение списка навзаний видео
    video_list = page.locator("//*[@class='wdp-card-poster-module__image']")

    # открытие рандомного видео
    video_index = random.choice(list(range(video_list.count())))
    element_video = page.locator("//*[@class='wdp-card-poster-module__image']").nth(video_index)

    return element_video


def test_adding_videos_to_list(authorization_ru):
    # Шаг1 - открытие страницы
    authorization_ru.goto("https://rutube.ru/feeds/auto/")
    authorization_ru.get_by_role("button", name="Хорошо, продолжим").click()

    # Шаг2-3 открытие видео
    video = random_video(authorization_ru)
    video.click()

    # Шаг4 - сохранить видео
    authorization_ru.get_by_role("button", name="Сохранить").click()

    # Шаг5 - открыть раздел
    authorization_ru.get_by_role("banner").get_by_role("button").first.click()
    authorization_ru.get_by_text("Посмотреть позже").click()

    authorization_ru.locator("title", has_text=video)


# 3. Проверка наличия раздела "Рекомендуем" в разделах feeds/...

# Тест кейс:
# 1. Открыть страницу /feeds/music
# 2. Проверить, что на странице есть раздел "Рекомендуем"
# Параметризовать тест для других страниц feeds/.. содержащих раздел Рекомендуем.

@pytest.mark.parametrize("feeds", ["https://rutube.ru/feeds/music/", "https://rutube.ru/tags/video/6716/", "https://rutube.ru/feeds/education/"])
def test_availability_of_recommendations(creating_page, feeds):
    # Шаг1. Открытие главной
    page = creating_page
    page.goto("https://rutube.ru/")
    page.get_by_role("button", name="Хорошо, продолжим").click()

    # Шаг2. Открытие страницы
    page.goto(feeds)

    # Шаг3. Проверка
    recommendations = page.locator('text = Рекомендуем')

    assert recommendations.count() != 0

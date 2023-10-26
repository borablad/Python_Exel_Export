import requests
from bs4 import BeautifulSoup
import base64


def get_image(query: str) -> str:
    try:
        # Формируем URL для поиска изображений на Google
        search_url = f"https://www.google.com/search?q={query}&tbm=isch"

        # Отправляем GET-запрос к Google
        response = requests.get(search_url)

        if response.status_code == 200:
            # Используем BeautifulSoup для парсинга HTML-кода страницы
            soup = BeautifulSoup(response.text, 'html.parser')

            # Находим первую ссылку на изображение
            img_tags = soup.find_all("img")

            for img_tag in img_tags:
                if "src" in img_tag.attrs:
                    image_url = img_tag["src"]
                    # Проверяем, является ли URL абсолютным
                    if image_url.startswith("http"):
                        return uplod_to_lfs_image(image_url)

        return "Картинка не найдена"

    except Exception as e:
        print(f"Произошла ошибка при поиске изображения: {str(e)}")
        return "Ошибка при поиске или отпрвке изображения"




def uplod_to_lfs_image(image_url: str) -> str:
    try:
        # Задаем URL для отправки POST-запроса, замените на нужный URL
        base_url = "https://lis.4dev.kz/upload/guestor"

        # Загружаем изображение из интернета
        response = requests.get(image_url)

        if response.status_code == 200:
            # Создаем объект FormData для передачи файла
            files = {'file': ('image.jpg', response.content, 'image/jpeg')}

            # Отправляем POST-запрос
            response = requests.post(base_url, files=files)

            if response.status_code == 200:
                url = response.text
                return url
            else:
                print("Ошибка при загрузке файла:", response.status_code, response.reason)
                return ""
        else:
            print("Ошибка при загрузке изображения:", response.status_code, response.reason)
            return ""

    except Exception as e:
        print("Произошла ошибка:", str(e))
        return ""
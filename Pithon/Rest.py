import requests
import json
import Utils

def send_post_category_request(prodict_dict):
    # Задайте URL, на который вы хотите отправить POST-запрос
    url = 'https://guester.gosu.kz/odata/Categories'  # Замените на актуальный URL

    # poster_id_product_id = prodict_dict['PosterID product_id (не менять!)']
    # poster_id_modificator_id = prodict_dict['PosterID modificator_id (не менять!)']
    # название = prodict_dict['Название']
    category_name = prodict_dict['Категория']
    # тип = prodict_dict['Тип']
    # себестоимость_без_ндс = prodict_dict['Себестоимость без НДС']
    # цена = prodict_dict['Цена']
    # наценка = prodict_dict['Наценка']
    # photo = prodict_dict['photo']

    if category_exists(category_name):
        return 

    # Создайте JSON-объект, который вы хотите отправить
    data = {
        "BrandId": "6539fe7996384b9e8d7e72e5",
        "Picture": Utils.get_image(category_name),
        "Name": category_name,
        "TaxId": "653a064c2e0a86d5f67f519c",
        "SalesPointsId": ["6539fe7996384b9e8d7e72e9"],
        "Type": 0
    }

    # Отправьте POST-запрос с JSON-объектом
    response = requests.post(url, json=data)

    # Проверьте статус кода ответа
    if response.status_code >= 200 and response.status_code < 300:
        print("Запрос успешно отправлен.")
    else:
        print(f"Произошла ошибка при отправке запроса. Статус код: {response.status_code}")
        print(response.text)  # Вывести текст ответа с дополнительной информацией, если есть

def send_post_product_request(prodict_dict):
    # Задайте URL, на который вы хотите отправить POST-запрос
    url = 'https://guester.gosu.kz/odata/Products'  # Замените на актуальный URL

    # poster_id_product_id = prodict_dict['PosterID product_id (не менять!)']
    # poster_id_modificator_id = prodict_dict['PosterID modificator_id (не менять!)']
    Name = prodict_dict['Название']
    category_name = prodict_dict['Категория']
    # тип = prodict_dict['Тип']
    # себестоимость_без_ндс = prodict_dict['Себестоимость без НДС']
    CostPrice = prodict_dict['Цена']
    # MarkupPercent = prodict_dict['Наценка']
    photo = prodict_dict['photo']

    # Создайте JSON-объект, который вы хотите отправить
    data = {
            "BrandId":"6539fe7996384b9e8d7e72e5",
            "Type":1,
            "CategoryId":get_category_id_by_name(category_name),
            "Name": Name,
            "Picture":photo,
            "CostPrice":CostPrice,
            "MarkupPercent":0,
            "SumWithoutPrice":CostPrice
            }
    print(data)
    # Отправьте POST-запрос с JSON-объектом
    response = requests.post(url, json=data)

    # Проверьте статус кода ответа
    if response.status_code >= 200 and response.status_code <300:
        print("Запрос успешно отправлен.")
    else:
        print(f"Произошла ошибка при отправке запроса. Статус код: {response.status_code}")
        print(response.text)  # Вывести текст ответа с дополнительной информацией, если есть



def category_exists(category_name):
    url = 'https://guester.gosu.kz/odata/Categories'
    
    # Выполняем GET-запрос
    response = requests.get(url)
    
    if response.status_code >= 200 and response.status_code < 300:
        categories_data = response.json()
        
        # Проверяем, есть ли категория с заданным названием
        for category in categories_data['value']:
            if category.get('Name') == category_name:
                return True
        
        # Если ни одной категории с заданным названием не найдено
        return False
    else:
        print(f"Произошла ошибка при выполнении GET-запроса. Статус код: {response.status_code}")
        return ""



def get_category_id_by_name(category_name):
    url = 'https://guester.gosu.kz/odata/Categories'
    
    # Выполняем GET-запрос
    response = requests.get(url)
    
    if response.status_code >= 200 and response.status_code <300:
        categories_data = response.json()
        
        # Поиск категории с заданным названием
        for category in categories_data['value']:
            if category.get('Name') == category_name:
                return category.get('Id')
        
        # Если категория с заданным названием не найдена
        return ""
    else:
        print(f"Произошла ошибка при выполнении GET-запроса. Статус код: {response.status_code}")
        return ""
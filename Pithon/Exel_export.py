import pandas as pd
import Utils


def read_excel_to_dataframe(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name)
        return df
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")
        return None

def dataframe_to_dict_with_custom_keys(data_frame):
    try:
        if data_frame is not None:
             # Загрузите вторую строку таблицы в качестве заголовков столбцов
            custom_columns = data_frame.iloc[0].to_list()
            # Удалите вторую строку из данных
            data_frame = data_frame.iloc[1:]
            data_frame.columns = custom_columns

            # Преобразуйте DataFrame в список словарей
            result_dict = data_frame.to_dict(orient='records')


            for record in result_dict:
                # Получите значение из поля "Название"
                query = record.get("Название", "")
                print(query)
                
                # Вызов функции get_image для получения значения для ключа "photo"
                photo = Utils.get_image(query)
                
                # Добавление ключа "photo" и значения в запись
                record["photo"] = photo

                #result_dict.append(record)


            return result_dict

        else:
            return None
    except Exception as e:
        print(f"Произошла ошибка при конвертации в словарь: {str(e)}")
        return None

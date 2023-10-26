import Exel_export
import Rest


# Пути и имена листов
file_path = "./ExelAtributes/export_products_231025.xlsx"
sheet_name = "Экспорт товаров, модификаци..."

# Использование функции
data_frame = Exel_export.read_excel_to_dataframe(file_path, sheet_name)

if data_frame is not None:
    print(data_frame)

if data_frame is not None:
    result_dict = Exel_export.dataframe_to_dict_with_custom_keys(data_frame)
    if result_dict:
        for record in result_dict:
            Rest.send_post_category_request(record)
        print("Заверщён 1-й цикл")

        for record in result_dict:
            Rest.send_post_product_request(record)
        print("Заверщён 2-й цикл")

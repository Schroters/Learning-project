import json
import pandas as pd
import os
pd.set_option('display.max_columns', 15)


# Слоаварь со всеми значениями для таблицы
item_all_dic = {'item': [], 'SalePriceBeforePromo': [], 'SalePriceTimePromo': [], 'DatePriceBeforePromo': [], 'ObjCode': [],
                'DiscountType': [], 'DiscountValue': [], 'DateBegin': [], 'DateEnd': [], 'PWCcode': [], 'Value': [],
                'FirstValue': [], 'LessOrEqual': [], 'File': []}


def work_single_file(js_string_func, name_file):
    for n in range(len(js_string_func['Information']['GoodsLists'])):
        for j in range(len(js_string_func['Information']['GoodsLists'][0]['Prices'])):
            for i in range(len(js_string_func['Information']['GoodsLists'][0]['Prices'][j]['Data'])):
                item_all_dic['item'].append(js_string_func['Information']['GoodsLists'][0]['Prices'][j]['Data'][i][0])
                item_all_dic['SalePriceBeforePromo'].append(js_string_func['Information']['GoodsLists'][0]['Prices'][j]['Data'][i][1])
                item_all_dic['SalePriceTimePromo'].append(js_string_func['Information']['GoodsLists'][0]['Prices'][j]['Data'][i][2])
                item_all_dic['DatePriceBeforePromo'].append(js_string_func['Information']['GoodsLists'][0]['Prices'][j]['Data'][i][3])
                item_all_dic['ObjCode'].append(js_string_func['Information']['GoodsLists'][0]['Prices'][j]['StoreCode'])
                item_all_dic['DiscountType'].append(js_string_func['Information']['GoodsLists'][0]['DiscountType'])
                item_all_dic['DiscountValue'].append(js_string_func['Information']['GoodsLists'][0]['DiscountValue'])
                item_all_dic['DateBegin'].append(js_string_func['GeneralInfo']['DateBegin'])
                item_all_dic['DateEnd'].append(js_string_func['GeneralInfo']['DateEnd'])
                item_all_dic['PWCcode'].append(js_string_func['GeneralInfo']['PWCcode'])

                if 'GoodsComposition' in js_string_func['Information']['GoodsLists'][n]:
                    item_all_dic['Value'].append(js_string_func['Information']['GoodsLists'][n]['GoodsComposition'][0]['Value'])
                else:
                    item_all_dic['Value'].append('None')

                if ('PriceOptions' in js_string_func['Information']['GoodsLists'][n].values()) or \
                   ('PriceOptions' in js_string_func['Information']['GoodsLists'][0]):
                    if js_string_func['Information']['GoodsLists'][n]['PriceOptions'] != None:
                        if ('FirstValue' in js_string_func['Information']['GoodsLists'][n]['PriceOptions'][0]) or \
                           ('FirstValue' in js_string_func['Information']['GoodsLists'][n]['PriceOptions'][0].values()):
                            if js_string_func['Information']['GoodsLists'][n]['PriceOptions'][0]['FirstValue'] == None:
                                item_all_dic['FirstValue'].append('None')
                            else:
                                item_all_dic['FirstValue'].append(js_string_func['Information']['GoodsLists'][n]['PriceOptions'][0]['FirstValue'])
                        else:
                            item_all_dic['FirstValue'].append('None')
                    else:
                        item_all_dic['FirstValue'].append('None')
                else:
                    item_all_dic['FirstValue'].append('None')

                if js_string_func['Information']['GoodsLists'][n]['PriceOptions'] == None or \
                   js_string_func['Information']['GoodsLists'][n]['PriceOptions'][0]['Operator'] == None:
                    item_all_dic['LessOrEqual'].append('None')
                else:
                    item_all_dic['LessOrEqual'].append(js_string_func['Information']['GoodsLists'][n]['PriceOptions'][0]['Operator'])

                item_all_dic['File'].append(name_file)


def opnFolder(path):
    fileList = os.listdir(path)
    for file in fileList:
        temp_name_file = file
        print(temp_name_file)
        file = open(os.path.join(path + file), 'r')
        json_string = json.load(file)
        work_single_file(json_string, temp_name_file)


opnFolder('promo/')     # прописываем адрес папки где лежат json файлы, путь начинаем от места скрипта

df = pd.DataFrame(item_all_dic)

df.to_excel("result.xlsx", index=False)

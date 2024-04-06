import json

filename = 'response.json'
# 文件名
logfile = 'product_log.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        product_list = data.get('product_list')
        if product_list:
            with open(logfile, 'w', encoding='utf-8') as log_file:
                for product in product_list:
                    # 获取信息
                    goodsinfo = product.get('goodsinfo')
                    price = product.get('price')
                    # print('Goods Info:', goodsinfo)
                    # print('Price:', price)
                    print()
                    log_entry = f'Goods Info: {goodsinfo}\nPrice: {price}\n\n'
                    log_file.write(log_entry)

            print(f"已写入：{logfile}")
        else:
            print("啊错错错")
except FileNotFoundError:
    print(f"无法找到文件：{filename}")
except json.JSONDecodeError as e:
    print(f"JSON解码错误：{e}")
except Exception as e:
    print(f"发生了一个错误：{e}")

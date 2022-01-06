import bs4
import requests
import pandas as pd

if __name__ == '__main__':
    
    url = 'https://www.momoshop.com.tw/category/LgrpCategory.jsp?l_code=4301300000&mdiv=1099700000-bt_0_997_12-bt_0_997_12_P103_3_e1&ctype=B'
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    html = requests.get(url, headers=header)
    web = bs4.BeautifulSoup(html.text, 'lxml')

    product = {}
    result = web.select('.prdName')
    for index in range(len(result)):
        model = result[index].getText()
        if model != '':
            price = web.select('.prdPrice')[index].getText()
            price = price.removeprefix('$')
            price = price.replace(',', '')
            try:
                price_num = int(price)
            except:
                price_num = 0
            product[index] = {'model': model, 'price': price_num}
        
    product_df = pd.DataFrame(product).T
    product_df.to_excel(f"mouse-and-kb.xlsx")
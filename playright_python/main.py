from get_html_data import get_html
import pandas as pd
from loop import looping

if __name__ == '__main__':
    url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
     # Here we get the html_body ..[please refer get_html_data.py]
    parse_html = get_html(url)
    # in this tag we get the entire details of our laptop 
    laptops = parse_html.css('div.cPHDOP a')
    all_laptop_data = []
    for laptop in laptops:
        laptop_data = {}
        # Here we trying to get img url & also condition is applied to avoid null 
        if laptop.css_first('img.DByuf4'):
            laptop_data['image_url'] = laptop.css_first('img.DByuf4').attributes['src']
            # Here we get the titles of our laptops 
            laptop_data['title'] = laptop.css_first('div.KzDlHZ').text()
            # in this code we used condition to get ratings.. if its available then get it & if not put the 0 
            if laptop.css_first('div.XQDdHH'):
                laptop_data['ratings'] = laptop.css_first('div.XQDdHH').text()
            else:
                laptop_data['ratings'] = 0
            # From here we created another looping function because we use main tag which contains several child tag
            # therefore to get them out we use other function and get the other details
            laptop_data['details'] = looping(laptop.css('ul.G4BRas li'))
            laptop_data['discount_price'] = looping(laptop.css('div.hl05eU > div'))[0]
            laptop_data['original_price'] = looping(laptop.css('div.hl05eU > div'))[1]
            laptop_data['discount_per'] = looping(laptop.css('div.hl05eU > div'))[2]       
            all_laptop_data.append(laptop_data)
        
    pd_laptop = pd.DataFrame(all_laptop_data)      
    pd_laptop.to_csv('laptop_data.csv') 
    

    # print(all_laptop_data)
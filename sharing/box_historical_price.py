from datetime import date
import requests
import json

todaysdate = date.today().strftime('%Y-%m-%d')

# 浏览器-inspect-xhr-markets项-Headers-General-链接地址
res_page = requests.get('https://www.bigone.com/api/xn/v1/markets')

json_page = res_page.json()# 使用json()方法，将response对象，转为列表/字典

# 一层一层地取字典/列表，获取标的价格
btc_price = json_page['data'][0]['asset_pairs'][0]['ticker']['close']
eos_price = json_page['data'][0]['asset_pairs'][7]['ticker']['close']
xin_price = json_page['data'][0]['asset_pairs'][2]['ticker']['close']

box_price = (float(btc_price) + float( eos_price ) * 1500 + float(xin_price) * 8)/10000
box_price = str(round(box_price,2))#保留小数点后2位

# 把数据写入txt文件
f = open("/USERS/aosjiabei/desk/box_price_history.txt", "a")
f.write(todaysdate + '\t'  + 'btc:$' + btc_price + '\t' +'eos:$' + eos_price + '\t' + 'xin:$' + xin_price + '\t' + 'box:$' + box_price +  '\r')
f.close()

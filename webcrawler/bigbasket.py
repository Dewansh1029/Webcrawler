import json
import io
import requests
import pandas as pd
import csv


link1=requests.get('https://www.bigbasket.com/custompage/sysgenpd/?type=pc&slug=edible-oils-ghee&sid=L7XBq4-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OnMzgxfDM4MqliYXRjaF9pZHgAomFvwqJ1csKiYXDDomx0zQEuo2Rzas0ia6FvqnBvcHVsYXJpdHmlc3JfaWQBomRzzQa4o21yac0OLg==')
compare1=json.loads(link1.text)
compare1=compare1['tab_info']
compare2=compare1[0]['header_section']
data=compare2['items']
#print(data)

compare2=compare1[0]['product_info']
data=compare2['products']

lst_description = []
lst_category=[]
lst_brand=[]
lst_mrp=[]
lst_offer=[]
lst_rs=[]

for j in range(len(data)):
    offers=data[j]['j_offer_detail']
    text=offers['d_text']
    lst_offer.append(text)
    data1=data[j]['p_desc']
    lst_description.append(data1)
    data2=data[j]['llc_n']
    lst_category.append(data2)
    data3=data[j]['p_brand']
    lst_brand.append(data3)
    data4=data[j]['mrp']
    lst_mrp.append(data4)
    data5=data[j]['sp']
    lst_rs.append(data5)
    print("Product Description "+data1+" Category ="+data2+" Product Brand = "+data3+"  MRP = "+data4+" Offer = "+text+"  Rs "+data5)

    c={'Product Description':lst_description,
        'Category':lst_category,
        'Product Brand':lst_brand,
        'Mrp':lst_mrp,
        'Offer':lst_offer,
        'Rs':lst_rs
        }
    df = pd.DataFrame(c)
    export_csv=df.to_csv(r'D:\project\internship1\bigbasket.csv')
print(df)
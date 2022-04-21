import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import psycopg2

# 데이터를 수집하여 df에 저장
def makedf(color, code) :
  headers = {"User-Agent" : "Mozilla/5.0"}
  URL = f'https://store.musinsa.com/app/goods/{code}'
  page = requests.get(URL, headers = headers)
  soup = BeautifulSoup(page.content, 'html.parser')

  link = link = soup.select('#product_size_recommend > ul > li > p.size_content')

  height = height = [i.text for i in link]
  weight = [i.text for i in link]
  fit = [i.text for i in link]
  size = [int(i.find('strong').text[0:2]) for i in link]

  df = pd.DataFrame({'height' : height, 'weight' : weight, 'fit' : fit, 'size' : size})

  def conh(x) :
    a, b = x.split('/')
    a = int(a[-5:-2])
    return a
    
  def conw(x) :
    a, b = x.split('/')
    c, d = b.split('kg')
    return(int(c))
    
  def conf(x) :
    if '작음' in x :
      return '작음'
    elif '큼' in x :
      return '큼'
    else :
      return '적당함'

  df['height'] = df['height'].apply(conh)
  df['weight'] = df['weight'].apply(conw)
  df['fit'] = df['fit'].apply(conf)
  df['color'] = color

  df = df[['height', 'weight', 'color', 'fit', 'size']]

  return df

# 상위 10개 컬러의 df를 만들고 합침
df_bk = makedf('블랙', 1323968)
df_mg = makedf('미디엄그레이', 1216295)
df_db = makedf('더스티베이지', 1231416)
df_lb = makedf('라이트베이지', 1675527)
df_lg = makedf('라이트그레이', 1231424)
df_cg = makedf('차콜그레이', 1216294)
df_be = makedf('베이지', 1675524)
df_cr = makedf('크림', 1231420)
df_dg = makedf('다크그레이', 1231413)
df_nv = makedf('네이비', 1216293)

df_list = [df_bk, df_mg, df_db, df_lb, df_lg, df_cg, df_be, df_cr, df_dg, df_nv]
df_all = pd.concat(df_list, ignore_index = True).reset_index()
df_all = df_all.rename(columns = {'index' : 'id'})

# df_all.to_csv('pants.csv', encoding = 'UTF-8')
df_all.to_excel('pants.xlsx', encoding = 'UTF-8')

# PostgreSQL에 데이터를 저장

hostname = 'localhost'
database = 'jeongbinheo'
username = 'jeongbinheo'
pwd = 'wilshere10'
port_id = 5432

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id)

cur = conn.cursor()

list_pants = df_all.values.tolist()

# for i in list_pants :
#     cur.execute("INSERT INTO pants (Id, Height, Weight, Color, Fit, Size) VALUES (%s, %s, %s, %s, %s, %s);", i)

conn.commit()

cur.close()
conn.close()
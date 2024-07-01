import pandas as pd
import numpy as np
import streamlit as st
import pymysql
from sqlalchemy import create_engine
c=st.container()
with c:
  data=pd.read_csv("orders.csv",na_values=["Not Available","unknown"])
  data.drop_duplicates(inplace=True)
  data.dropna(subset=["Ship Mode"],axis=0,inplace=True)
  data.rename(columns={"Order ID":"order_id","City":"city"})
  data.columns=data.columns.str.lower()
  data.columns=data.columns.str.replace(" ","_")
  data["order_date"]=pd.to_datetime(data["order_date"],format="%Y-%m-%d")
  data.drop(columns=["Order Date","Product Id"],inplace=True)
  username="root"
  password="root"
  server="localhost"
  port="3306"
  dbname="sakila"
  connection_url=f'mysql+pymysql://{username}:{password}@{server}:{port}/{dbname}'
  engine=create_engine(connection_url)
  try:
      connection=engine.connect()
      print("Connection successful")
      connection.close()
  except Exception as e:
      print(f"Connection failed: {e}")
  data.to_sql('data_orders',con=engine,index=False,if_exists='append')
  st.bar_chart(data=data,x="Order Date",y="List Price")
  

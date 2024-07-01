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
  
  st.bar_chart(data=data,x="order_date",y="list_price")
  

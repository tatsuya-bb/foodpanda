# -*- coding: utf-8 -*-
from datetime import datetime as dt
from pytz import timezone
import socket
import ssl
import urllib.error
import urllib.request
import os
import datetime
import urllib.error
from zipfile import ZipFile
import requests
import pandas as pd

def now_timestamp():
    return dt.now().strftime("%Y-%m-%d %H:%M:%S")

def list_to_bool(l:list):
    bool_list=[]
    for item in l:
        bool_list.append(False if item == "0" or item == 0 else True)
    
    return bool_list

def create_proxy_dict(id,password,host,port,proxy_flg=True):
    if proxy_flg:
        proxy_url=f"http://{id}:{password}@{host}:{port}"
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    else:
        return {}

def get_global_ip():
    return socket.gethostbyname(socket.gethostname())

def down_load_img(url, path):
    ''' URLを指定し、画像を指定のフォルダに配置する '''
    # ファイル名の作成
    values = url.split('/')
    filename = values[-1]
    filename = filename.split('.')[0]
    # ファイルパスの指定
    if os.name == 'posix':
        path = '{}/{}.jpg'.format(path, filename)
    elif os.name == 'nt':
        path = '{}\\{}.jpg'.format(path, filename)

    # 画像URLからダウンロード
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def get_date_delta(delta):
    now = datetime.datetime.now()
    return now+datetime.timedelta(days=int(delta))

def padding_zero(text,num):
    return ("0"+text)[-num:]


def download_zipfile(url:str, save_path: str):
    try:
        with urllib.request.urlopen(url) as download_file:
            data = download_file.read()
            with open(save_path, mode='wb') as save_file:
                save_file.write(data)
        return True
    except urllib.error.URLError as e:
        print(e)
        return False

def extract_zipfile(zipfile_path: str, save_path: str):
    try:
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        with ZipFile(zipfile_path) as obj_zip:
            # 指定ディレクトリにすべてを保存する
            obj_zip.extractall(save_path)
            return True
    except Exception as e:
        print(f"[error] extract zipfile: {e}")
        return False

def to_cm(inchi: float):
    return inchi * 2.54

def to_kg(pound: float):
    return pound * 0.4535 


def fetch_currency_rate(base: str, to: str):
    res = requests.get("http://fx.mybluemix.net/")
    res.raise_for_status()
    res_dict = res.json()
    try:
        return res_dict["result"]["rate"][base + to]
    except:
        raise Exception(f"exchange currency error: {base}->{to}")

def write_text(text: str, path: str, mode: str="w", encoding="utf-8_sig"):
    with open(path, mode=mode, encoding=encoding) as f:
        f.write(text)


def class_list_to_df(items: list):
    df = pd.DataFrame()
    for item in items:
        df = df.append(item.__dict__, ignore_index=True)

    return df
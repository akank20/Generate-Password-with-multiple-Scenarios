# -*- coding: utf-8 -*-

import random  # https://docs.python.org/3.6/library/random.html
import sqlite3  # https://docs.python.org/3.6/library/sqlite3.html
import string  # https://docs.python.org/3.6/library/string.html
import json
import requests
from random import randint

def generate_password(length: int, complexity: int)-> str:
    
    if complexity==1:
        pswd=string.ascii_lowercase
    elif complexity==2:
        pswd=string.ascii_lowercase+string.digits
    elif complexity==3:
        pswd=string.ascii_lowercase+string.digits+string.ascii_uppercase
    elif complexity==4:
        pswd=string.ascii_lowercase+string.digits+string.ascii_uppercase+string.punctuation
   
    res=(''.join(random.choice(pswd) for i in range(length)))
    return res


def check_password_level(password: str) -> int:
    
    password_map = {}
    punctuation_list = set(string.punctuation)
    
    for character in password:
        if ord(character) >= 97 and ord(character) <= 122:
            add_to_map(1, character, password_map)
        if ord(character) >= 48 and ord(character) <= 57:
            add_to_map(2, character, password_map)
        if ord(character) >= 65 and ord(character) <= 90:
            add_to_map(3, character, password_map)
        if character in punctuation_list:
            add_to_map(4, character, password_map)
    password_map_length = len(password_map)
    password_length = len(password)
    if password_length < 8:
        return password_map_length
    else:
        if password_map_length is 4:
            return 4
        else:
            return password_map_length + 1

def add_to_map(level, value, password_map):
    if level not in password_map:
        password_map[level] = 1
    else:
        value = password_map[level]
        password_map[level] = value + 1


password1a=generate_password(9,1)
assert check_password_level(password1a)==2,"False"

password1b=generate_password(6,1)
assert check_password_level(password1b)==1,"False"

password2a=generate_password(10,2)
assert check_password_level(password2a)==3,"False"

password2b=generate_password(7,2)
assert check_password_level(password2b)==2,"False"

password3=generate_password(5,3)
assert check_password_level(password3)==3,"False"

password4=generate_password(8,4)
assert check_password_level(password4)==4,"False"


def create_user(db_path: str) -> None:  # you may want to use: http://docs.python-requests.org/en/master/
   
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    response=json.loads(requests.get("https://randomuser.me/api/").text)
    res=response['results']
    random_user=randint(0,len(res)-1)
    
    user=res[random_user]
    
    full_nm_json=user['name']
    fullnm=full_nm_json['title']+' '+full_nm_json['first']+' '+full_nm_json['last']
    get_email=user['email']
    
    cur.execute('INSERT INTO Requests (fullname,email) VALUES ( ?, ? )', (fullnm,get_email ) )
    
    conn.commit()
    conn.close()
    return

db_path="UserDB.sqlite3"

conn = sqlite3.connect(db_path)
cur = conn.cursor()
    
cur.execute('DROP TABLE IF EXISTS Requests')
cur.execute('CREATE TABLE Requests (fullname text, email text, password text)')



for i in range(0,10):
    create_user(db_path)
    length=randint(6,12)
    complexity=randint(1,4)
    pswd=generate_password(length,complexity)
    cur.execute('UPDATE Requests SET password=pswd WHERE name = ?')
    

conn.close()

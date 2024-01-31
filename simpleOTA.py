
import uuid
from fastapi import FastAPI, File, UploadFile, HTTPException
import sqlite3
from fastapi import Body, FastAPI,UploadFile, File, Request, Form
from fastapi.responses import FileResponse, StreamingResponse

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import sqlite3

from pydantic import BaseModel
global versi
app = FastAPI()
conn=sqlite3.connect("Uuiduser.db",check_same_thread=False)
cursor=conn.cursor()
conn.commit()

class Item(BaseModel):
    name:list
# Commit the changes and close the connection








@app.post("/edit")
async def root2(item: Item):
    list_names = []
    for nm in item.name:
        list_names.append(nm)
    print(list_names[0])
    conn=sqlite3.connect("Uuiduser.db",check_same_thread=False)
    cursor=conn.cursor()
    data=list_names[0]
    cursor.execute("SELECT id, uuid, versi from data WHERE uuid=?", (list_names[0],))
    c=False
    for row in cursor:
        c=True
        print("HAIII")
        print(row[1])
        print(row[2])
        cursor.execute("UPDATE data SET versi=? WHERE uuid=?", (list_names[1], row[1]))
        conn.commit()
    if(c==False):
        print("HAIIIr")
        conn=sqlite3.connect("Uuiduser.db",check_same_thread=False)
        cursor=conn.cursor()
        cursor.execute("INSERT INTO data VALUES (?,?,?)",(None,list_names[0],list_names[1]))
        conn.commit()
    return {"DATA":"OKE"}

    # if(row[4]=="id5"):
    #     val id5=row[8]//isi high low
    #  if(row[4]=="id2"):
    #     val id2=row[8]//isi high low   
    # return {"id1":id1,"id5":id5}
@app.post("/getversi")
async def root(item: Item):
    conn=sqlite3.connect("Uuiduser.db",check_same_thread=False)
    cursor=conn.cursor()
    list_names = []
    ver=[]
    ver.clear
    for nm in item.name:
        list_names.append(nm)
    print(list_names)
    for x in list_names:
        print(x)
        cursor.execute("SELECT id, uuid, versi from data WHERE uuid=?", (x,))
        for row in cursor:
            print("HAIII")
            print(row[1])
            print(row[2])
            ver.append(row[2])
    return {"aku":ver}

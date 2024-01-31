
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
conn=sqlite3.connect("databaseOTA.db",check_same_thread=False)
cursor=conn.cursor()
class Item(BaseModel):
    name:list
# Commit the changes and close the connection

# Run the table creation at startup
templates=Jinja2Templates(directory="htmldirectory")

@app.get("/home/", response_class=HTMLResponse)  #Alamat link untuk memasukki menu home
def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request}) #menampilkan halaman HTML

@app.post("/submitform")

async def index2(versi:int=Form(...),file:UploadFile=File(...)): 
    conn=sqlite3.connect("databaseOTA.db",check_same_thread=False)
    cursor=conn.cursor()
    file_content = await file.read()
    file_name = file.filename
    global versi2
    versi2=versi
    cursor.execute("INSERT INTO ota VALUES (?,?,?,?)",(None,versi,file_name,file_content))
    conn.commit()
    return {"aku":"oke"}


# @app.get("/cat/{versi}") #Alamat link untuk mendownload file
# def catd(versi):
#     global data
#     global datas
#     conn=sqlite3.connect("databaseOTA.db",check_same_thread=False)
#     cursor=conn.cursor()
#     row=cursor.execute("SELECT id,versi, name,data from ota WHERE versi = ?", (str(versi)))
#     image_data = row[2] # type: ignore
#     # for row in cursor:
#     #     c=True
#     #     print("HAIII")
#     #     print(row[0])
#     #     print(row[1])
#     #     print(row[2])
#     #     data=row[1]
#     temp_file_path = f"temp_{uuid.uuid4()}.jpg"  # Ganti ekstensi sesuai format gambar
#     with open(temp_file_path, "wb") as file:
#         file.write(image_data)

#     return FileResponse(temp_file_path, media_type='text')
    # return {"data":"oke"}
        # return FileResponse(path=datas, media_type="text",filename=data)
        # return StreamingResponse(io.BytesIO(datas), media_type="application/octet-stream")

    
@app.get("/p/{versiw}/y/{idr}")  #Alamat link untuk request version
def index(versiw,idr):
    url="https://fastapiskripsi-be199a487d88.herokuapp.com/c/"+versiw+idr

    return {"version":versiw,"url":url}

@app.get("/c/{versi}")  # Alamat link untuk mendownload file
def catd(versi: str):
    conn = sqlite3.connect("databaseOTA.db", check_same_thread=False)
    cursor = conn.cursor()
    
    cursor.execute("SELECT data FROM ota WHERE versi = ?", (versi,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Version not found")

    image_data = row[0]

    temp_file_path = f"temp_{uuid.uuid4()}.jpg"  # Change extension based on actual image type
    with open(temp_file_path, "wb") as file:
        file.write(image_data)

    response = FileResponse(temp_file_path, media_type='text')

    # Cleanup temporary file after response
    # @response.background
    # def cleanup():
    #     os.remove(temp_file_path)
    return response
@app.post("/tampilversi")
def tampil_keluaran(payload: dict=Body(...)):
    lis=[]
    conn=sqlite3.connect("databaseOTA.db",check_same_thread=False)
    cursor=conn.cursor()
    getkontak=payload['name']
    if(getkontak=="cekdata"):
        data=conn.execute('SELECT versi FROM ota')
        for i in data:
            print(i)
            lis.append(i[0])
        print(lis)
    return {"data":lis}


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
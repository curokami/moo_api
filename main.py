from fastapi import Fastapi 

app =Fastapi()

@app.get("/")
def read_root():
 return {"message":"Welcom to FastAPI"}

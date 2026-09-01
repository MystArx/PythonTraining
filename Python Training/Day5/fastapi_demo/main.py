from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{
            "message": "Home Directory"
        }
    
@app.get("/get")
def home_get():
    return{
            "message": "Home Directory : get"
        }


@app.post("/post")
def home_post():
    return{
            "message": "Home Directory : post"
        }
    
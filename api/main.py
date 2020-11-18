from fastapi import fastAPI 
from v1.routers import router
# from mangum import Mangum

app = fastAPI(title = "FAST API Template",description="API to get/put/post/update")

app.include_router(router,prefix="/v1")

@app.get("/")
def read_root():
    return {"hello":"world"}

# to make it work with Amazon Lambda, we create a handler object
# handler = Mangum(app=app)    

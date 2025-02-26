from fastapi import FastAPI, Request
import datetime

app = FastAPI()

# http://192.168.1.130:8000/kayit
@app.get("/kayit")
async def read_root(request: Request):
    client_host = request.client.host
    with open("ip_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {client_host}\n")
    return {"ip": "Kayıt tamam"}

# http://192.168.1.130:8000/
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# http://localhost:8000/
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
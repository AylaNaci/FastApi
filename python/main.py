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

# Yeni rota: http://192.168.1.130:8000/random
@app.post("/random")
async def receive_random_number(request: Request):
    data = await request.json()
    random_number = data.get("number")
    with open("random_numbers.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {random_number}\n")
    return {"status": "success", "number": random_number}

# http://192.168.1.130:8000/
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# http://localhost:8000/
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
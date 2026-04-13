from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import ipaddress

app = FastAPI(title="Infra API - Quentin Juskowiak")

FILE = "servers.json"



def load_servers():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []



def save_servers(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


servers = load_servers()


class Server(BaseModel):
    name: str
    ip: str


@app.get("/")
def home():
    return {"message": "API Infra - Gestion de serveurs"}


@app.get("/servers")
def get_servers():
    return {"servers": servers}


@app.post("/servers")
def add_server(server: Server):
    try:
        ipaddress.ip_address(server.ip)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid IP address")

    new_server = {
        "id": len(servers) + 1,
        "name": server.name,
        "ip": server.ip
    }

    servers.append(new_server)
    save_servers(servers)

    return {"message": "Server added", "server": new_server}


@app.delete("/servers/{server_id}")
def delete_server(server_id: int):
    for i, s in enumerate(servers):
        if s["id"] == server_id:
            deleted = servers.pop(i)
            save_servers(servers)
            return {"message": "Deleted", "server": deleted}

    raise HTTPException(status_code=404, detail="Server not found")
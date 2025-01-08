from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}

@app.post("/receive-script/")
async def receive_script(request: Request):
    data = await request.json()
    script = data.get("script", "No script provided.")
    session_id = data.get("session_id", "Unknown session ID.")
    
    # Save the script with session_id as the filename
    with open(f"{session_id}_script.txt", "w") as file:
        file.write(script)
    
    return {"status": "success", "message": "Script received successfully"}

@app.get("/receive-script/")
def get_script(session_id: str):
    # Fetch the script file based on session_id
    script_file = f"{session_id}_script.txt"
    if os.path.exists(script_file):
        with open(script_file, "r") as file:
            script = file.read()
        return {"session_id": session_id, "script": script}
    return JSONResponse(status_code=404, content={"error": "Script not found"})

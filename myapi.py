from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# POST endpoint to save a script
@app.post("/receive-script/")
async def receive_script(request: Request):
    data = await request.json()
    script = data.get("script", "No script provided.")
    session_id = data.get("session_id", "Unknown session ID.")
    
    # Save the script to a file named after the session ID
    with open(f"{session_id}_script.txt", "w") as file:
        file.write(script)
    
    print(f"Saved script for session ID {session_id}: {script}")  # Debugging in logs
    return {"status": "success", "message": "Script received successfully"}

# GET endpoint to fetch a saved script
@app.get("/receive-script/")
def get_script(session_id: str):
    script_file = f"{session_id}_script.txt"
    if os.path.exists(script_file):
        with open(script_file, "r") as file:
            script = file.read()
        return {"session_id": session_id, "script": script}
    return JSONResponse(status_code=404, content={"error": "Script not found"})

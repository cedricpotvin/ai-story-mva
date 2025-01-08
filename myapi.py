from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Root route to confirm the server is running
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}

# POST endpoint to receive and save the script
@app.post("/receive-script/")
async def receive_script(request: Request):
    data = await request.json()  # Parse the incoming JSON payload
    script = data.get("script", "No script provided.")  # Extract script
    session_id = data.get("session_id", "Unknown session ID.")  # Extract session_id

    # Save the script to a file named after the session ID
    with open(f"{session_id}_script.txt", "w") as file:
        file.write(script)

    # Print the script for debugging (visible in Render logs)
    print(f"Session ID: {session_id}, Script: {script}")
    
    return {"status": "success", "message": "Script received successfully"}

# GET endpoint to retrieve the saved script
@app.get("/receive-script/")
def get_script(session_id: str):
    # Check if the file exists
    script_file = f"{session_id}_script.txt"
    if os.path.exists(script_file):
        with open(script_file, "r") as file:
            script = file.read()
        return {"session_id": session_id, "script": script}

    # If the file doesn't exist, return a 404 error
    return JSONResponse(status_code=404, content={"error": "Script not found"})

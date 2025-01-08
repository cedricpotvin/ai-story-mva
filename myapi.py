from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/receive-script/")
async def receive_script(request: Request):
    data = await request.json()
    script = data.get("script", "No script provided.")
    session_id = data.get("session_id", "Unknown session ID.")
    
    # Save the script with session_id as the filename
    with open(f"{session_id}_script.txt", "w") as file:
        file.write(script)
    
    return {"status": "success", "message": "Script received successfully"}

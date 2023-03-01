import uvicorn

if __name__ == "__main__":
    uvicorn.run("InsMachine:app", host="192.168.16.140", port=8005, log_level="info", reload=True)
    print("Server Classed")

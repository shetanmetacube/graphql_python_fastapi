# Run the FastAPI app
import uvicorn
from server import app
if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8001, reload=False)
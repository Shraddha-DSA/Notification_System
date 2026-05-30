from fastapi import FastAPI
from app.routes import auth, notifications
from app.websocket.websocket import router as websocket_router
app = FastAPI(title="Real-time Notification System")
app.include_router(auth.router)
app.include_router(notifications.router)
app.include_router(websocket_router)
@app.get("/")
def root():
    return {"message":"Notification System Running"}

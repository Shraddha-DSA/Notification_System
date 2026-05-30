from app.database import engine
from app.models.user import User
from app.models.notifications import Notification
from app.database import Base
Base.metadata.create_all(bind=engine)
print("Tables create successfully")
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.notifications import Notification
from app.schemas.notification_schema import NotificationCreate
router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)
@router.post("/{user_id}")
def create_nitification(
    user_id: int,
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):
    new_notification = Notification(
        message=notification.message,
        user_id=user_id
    )
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return {
        "message":"Notification created"
    }
@router.get("/{user_id}")
def get_notifications(
    user_id: int,
    db: Session = Depends(get_db)
):
    notifications = db.query(Notification).filter(
        Notification.user_id == user_id
    ).all()
    return notifications
from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr
from schemas.models import Message

from backend.misc.email.funcs import generate_test_email, send_email
from backend.misc.usermanager import current_user

router = APIRouter(prefix="/utils", tags=["utils"])


@router.post(
    "/test-email/",
    dependencies=[Depends(current_user(active=True, superuser=True))],
    status_code=201,
)
def test_email(email_to: EmailStr) -> Message:
    """
    Test emails.
    """
    email_data = generate_test_email(email_to=email_to)
    send_email(
        email_to=email_to,
        subject=email_data.subject,
        html_content=email_data.html_content,
    )
    return Message(message="Test email sent")


@router.get("/health-check/")
async def health_check() -> bool:
    return True

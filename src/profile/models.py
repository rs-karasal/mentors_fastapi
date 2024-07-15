from auth.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class MentorProfile(Base):
    "mentor_profile"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=False)
    description = Column(String, nullable=False)
    photo = Column(String, nullable=False)

# TODO: learn Jinja2 for templates
# TODO: learn Bootstrap for styling

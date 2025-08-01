from app.base.base_pydantic import Base
from app.projects.schemas.projects.base import BaseProject


class Project(Base):
    id: int
    name: str
    owner_id: int


class CreateProjectDTO(BaseProject): ...


class CreateProjectRequest(Base):
    name: str

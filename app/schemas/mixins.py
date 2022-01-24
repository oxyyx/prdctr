import datetime

from pydantic import BaseModel, Field, validator


class AuditedModelMixin(BaseModel):
    created_at: datetime.datetime = Field(None, title="Created At")
    created_by: str = Field(None, title="Created By")
    updated_at: datetime.datetime = Field(None, title="Updated At")
    updated_by: str = Field(None, title="Created By")

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(
            cls,
            value: datetime.datetime,
    ) -> datetime.datetime:
        return value or datetime.datetime.now()


class IDModelMixin(BaseModel):
    id_: int = Field(0, title="ID", alias="id")
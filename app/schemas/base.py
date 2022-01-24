import datetime

from pydantic import BaseConfig, BaseModel


def datetime_to_realworld(dt: datetime.datetime) -> str:
    return dt.replace(tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def to_camel_case(string: str) -> str:
    return "".join(
        word if index == 0 else word.capitalize()
        for index, word in enumerate(string.split("_"))
    )


class Base(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {datetime.datetime: datetime_to_realworld}
        alias_generator = to_camel_case

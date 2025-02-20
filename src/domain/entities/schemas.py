from pydantic import BaseModel, ConfigDict, field_validator

from domain.entities.exceptions import (
    NegativeNumberError,
    ZeroOrNegativeNumberError,
)


class CharacterSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int

    @field_validator("height", "mass")
    @classmethod
    def validate_height_mass(cls, value):
        if value <= 0:
            raise ZeroOrNegativeNumberError()
        return value

    @field_validator("birth_year")
    @classmethod
    def validate_birth_year(cls, value):
        if value < 0:
            raise NegativeNumberError()
        return value


class CharacterPartialSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    name: str
    height: float
    mass: float
    eye_color: str
    birth_year: int

from __future__ import annotations

from typing import Optional, Annotated
from uuid import UUID, uuid4
from datetime import datetime, timezone
from pydantic import BaseModel, Field, StringConstraints

from .person import UNIType

# Columbia University Course Number Format: 4 letter for the department followed by 4 digits for the course number and a letter
# Ex: COMS4153W
CourseNumberType = Annotated[str, StringConstraints(pattern=r"^[A-Z]{4}\d{4}[A-Z]$")]

class CourseBase(BaseModel):
    course_number: CourseNumberType = Field(
        ...,
        description="Columiba University Course Number (Department abbreviation followed by 4 digits and a character).",
        json_schema_extra={"example": "COMS4153W"},
    )
    name: str = Field(
        ...,
        description="Course name.",
        json_schema_extra={"example": "Cloud Computing"},
    )
    professor_uni: UNIType = Field(
        ...,
        description="UNI of the professor teaching this course.",
        json_schema_extra={"example": "dj2390"},
    )
    credits: int = Field(
        ...,
        description="Number of credits earned by taking this course.",
        json_schema_extra={"example": 3},
    )
    strength: int = Field(
        ...,
        description="Maximum number of students that can enroll in this course.",
        json_schema_extra={"example": 120},
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "course_number": "COMS4153W",
                    "name": "Cloud Computing",
                    "professor_uni": "dff9",
                    "credits": 3,
                    "strength": 120,
                }
            ]
        }
    }


class CourseCreate(CourseBase):
    """Creation payload for a Course."""

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "course_number": "COMS4705W",
                    "name": "Natural Language Processing",
                    "professor_uni": "ab2312",
                    "credits": 3,
                    "strength": 90,
                }
            ]
        }
    }


class CourseUpdate(BaseModel):
    """Partial update for a Course; supply only fields to change."""

    course_number: Optional[UNIType] = Field(
        None,
        description="Columiba University Course Number (Department abbreviation followed by 4 digits and a character).",
        json_schema_extra={"example": "COMS4995W"},
    )
    name: Optional[str] = Field(
        None, description="Course name.", json_schema_extra={"example": "Deep Learning"}
    )
    credits: Optional[int] = Field(
        None,
        description="Number of credits earned by taking this course.",
        json_schema_extra={"example": 3},
    )
    professor_uni: Optional[UNIType] = Field(
        ...,
        description="UNI of the professor teaching this course.",
        json_schema_extra={"example": "dj2390"},
    )
    strength: Optional[int] = Field(
        None,
        description="Maximum number of students that can enroll in this course.",
        json_schema_extra={"example": 100},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Cloud Computing"},
                {"strength": 60},
            ]
        }
    }


class CourseRead(CourseBase):
    """Server representation of course returned to clients."""

    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Course ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "99999999-9999-4999-8999-999999999999",
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                    "course_number": "COMS4153W",
                    "name": "Cloud Computing",
                    "professor_uni": "dff9",
                    "credits": 3,
                    "strength": 120,
                }
            ]
        }
    }

from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from datetime import datetime, timezone

from .person import UNIType
from .course import CourseBase


class DepartmentBase(BaseModel):
    department_code: str = Field(
        ..., description="Department code.", json_schema_extra={"example": "COMS"}
    )
    name: str = Field(
        ...,
        description="Department name.",
        json_schema_extra={"example": "Computer Science"},
    )
    head_of_department: UNIType = Field(
        ...,
        description="UNI of the head of the department.",
        json_schema_extra={"example": "sf2303"},
    )
    courses_list: List[CourseBase] = Field(
        ...,
        description="All the courses offered by the department.",
        json_schema_extra={
            "example": [
                {
                    "course_number": "COMS4153W",
                    "name": "Cloud Computing",
                    "professor_uni": "dff9",
                    "credits": 3,
                    "strength": 120,
                }
            ]
        },
    )
    email: EmailStr = Field(
        ...,
        description="Email of the department",
        json_schema_extra={"example": "cs@columbia.edu"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "department_code": "IEOR",
                    "name": "Industrial Engineering and Operations Research",
                    "head_of_department": "sm1231",
                    "courses_list": [
                        {
                            "course_number": "IEOR4121W",
                            "name": "Marketing Analytics",
                            "professor_uni": "dd39",
                            "credits": 3,
                            "strength": 50,
                        },
                        {
                            "course_number": "IEOR4123W",
                            "name": "Data Analysis",
                            "professor_uni": "ce19",
                            "credits": 3,
                            "strength": 120,
                        },
                    ],
                    "email": "info@ieor.columbia.edu",
                }
            ]
        }
    }


class DepartmentRead(DepartmentBase):
    """Server representation returned to clients."""

    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Department ID.",
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
                    "department_code": "IEOR",
                    "name": "Industrial Engineering and Operations Research",
                    "head_of_department": "sm1231",
                    "courses_list": [
                        {
                            "course_number": "IEOR4121W",
                            "name": "Marketing Analytics",
                            "professor_uni": "dd39",
                            "credits": 3,
                            "strength": 50,
                        },
                        {
                            "course_number": "IEOR4123W",
                            "name": "Data Analysis",
                            "professor_uni": "ce19",
                            "credits": 3,
                            "strength": 120,
                        },
                    ],
                    "email": "info@ieor.columbia.edu",
                }
            ]
        }
    }


class DepartmentCreate(DepartmentBase):
    """Payload for department creation"""

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "department_code": "IEOR",
                    "name": "Industrial Engineering and Operations Research",
                    "head_of_department": "sm1231",
                    "courses_list": [
                        {
                            "course_number": "IEOR4121W",
                            "name": "Marketing Analytics",
                            "professor_uni": "dd39",
                            "credits": 3,
                            "strength": 50,
                        },
                        {
                            "course_number": "IEOR4123W",
                            "name": "Data Analysis",
                            "professor_uni": "ce19",
                            "credits": 3,
                            "strength": 120,
                        },
                    ],
                    "email": "info@ieor.columbia.edu",
                }
            ]
        }
    }


class DepartmentUpdate(BaseModel):
    department_code: Optional[str] = Field(
        ..., description="Department code.", json_schema_extra={"example": "COMS"}
    )
    name: Optional[str] = Field(
        ...,
        description="Department name.",
        json_schema_extra={"example": "Computer Science"},
    )
    head_of_department: Optional[UNIType] = Field(
        ...,
        description="UNI of the head of the department.",
        json_schema_extra={"example": "sf2303"},
    )
    courses_list: Optional[List[CourseBase]] = Field(
        ...,
        description="All the courses offered by the department.",
        json_schema_extra={
            "example": [
                {
                    "course_number": "COMS4153W",
                    "name": "Cloud Computing",
                    "professor_uni": "dff9",
                    "credits": 3,
                    "strength": 120,
                }
            ]
        },
    )
    email: Optional[EmailStr] = Field(
        ...,
        description="Email of the department",
        json_schema_extra={"example": "cs@columbia.edu"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Industry and Engineering"},
                {"head_of_department": "aj9843"},
            ]
        }
    }

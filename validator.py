from pydantic import BaseModel, ConfigDict, field_validator
from typing import List, Dict, Any


class Note(BaseModel):
    note_id: str
    note_name: str
    data: List[Dict[str, Any]]
    remark: str

    model_config = ConfigDict(extra="allow")


class NotebookRequest(BaseModel):
    user_id: str
    notebook: List[Note]
    user_query: str

    model_config = ConfigDict(extra="allow")

    @field_validator("notebook")
    @classmethod
    def notebook_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError("Notebook must contain at least one note")
        return v


class PDFRequest(BaseModel):
    html: str
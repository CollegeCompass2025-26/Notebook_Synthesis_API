from pydantic import BaseModel
from typing import List, Dict, Any


class Note(BaseModel):
    note_id: str
    note_name: str
    data: List[Dict[str, Any]]
    remark: str


class NotebookRequest(BaseModel):
    user_id: str
    notebook: List[Note]
    user_query: str
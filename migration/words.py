# from __future__ import annotations
# from typing import Optional
from pydantic import BaseModel
class Words(BaseModel):
    input_word=str
    converted_word=str
    lang_type=str

"""
Virtual Objects definitions
"""

from dataclasses import dataclass
from typing import List
from pydantic import BaseModel

@dataclass
class TIProj(BaseModel):
    """
    Class to data define on TI Project
    """

    issue: List[str] = None
    priority: List[str] = None

    def to_json(self):
        """
        Function to return data in json format
        """

        return {
            'issue': self.issue,
            'priority': self.priority
        }

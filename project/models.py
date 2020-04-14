"""
Virtual Objects definitions
"""

from dataclasses import dataclass

@dataclass
class TIProj:
    """
    Class to data define on TI Project
    """
    issue: str
    priority: str

    def to_json(self):
        """
        Function to return data in json format
        """
        return {
            'issue': self.issue,
            'priority': self.priority
        }

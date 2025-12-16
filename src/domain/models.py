# ? why
from __future__ import annotations

# ? why
from dataclasses import dataclass
from datetime import date
from uuid import UUID, uuid4 # ? why
from typing import Optional, Dict, Any # why?


# ? why using data class, frozen and slots?
# ? frozen: makes the class immutable
# ? slots: makes the class faster
@dataclass(frozen=True, slots=True)
class LogEntry:
    """
    Domain entity which represents an event done by the user in a given day.
    """
    id: UUID
    topic: str
    minutes: int
    date: date
    note: Optional[str] = None

    #? why at the end is -> "LogEntry"
    # ? why using static method?
    @staticmethod
    def create(*, date: date, topic: str, minutes: int, note: Optional[str] = None) -> "LogEntry":
        return LogEntry(id=uuid4(), date=date, topic=topic, minutes=minutes, note=note)
        # ? why using uuid4?
        # ? because it's a good way to generate a unique id, note that it's not incrementing and it's not sequential

    # what is __post_init__?
    # it is a method that is called after the object is initialized
    def __post_init__(self):
        validate_date(self.date)
        object.__setattr__(self, "topic", normalize_topic(self.topic))
        object.__setattr__(self, "minutes", valizate_minutes(self.minutes))
        object.__setattr__(self, "note", normalize_note(self.note))
        #TODO: validate_topic(self.topic)
        #TODO: validate_minutes(self.minutes)
        #TODO: validate_note(self.note)
        #TODO: validate_date(self.date)

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of a  log entry
        I will be usefull when doing serialization 
        Note: useful when working with json export
        """
        # TODO: Implement this method
        pass

    @staticmethod
    def from_doct(self) -> Dict[str, Any]:
        """
        Returns a log entry object from a dictionary representation
        I will be usefull when doing deserialization
        Note: useful when working with json import
        """
        # TODO: Implement this method
        pass

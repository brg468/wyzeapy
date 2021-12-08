from typing import Dict, Any, List


class Event:
    event_id: str
    device_mac: str
    device_model: str
    event_category: int
    event_value: str
    event_ts: int
    event_ack_result: int
    is_feedback_correct: int
    is_feedback_face: int
    is_feedback_person: int
    file_list: List[Dict[Any, Any]]
    event_params: Dict[Any, Any]
    recognized_instance_list: List[Any]
    tag_list: List[Any]
    read_state: int

    def __init__(self, dictionary: Dict[Any, Any]):
        for k, v in dictionary.items():
            setattr(self, k, v)

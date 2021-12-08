from typing import Dict, Any


class Group:
    group_id: str
    group_name: str

    def __init__(self, dictionary: Dict[Any, Any]):
        for k, v in dictionary.items():
            setattr(self, k, v)

    def __repr__(self) -> str:
        return "<Group: {}, {}>".format(self.group_id, self.group_name)

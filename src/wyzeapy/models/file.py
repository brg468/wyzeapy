from typing import Union, List, Any, Dict


class File:
    file_id: str
    type: Union[int, str]
    url: str
    status: int
    en_algorithm: int
    en_password: str
    is_ai: int
    ai_tag_list: List[Any]
    ai_url: str
    file_params: Dict[Any, Any]

    def __init__(self, dictionary: Dict[Any, Any]):
        for k, v in dictionary.items():
            setattr(self, k, v)

        if self.type == 1:
            self.type = "Image"
        else:
            self.type = "Video"

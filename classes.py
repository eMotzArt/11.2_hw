import json
from typing import Optional


class RepositoryCandidates:
    """Класс считывает и берет с базы данные (все, по id, по skill'у)"""

    def __init__(self, file_name: str):
        self.candidates_file = file_name

    def load_candidates(self) -> list[dict]:
        with open(self.candidates_file, encoding='utf-8') as file:
            return json.load(file)

    def get_all(self) -> list[dict]:
        return self.load_candidates()

    def get_by_id(self, id: int) -> Optional[dict]:
        candidates = self.load_candidates()
        for candidate in candidates:
            if candidate['id'] == id:
                return candidate

    def get_by_skill(self, skill) -> Optional[list[dict]]:
        candidates = self.load_candidates()
        skillful_candidates = []
        for candidate in candidates:
            if skill in map(lambda skill: skill.lower(), candidate['skills'].split(', ')):
                skillful_candidates.append(candidate)

        if skillful_candidates:
            return skillful_candidates
        return None


class AppTemplateRenderer:
    def render_index(candidates_list: list[dict]) -> str:
        to_return_list = []
        for candidate in candidates_list:
            to_return_list.append(f"{candidate['name']}\n" \
                                  f"{candidate['id']}\n" \
                                  f"{candidate['skills']}\n\n")
        to_return_str = Preformater.pre(''.join(to_return_list))
        return to_return_str

    def render_by_id(candidate: dict) -> str:
        to_return_list = []

        to_return_list.append(f'<img src={candidate["picture"]}>\n\n')
        to_return_list.append(f"{candidate['name']}\n" \
                              f"{candidate['id']}\n" \
                              f"{candidate['skills']}")
        to_return_str = Preformater.pre(''.join(to_return_list))

        return to_return_str

    def render_by_skill(candidates_list: list[dict]) -> str:
        to_return_list = []
        for candidate in candidates_list:
            to_return_list.append(f"{candidate['name']}\n" \
                                  f"{candidate['id']}\n" \
                                  f"{candidate['skills']}\n\n")
        to_return_str = Preformater.pre(''.join(to_return_list))
        return to_return_str


class Preformater:
    @classmethod
    def pre(cls, data: str) -> str:
        return f'<pre>{data}</pre>'

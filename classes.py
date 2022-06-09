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

    def get_by_name(self, name: str) -> Optional[list[dict]]:
        candidates = self.load_candidates()
        founded_candidates = []
        for candidate in candidates:
            if name.lower() in map(lambda low_name: low_name.lower(), candidate['name'].split()):
                founded_candidates.append(candidate)

        if founded_candidates:
            return founded_candidates
        return None
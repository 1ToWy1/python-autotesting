import json
from typing import List, Dict, Any


class TaskManager:
    """Класс для управления списком задач."""

    def __init__(self) -> None:
        """Инициализация пустого списка задач."""
        self.tasks: List[Dict[str, Any]] = []

    def add_task(self, description: str) -> None:
        """Добавление новой задачи."""
        task = {
            "description": description,
            "completed": False
        }
        self.tasks.append(task)

    def complete_task(self, index: int) -> bool:
        """Отметка задачи как выполненной с проверкой индекса."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            return True
        return False

    def remove_task(self, index: int) -> bool:
        """Удаление задачи из списка по индексу."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def save_to_json(self, filename: str) -> None:
        """Сохранение текущего списка задач в JSON-файл."""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def load_from_json(self, filename: str) -> None:
        """Загрузка списка задач из JSON-файла."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
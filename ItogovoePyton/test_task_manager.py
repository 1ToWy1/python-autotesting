from task_manager import TaskManager


class TestTaskManager:

    def test_add_and_complete_task(self) -> None:
        """Первый тест: Добавление и выполнение задачи, проверка статуса на True."""
        print("\n--- Добавление и выполнение задачи ---")
        manager = TaskManager()
        manager.add_task("Купить продукты")

        assert len(manager.tasks) == 1, f"Ожидалась 1 задача, но найдено: {len(manager.tasks)}"
        assert manager.tasks[0][
                   "description"] == "Купить продукты", f"Неверное описание: {manager.tasks[0]['description']}"
        assert manager.tasks[0]["completed"] is False, "Новая задача не должна быть выполненной"

        success = manager.complete_task(0)

        assert success is True, "Метод complete_task должен вернуть True"
        assert manager.tasks[0]["completed"] is True, "Статус задачи должен измениться на True"
        print("Тест успешно пройден.")

    def test_remove_task(self) -> None:
        """Второй тест: Удаление задачи и проверка её исчезновения из списка."""
        print("\n--- Удаление задачи ---")
        manager = TaskManager()
        manager.add_task("Первая задача")
        manager.add_task("Вторая задача")

        assert len(manager.tasks) == 2, f"Ожидалось 2 задачи, найдено: {len(manager.tasks)}"

        success = manager.remove_task(0)

        assert success is True, "Метод remove_task должен вернуть True"
        assert len(manager.tasks) == 1, f"После удаления должно остаться 1 задач(а), но осталось: {len(manager.tasks)}"
        assert manager.tasks[0][
                   "description"] == "Вторая задача", f"Осталась неверная задача: {manager.tasks[0]['description']}"
        print("Тест успешно пройден.")

    def test_save_and_load_json(self, tmp_path) -> None:
        """Третий тест: Сохранение задач в JSON и загрузка, проверка корректности."""
        print("\n--- Сохранение и загрузка JSON ---")
        manager = TaskManager()
        manager.add_task("Изучить ООП")
        manager.complete_task(0)

        file_path = tmp_path / "tasks_test.json"
        manager.save_to_json(str(file_path))

        new_manager = TaskManager()
        new_manager.load_from_json(str(file_path))

        assert len(new_manager.tasks) == 1, f"После загрузки ожидалась 1 задача, получено: {len(new_manager.tasks)}"
        assert new_manager.tasks[0][
                   "description"] == "Изучить ООП", f"Загружено неверное описание: {new_manager.tasks[0]['description']}"
        assert new_manager.tasks[0]["completed"] is True, "Статус выполненной задачи не сохранился"
        print("Тест успешно пройден.")
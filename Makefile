.PHONY: exercise_1
exercise_1:
	pytest -k test_get_all_subjects

.PHONY: exercise_2
exercise_2:
	pytest -k test_get_professor_names

.PHONY: exercise_1
exercise_1:
	pytest -k test_get_all_subjects

.PHONY: exercise_2
exercise_2:
	pytest -k test_get_professor_names

.PHONY: exercise_3
exercise_3:
	pytest -k test_remove_pii

.PHONY: exercise_4
exercise_4:
	pytest -k test_add_new_professors

.PHONY: exercise_5
exercise_5:
	pytest -k test_update_professor_ages

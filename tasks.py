from invoke import run, task


def get_test(exercise):
    if (exercise == 0):
        return "test_get_all_subjects"
    elif(exercise == 1):
        return "test_get_professor_names"
    elif(exercise == 2):
        return "test_remove_pii"
    elif(exercise == 3):
        return "test_add_new_professors"
    elif(exercise == 4):
        return "test_update_professor_ages"
    elif(exercise == 5):
        return "test_get_professor"
    elif(exercise == 6):
        return "test_get_professors"


@task
def test(ctx, exercise=1):
    test_name = get_test(exercise)
    ctx.run("pytest -v -k {}".format(test_name), pty=True)

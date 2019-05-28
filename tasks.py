from invoke import run, task


def get_test(exercise):
    if (exercise == "0"):
        return "test_get_all_subjects"
    elif(exercise == "1"):
        return "test_get_professor_names"
    elif(exercise == "2"):
        return "test_remove_pii"
    elif(exercise == "3"):
        return "test_add_new_professors"
    elif(exercise == "4"):
        return "test_update_professor_ages"
    elif(exercise == "5"):
        return "test_get_professor"
    elif(exercise == "6"):
        return "test_get_professors"


def get_hint(exercise):
    if (exercise == "0"):
        return "https://docs.djangoproject.com/en/2.1/ref/models/querysets/#select-related"
    elif(exercise == "1"):
        return "https://docs.djangoproject.com/en/2.2/ref/models/querysets/#prefetch-related"
    elif(exercise == "2"):
        return "https://docs.djangoproject.com/en/2.2/ref/models/querysets/#update"
    elif(exercise == "3"):
        return "https://docs.djangoproject.com/en/2.2/ref/models/querysets/#bulk-create"
    elif(exercise == "4"):
        return "https://docs.djangoproject.com/en/2.2/ref/models/expressions/#f-expressions"
    elif(exercise == "5"):
        return "https://docs.djangoproject.com/en/2.2/ref/models/options/#django.db.models.Options.indexes"
    elif(exercise == "6"):
        return "https://docs.djangoproject.com/en/2.1/ref/models/querysets/#in"


@task(
    help={
        "exercise": "number of which exercise folder is being attempted",
        "hint": "show hint for exercise"
    }
)
def test(ctx, exercise, hint=False):
    if hint:
        ctx.run("echo See documentation: {}".format(get_hint(exercise)), pty=True)
        return

    ctx.run("pytest -v -k {}".format(get_test(exercise)), pty=True)

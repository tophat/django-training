from invoke import run, task


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
        ctx.run(f"echo See documentation: {get_hint(exercise)}", pty=True)
        return

    ctx.run(f"pytest -v -k exercise_{exercise}", pty=True)

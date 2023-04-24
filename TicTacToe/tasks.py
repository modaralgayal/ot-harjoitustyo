from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests/main_test.py", pty = True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src/tests/main_test.py", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def report(ctx):
    ctx.run("coverage report", pty = True)

@task 
def lint(ctx):
    ctx.run("pylint src", pty=True)
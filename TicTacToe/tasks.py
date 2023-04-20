from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python3 main.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest tests/main_test.py", pty = True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest tests/main_test.py", pty=True)

@task()
def coverage_report(ctx):
    ctx.run("coverage html", pty=True) 

@task 
def lint(ctx):
    ctx.run("pylint src", pty=True)
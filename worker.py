from celery import Celery

app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    task_routes={"task_1": {"queue": "queue_a"}, "task_2": {"queue": "queue_b"}},
    broker_connection_retry=True,
    broker_connection_retry_on_startup=True,
)


@app.task(name="task_1")
def task_1():
    print("hello from task_1")


@app.task(name="task_2")
def task_2():
    print("hello from task_2")

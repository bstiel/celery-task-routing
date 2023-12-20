import time
from worker import app


def main():
    while True:
        app.send_task("task_1")
        app.send_task("task_2")
        time.sleep(1)


if __name__ == "__main__":
    main()

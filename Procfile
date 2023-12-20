producer: python producer.py 
worker_1: celery --app=worker.app worker --pool=solo --queues=queue_a
worker_2: celery --app=worker.app worker --pool=solo --queues=queue_b

producer: python producer.py 
worker1: celery --app=worker.app worker --pool=solo --queues=queue_a
worker2: celery --app=worker.app worker --pool=solo --queues=queue_b

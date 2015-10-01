# Job Runner

## Description

This is a simple asynchronous job runner written in Python. It uses Redis as a queue system and docker to easily create containers. A producer add a job description in queue looking like this : 

```json
{
    "type": "print",
    "name": "nameOfTheJob",
    "params": {
        "text": "Hello world"
    }
}
```

The next producer will pop the next job, create the correct class corresponding and execute the job. The idea is that you can have lots of producers and lots of consumers on different machines, using one Queue system. Jobs can be added in different languages.

## Quick example

```python
# default: localhost, 6379
redis_queue = RedisQueue()                                              
job_runner = JobRunner(redis_queue)                                     # Create the job runner
job_runner.add_job(PrintJob("myFirstJob", {"text": "Hello World"}))     # Add a job of type PrintJob
job_runner.run()                                                        # Run every job it can
# Will print "Hello World"
```

## Run samples

The samples here are available in the [example folder](examples). You can use docker and docker-compose to easily test these.

### Simple

You could create a redis container and a producing and consuming container.

```bash
# Create a redis container
docker run -d --name redis
# First build a docker image using the Dockerfile
docker build -t epayet/job-runner .
# Then run the simple example
docker run --link redis --rm epayet/job-runner examples/simple.py
```

This example add 20 jobs, then run them (print 20 times). Checkout [examples/simple.py](examples/simple.py).

## Multiple producers and consumers

We can easily add producers and consumers using docker-compose. The current [docker-compose.yml](docker-compose.yml) creates 2 producers and 1 consumer, using 1 redis container. They use the simples scripts [examples/simple-producer.py](examples/simple-producer.py) and [examples/simple-consumer.py](examples/simple-consumer.py)

```bash
docker-compose up
```

## How to

### Add your own job

Job definition are on the [job/jobs folder](job/jobs). You have to create a class inheriting from the Job class, add an unique `self.type = "theUniqueTypeOfYourJob"` in the constructor, and have a `run` method. Checkout the [PrintJob](job/jobs/PrintJob.py) job for example.

### MemoryQueue

You can replace the Redis queue by a simple memory queue (will vanish after your program stops), which is great for testing.

```python
memory_queue = MemoryQueue()
job_runner = JobRunner(memory_queue)
# The rest is similar
```

## Contributing

Pull requests and comments are welcome!

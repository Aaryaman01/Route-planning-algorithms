from task3_algorithmic_strategies.weighted_job_scheduling import (
    Job,
    weighted_job_scheduling
)


jobs = [
    Job(1, 3, 50),
    Job(2, 5, 20),
    Job(4, 6, 70),
    Job(6, 7, 60),
    Job(5, 8, 30),
    Job(7, 9, 40)
]

result = weighted_job_scheduling(jobs)

print("Maximum profit:", result)
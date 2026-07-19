from dataclasses import dataclass


@dataclass
class Job:
    start: int
    finish: int
    profit: int


def weighted_job_scheduling(jobs):
    if not jobs:
        return 0

    jobs = sorted(
        jobs,
        key=lambda job: job.finish
    )

    dp = [0] * len(jobs)
    dp[0] = jobs[0].profit

    for i in range(1, len(jobs)):
        include_profit = jobs[i].profit

        previous_job = -1

        for j in range(i - 1, -1, -1):
            if jobs[j].finish <= jobs[i].start:
                previous_job = j
                break

        if previous_job != -1:
            include_profit += dp[previous_job]

        dp[i] = max(
            include_profit,
            dp[i - 1]
        )

    return dp[-1]
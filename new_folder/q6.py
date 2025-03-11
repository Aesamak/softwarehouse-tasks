import heapq

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

    def __lt__(self, other):
        return self.profit > other.profit  

def job_scheduling(jobs):
    
    jobs.sort(key=lambda job: job.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)  
    result = [-1] * (max_deadline + 1)  
    max_profit = 0
    job_count = 0

    for job in jobs:
        for slot in range(min(max_deadline, job.deadline), 0, -1):
            if result[slot] == -1:  
                result[slot] = job.job_id
                max_profit += job.profit
                job_count += 1
                break

    scheduled_jobs = [job_id for job_id in result if job_id != -1]
    return job_count, max_profit, scheduled_jobs


jobs = [
    Job("A", 2, 100),
    Job("B", 1, 50),
    Job("C", 2, 20),
    Job("D", 1, 40),
    Job("E", 3, 30)
]

count, profit, scheduled_jobs = job_scheduling(jobs)
print(f"Total Jobs Scheduled: {count}")
print(f"Total Profit: {profit}")
print(f"Scheduled Jobs Order: {scheduled_jobs}")

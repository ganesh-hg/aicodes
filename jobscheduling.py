def JobScheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
 
    job = ['-1'] * t
    for i in range(n):
        for j in range(min(t-1, arr[i][1]-1), -1, -1):
            if job[j] == '-1':
                job[j] = arr[i][0]
                break
    print(job)

arr = [['a', 2, 100],
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

print("Following is maximum profit sequence of jobs:")
JobScheduling(arr, 3)

#Output

''' The JobScheduling function takes two parameters: arr - a list of jobs where each job is represented by a list [job_id, deadline, profit], and t - the maximum time or deadline available for scheduling the jobs.

The variable n is initialized with the length of the arr list, which represents the number of jobs.

The code uses a bubble sort algorithm to sort the jobs in descending order of their profits. The outer loop iterates n times, and the inner loop iterates n - 1 - i times to compare adjacent jobs and swap them if their profits are not in the desired order.

After the jobs are sorted based on profits, the job list is initialized with t elements, each set to '-1'. This list will represent the scheduled jobs at different time slots.

The code then iterates over each job in the sorted arr list. It starts from the job with the highest profit.

Within the outer loop, there is an inner loop that iterates from min(t-1, arr[i][1]-1) down to 0. This inner loop selects the time slots for scheduling the jobs.

If the job list at the current time slot j is '-1', it means the time slot is available, and the current job can be scheduled in that slot.

When an available time slot is found, the job list is updated with the job ID (arr[i][0]) at that time slot, and the loop is broken using the break statement.

The algorithm continues this process until all the jobs are scheduled or all time slots are filled.

Finally, the code prints the job list, which represents the maximum profit sequence of the scheduled jobs.

The arr list is defined with job information, including job IDs, deadlines, and profits.

The JobScheduling function is called with the arr list and t = 3 as parameters to schedule jobs within a maximum of three time slots.

The scheduled job sequence is printed as the output.

In summary, the code implements a job scheduling algorithm that sorts the jobs based on their profits in descending order and schedules the jobs in time slots based on their deadlines. The goal is to maximize the total profit by selecting jobs with higher profits and scheduling them before their respective deadlines. The output shows the sequence of jobs scheduled to maximize the profit. '''

from datetime import date

def fine(due, ret):
    fine = 0

    if ret > due:
        if due.year == ret.year:
            if due.month == ret.month:
                fine = 15 * (ret.day - due.day)
            else:
                fine = 500 * (ret.month - due.month)
        else:
            fine = 10000

    return fine


return_date = list(map(int, input().split()))
return_date = date(day=return_date[0], month=return_date[1], year=return_date[2])

due_date = list(map(int, input().split()))
due_date = date(day=due_date[0], month=due_date[1], year=due_date[2])

fine = fine(due_date, return_date)
print(fine)

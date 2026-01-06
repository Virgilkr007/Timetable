courses = []

high_rank = []
mid_rank = []
low_rank = []

WEIGHTS = {
    "A": 25,
    "B": 15,
    "C": 9
}

def request_input():
    num_of_courses = int(input("Enter the number of courses you want to add: "))

    for i in range(num_of_courses):
        course = {
            "title": input("Enter course name: "),
            "units": int(input("Number of units: ")),
            "importance": bool(int(input("Important OR Not important (1/0): ")))
        }
        courses.append(course)

def compute_status(course):
    if course["units"] >= 3 and course["importance"]:
        return "A"
    elif (course["units"] >= 3 and not course["importance"]) or \
         (course["units"] <= 2 and course["importance"]):
        return "B"
    else:
        return "C"

def weight_func(course):
    status = compute_status(course)
    course["status"] = status
    course["weight"] = WEIGHTS[status]

    if status == "A":
        high_rank.append(course)
    elif status == "B":
        mid_rank.append(course)
    else:
        low_rank.append(course)

def compute_total_weight():
    return (
        len(high_rank) * WEIGHTS["A"] +
        len(mid_rank) * WEIGHTS["B"] +
        len(low_rank) * WEIGHTS["C"]
    )

def available_slots():
    hours_per_day = int(input("Enter number of hours you want to study per day: "))
    period = int(input(
        "1=1week 2=2weeks 3=1month 4=2 months 5=3 months 6=6 months 7=1year : "
    ))

    days_map = [7, 14, 30, 60, 90, 180, 365]
    total_days = days_map[period - 1]

    return total_days, hours_per_day, total_days * hours_per_day

def slot_allocation():
    total_days, hours_per_day, total_slots = available_slots()
    W = compute_total_weight()

    for course in high_rank + mid_rank + low_rank:
        course["slots"] = round((course["weight"] / W) * total_slots)
        course["remaining"] = course["slots"]

    return total_days, hours_per_day

def daily_schedule(total_days, hours_per_day):
    timetable = {}

    for day in range(1, total_days + 1):
        timetable[f"Day {day}"] = []
        daily_slots = hours_per_day

        while daily_slots > 0:
            available = [c for c in courses if c["remaining"] > 0]
            if not available:
                break

            available.sort(key=lambda c: c["weight"], reverse=True)
            course = available[0]

            timetable[f"Day {day}"].append(course["title"])
            course["remaining"] -= 1
            daily_slots -= 1

    return timetable

request_input()

for c in courses:
    weight_func(c)

total_days, hours_per_day = slot_allocation()
timetable = daily_schedule(total_days, hours_per_day)

for day, plan in timetable.items():
    print(day, plan)

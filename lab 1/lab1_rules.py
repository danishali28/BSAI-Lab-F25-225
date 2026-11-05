#Lab 1 - Task 2

Min_score = 70
Min_attendance = 75

def screen(score,documents, attendance, letters):
    reason = []

    if score < Min_score:
        reason.append("Score is below 70")

    if not documents:
        reason.append("Documents are incomplete")

    if score < Min_attendance:
        reason.append("Attendance is below 75")

    if letters < 1:
        reason.append("Recommendation letter missing")

    if reason:
        return "Hold", ":".join(reason)

    return "Review", "All condition are satisfied"

test = [
    ("T1_pass",85,True,90,2,"Review"),
    ("T2_fail_attendance",85,True,60,2,"Hold"),
    ("T3_fail_recommend",85, True,90,0,"Hold"),
    ("T4_boundary",70,True,75,1,"Review")
]

print("All thresholds are synthetic lab assumptions")

passed = 0

for name, score, docs, attendance, letters, expected in test:
    actual, reason= screen(score, docs, attendance, letters)

    status = "PASS" if actual == expected else "FAIL"
    passed += (status == "PASS")

    print("-"*40)
    print("case" ,name)
    print("Expected",expected)
    print("Actual", actual)
    print("Reason", reason)
    print("Result", status)

print("-"*40)
print("Test passed:", passed,"/",len(test))
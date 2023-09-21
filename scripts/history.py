from git import Repo
import csv
import hashlib
import sys

certifications_file = sys.argv[1]

writer = csv.DictWriter(
    sys.stdout,
    fieldnames=[
        "school",
        "school_id",
        "student_count",
        "certExpirationDate",
        "position",
        "trainerOneFullName",
        "trainerTwoFullName",
        "employeeHash",
        "observedDate",
    ],
)
writer.writeheader()

rows = []

repo = Repo(".")
for commit in repo.iter_commits(paths=certifications_file):
    repo.git.checkout(commit, force=True)
    with open(certifications_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            employee_hash = hashlib.sha256(
                (row.pop("employeeFullName") + row["school_id"]).encode()
            ).hexdigest()
            row["employeeHash"] = employee_hash
            row["observedDate"] = commit.authored_datetime.date()

            rows.append(row)

repo.git.checkout("main")

writer.writerows(rows)

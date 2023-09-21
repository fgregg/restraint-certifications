import requests
import csv
import sys

writer = csv.DictWriter(
    sys.stdout,
    fieldnames=[
        "school",
        "school_id",
        "student_count",
        "employeeFullName",
        "certExpirationDate",
        "position",
        "trainerOneFullName",
        "trainerTwoFullName",
    ],
)
writer.writeheader()

session = requests.Session()

schools = session.get(
    "https://api.cps.edu/schoolprofile/CPS/AllSchoolProfiles"
).json()

for school in schools:
    school_name = school["SchoolShortName"]
    school_id = school["SchoolID"]
    student_count = school["StudentCount"]
    certifications = session.get(
        f"https://api.cps.edu/prto/api/CertifiedEmployees?schoolId={school_id}"
    ).json()
    for certification in certifications:
        del certification['schoolId']
        del certification['schoolShortName']
        del certification['schoolLongName']
        certification["school"] = school_name
        certification["school_id"] = school_id
        certification["student_count"] = student_count
        writer.writerow(certification)

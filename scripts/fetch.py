import requests
import csv
import sys

writer = csv.DictWriter(
    sys.stdout,
    fieldnames=[
        "school",
        "school_id",
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
    "https://api.cps.edu/schoolprofile/CPS/TypeaheadSchoolSearch"
).json()

for school in schools:
    school_name = school["SchoolShortName"]
    school_id = school["SchoolID"]
    certifications = session.get(
        f"https://api.cps.edu/prto/api/CertifiedEmployees?schoolId={school_id}"
    ).json()
    for certification in certifications:
        certification["school"] = school_name
        certification["school_id"] = school_id
        writer.writerow(certification)

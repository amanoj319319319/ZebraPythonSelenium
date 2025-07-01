# conftest.py
import requests
import pytest

TESTRAIL_URL = "https://bubbu0101.testrail.io"
USERNAME = "bubbududdu0101@gmail.com"
API_KEY = "G26Vl0F.WPNb2ofioaw8-dqiuffOVIdPYRFbxUg46"
RUN_ID = 1

def add_result_for_case(case_id, status_id, comment=""):
    endpoint = f"{TESTRAIL_URL}/index.php?/api/v2/add_result_for_case/{RUN_ID}/{case_id}"
    payload = {
        "status_id": status_id,
        "comment": comment
    }

    print(f"Sending result to TestRail: Case ID={case_id}, Status ID={status_id}, Comment={comment}")
    print(f"POST {endpoint}")

    response = requests.post(endpoint, auth=(USERNAME, API_KEY), json=payload)

    print("Response Code:", response.status_code)
    print("Response Body:", response.text)

    if response.status_code == 200:
        print(f"[✓] Case {case_id} marked as status {status_id} in TestRail")
    else:
        print(f"[✗] Failed to update TestRail for case {case_id}")

    return response

# Pytest hook to be called after every test
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        marker = item.get_closest_marker("testrail_case_id")
        if marker:
            case_id = marker.args[0]
            passed = call.excinfo is None
            status_id = 1 if passed else 5
            comment = "Test passed" if passed else f"Test failed: {call.excinfo.value}"
            add_result_for_case(case_id, status_id, comment)

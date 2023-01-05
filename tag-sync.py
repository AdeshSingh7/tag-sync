#!/usr/bin/python3
import requests, csv, argparse, os

def get_project_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_id', help='The ID of the project')
    args = parser.parse_args()
    return args.project_id

def sync_tag(project_id, tag_id):
    json = {"activate_condition":{"project_id":project_id, "tag_id":tag_id}}
    response = requests.post('https://vehicle.parkplus.io/api/v1/sync-tag_infra/condition/', json=json)
    status = response.json()['count']
    if status != 0 and response.status_code == 200:
        print(f"\33[1;92m\u2714 Push cloud action for tag_id:{tag_id} on project_id:{project_id}\33[0m")
    else:print(f"\33[1;91m\u2716 Check hardware and configuration for project_id:{project_id}\33[0m")

def read_data(username):
    project_id = get_project_id()
    with open(f"/home/{username}/Downloads/tags/{project_id}.csv", "r", encoding="utf-8") as csv_file:
        data = csv.reader(csv_file)
        for lines in data:
            tag_id = lines[0]
            if tag_id in "tag_id":pass
            else:sync_tag(project_id, tag_id)

try:
    os.system('clear')
    username = os.popen('users').read().strip()
    if not os.path.exists(f"/home/{username}/Downloads/tags/"):
        os.makedirs(f"/home/{username}/Downloads/tags/")
    read_data(username)
except KeyboardInterrupt:exit(0)
except Exception:pass
finally:pass

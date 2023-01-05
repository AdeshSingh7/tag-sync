#!/usr/bin/python3
import requests, csv, argparse, time, os

def args():
    parser = argparse.ArgumentParser(description='Check Fastag details through vehicle number')
    parser.add_argument('-p', '--project', help='Project Id')
    return parser.parse_args()

def sync_tag(project_id, tag_id):
    json = {"activate_condition":{"project_id":project_id, "tag_id":tag_id}}
    response = requests.post('https://vehicle.parkplus.io/api/v1/sync-tag_infra/condition/', json=json)
    status = response.json()['count']
    if status == 0:
        print(f"\u2713 \33[91mCheck hardware and configuration for tag_id:{tag_id} project_id:{project_id}\33[0m")
    else:
        print(f"\u2713 \33[92mPush cloud action for tag_id:{tag_id} on project_id:{project_id}\33[0m")

def read_data():
    project_id = args().project
    with open("/home/"+username+"/Downloads/tags/"+project_id+".csv", "r", encoding="utf-8") as csv_file:
        data = csv.reader(csv_file)
        for lines in data:
            tag_id = lines[0]
            if tag_id in "tag_id":pass
            else:
                try:
                    sync_tag(project_id, tag_id)
                    time.sleep(.1)
                except Exception:pass

try:
    os.system('clear')
    username = os.popen('users').read().strip()
    if not os.path.exists(f"/home/{username}/Downloads/tags/"):
           os.makedirs(f"/home/{username}/Downloads/tags/")
    read_data()
except KeyboardInterrupt:pass
except Exception:pass
finally:pass

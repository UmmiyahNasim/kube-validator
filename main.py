import os
import sys
import glob
import yaml

result = []

def search_yaml_files(path, key, value):
    yaml_files = []

    if os.path.isfile(path):
        yaml_files.append(path)
    elif os.path.isdir(path):
        yaml_files = glob.glob(os.path.join(path, "*.yaml")) + glob.glob(os.path.join(path, "*.yml"))

    for file in yaml_files:
        with open(file) as f:
            data = yaml.safe_load(f)
            search_yaml_data(data, key, value, 0, "")
            print(result)

def search_yaml_data(data, argKey, value, cur, curKey):
    if value == str(data):
        result.append(curKey + ", " + value)
        return
    

    keyArray = argKey.split(".")
    if cur >= len(keyArray):
        return

    key = keyArray[cur]

    if isinstance(data, dict) and key in data:
        search_yaml_data(data[key], argKey, value, cur+1, curKey + "." + key)
    else:
        key = key.strip(']')
        split = key.split('[')
        key = split[0]
        if isinstance(data, dict) and isinstance(data[key], list):
            if split[1] == '*':
                for i, item in enumerate(data[key]):
                    search_yaml_data(item, argKey, value, cur+1, curKey + "." + key + "[" + str(i) + "]")
            else:
                index = int(split[1])
                search_yaml_data(data[key][index], argKey, value, cur+1, curKey + "." + key + "[" + str(index) + "]")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Insufficient arguments provided. Usage: python yaml_search.py <path> <key> <value>")
        sys.exit(1)

    path = sys.argv[1]
    key = sys.argv[2]
    value = sys.argv[3]

    search_yaml_files(path, key, value)



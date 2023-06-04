import os
import sys
import glob
import yaml


result = []

def search_yaml_files(path, key, value):
    """
    Search YAML files for a specific key-value pair.
    
    Args:
        path (str): Path to the YAML file(s) or directory.
        key (str): Key to search for.
        value (str): Value to match against the key.
    """
    yaml_files = []
    if os.path.isfile(path):
        yaml_files.append(path)
    elif os.path.isdir(path):
        yaml_files = glob.glob(os.path.join(path, "*.yaml")) + glob.glob(os.path.join(path, "*.yml"))

    for file in yaml_files:
        with open(file) as f:
            data = yaml.load_all(f, Loader=yaml.FullLoader)
            for root in data:
                search_yaml_data(root, key, value, 0, "", file)

    for i in result:
        print(i,  sep = "\n")

def search_yaml_data(data, argKey, value, cur, curKey, file):
    """
    Recursive function to search YAML data for a specific key-value pair.
    
    Args:
        data (dict or list): YAML data to search.
        argKey (str): Key to search for.
        value (str): Value to match against the key.
        cur (int): Cursor position.
        curKey (str): Current key path.
        file (str): File name.
    """

    if value == str(data):
        result.append(curKey.strip('.') + " " + value + " " + file )
        return

    keyArray = argKey.split(".")
    if cur >= len(keyArray):
        return

    key = keyArray[cur]

    if isinstance(data, dict) and key in data:
        try:
            search_yaml_data(data[key], argKey, value, cur+1, curKey + "." + key, file)
        except KeyError as e:
            pass

    else:
        key = key.strip(']')
        split = key.split('[')
        key = split[0]
        if isinstance(data, dict) and isinstance(data[key], list):
            if split[1] == '*':
                for i, item in enumerate(data[key]):
                    curKey = curKey + "." + key + "[" + str(i) + "]"
                    search_yaml_data(item, argKey, value, cur+1, curKey, file)
            else:
                index = int(split[1])
                curKey = curKey + "." + key + "[" + str(index) + "]"
                search_yaml_data(data[key][index], argKey, value, cur+1, curKey, file )

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Insufficient arguments provided. Usage: python yaml_search.py <path> <key> <value>")
        sys.exit(1)

    path = sys.argv[1]
    key = sys.argv[2]
    value = sys.argv[3]

    search_yaml_files(path, key, value)




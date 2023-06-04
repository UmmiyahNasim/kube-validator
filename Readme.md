# kube-yaml-validator

## Description
The kube-yaml-validator is a tool designed to automate the review of Kubernetes YAML configuration files. It helps ensure that the YAML files follow specified rules and best practices set by the SRE team. By running this tool, you can quickly validate multiple YAML files against predefined rules, saving time and effort in the review process.

## Features
- Validates Kubernetes YAML configuration files against predefined rules.
- Supports checking specific keys and values in YAML files.
- Handles individual YAML files, multiple YAMLs in a single file, directories, and nested directories.
- Prints the matching keys, values, and relative file paths for easy review.

## Requirements
Python 3.6 or above

Docker (if running as a Docker container

## Running the Script via Python

### Local Installation
1. Clone the repository: `git clone https://github.com/UmmiyahNasim/kube-yaml-validator.git`
2. Navigate to the project directory: `cd kube-validator`
3. Install the dependencies: `pip install -r requirements.txt`

To run the kube-yaml-validator locally, use the following command:

```shell
python main.py <file or directory path> <key> <value>
```

`<file or directory path>`: Path to a YAML file or a directory containing YAML files to be validated.

`<key>`: Key string to be searched in the YAML files. Use dot notation for nested keys, e.g., `spec.template.spec.containers[*].ports[*].containerPort`.

`<value>`: Value to be matched against the specified key.

### Sample Input and Output
Here are a few examples of running the kube-yaml-validator with different inputs and outputs:

Example 1: Single YAML file

Input:

```shel
python main.py example.yaml 'spec.template.spec.containers[*].ports[*].containerPort' 443 
```
Output:

``` shel
key = spec.template.spec.containers[0].ports[0].ports[1].containerPort, value = 443, example.yaml
```

Example 2: YAML files in a directory

Input:

```shel
python main.py kube-yaml 'spec.ports[*].name' http
```

Output:
```shel
key = spec.ports[0].name, value = http, kube-yaml/svc.yaml
key = spec.ports[0].name, value = http, kube-yaml/example.yaml
```

## Running via Docker


The kube-yaml-validator can also be executed as a Docker container. This approach eliminates the need to install dependencies and ensures consistent execution across different environments.

### Docker Installation
1. Clone the repository: `git clone https://github.com/UmmiyahNasim/kube-yaml-validator.git`
2. Navigate to the project directory: `cd kube-validator`
3. Build the Docker image: `docker build -t kube-yaml-validator .`

Run the Docker container, providing the necessary arguments.

```shell
docker run --rm --mount type=bind,source=/path/to/file,target=/app/file.yaml kube-yaml-validator /app/file.yaml key_to_search value_to_match
```

`/path/to/yaml/files`: The local path to the directory containing the YAML files to be validated.
`<path>`, `<key>`, `<value>`: Same as described in the script usage.

Example:

```shell
docker run --rm --mount type=bind,source=</path/to/kube-yaml/files>,target=/app/kube-yaml kube-yaml-validator kube-yaml spec.replicas 2
```

  
## GitHub Workflow
A GitHub Actions workflow is included in the repository to automatically run the kube-yaml-validator on pull requests, pushes, and manually triggered workflows. The workflow scans the repository for YAML files and executes the validation process.

To enable the workflow, create a .github/workflows/main.yml file in your repository and paste the following content:

``` shell
name: Kube-YAML-Validator
on:
  pull_request:
  push:
  workflow_dispatch:

jobs:
  scan:
    name: Kube-YAML-Validator
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Execute validation
        run: python main.py <file or directory path> <key> <value>
  ```
  
  Replace `<file or directory path>`, `<key>`, and `<value>` in the last line of the workflow file with your desired values.


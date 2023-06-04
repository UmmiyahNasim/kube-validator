# kube-yaml-validator

## Description
The kube-yaml-validator is a tool designed to automate the review of Kubernetes YAML configuration files. It helps ensure that the YAML files follow specified rules and best practices set by the SRE team. By running this tool, you can quickly validate multiple YAML files against predefined rules, saving time and effort in the review process.

## Features
- Validates Kubernetes YAML configuration files against predefined rules.
- Supports checking specific keys and values in YAML files.
- Handles individual YAML files, multiple YAMLs in a single file, directories, and nested directories.
- Prints the matching keys, values, and relative file paths for easy review.

## Requirements
- Python 3.10 or higher
- Docker (optional, for running the tool as a Docker container)

## Installation

### Local Installation
1. Clone the repository: `git clone https://github.com/your-username/kube-yaml-validator.git`
2. Navigate to the project directory: `cd kube-yaml-validator`
3. Install the dependencies: `pip install -r requirements.txt`

### Docker Installation
1. Clone the repository: `git clone https://github.com/your-username/kube-yaml-validator.git`
2. Navigate to the project directory: `cd kube-yaml-validator`
3. Build the Docker image: `docker build -t kube-yaml-validator .`

## Usage

### Local Usage
To run the kube-yaml-validator locally, use the following command:



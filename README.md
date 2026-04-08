# AutoCoder

## Description
AutoCoder is an automated workflow project designed to integrate ChatGPT capabilities directly into a continuous integration/continuous deployment (CI/CD) pipeline. This public repository stores the necessary GitHub Actions configuration files and custom Bash scripts required to interact with the OpenAI API. 

The goal of this project is to automate code-related tasks, reviews, or generation processes by triggering AI-driven scripts via GitHub Actions.

## Project Structure
The repository is organized as follows:

```text
AutoCoder/
    │
    ├── .github/                 
    │   └── workflows/           
    │       └── main.yml         # GitHub Actions workflow configuration
    │
    ├── scripts/                 
    │   └── script.sh            # Bash script to interact with the ChatGPT API
    │
    └── README.md                # Project documentation
test
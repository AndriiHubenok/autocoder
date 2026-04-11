# AutoCoder

## Description
AutoCoder is an advanced, automated workflow project meticulously designed to integrate OpenAI's powerful ChatGPT capabilities directly into a continuous integration and continuous deployment (CI/CD) pipeline using GitHub Actions. This public repository serves as the home for a custom, reusable composite GitHub Action, along with the necessary configuration files and robust Bash scripts required to facilitate seamless interaction with the OpenAI API.

The primary goal of this project is to revolutionize the software development lifecycle by fully automating code generation processes. By utilizing GitHub Issues as a user interface, developers can simply open a new issue with detailed requirements and assign a specific trigger label. Once triggered, the AutoCoder action springs into motion. It securely fetches the issue context, constructs a highly specific prompt, and queries the ChatGPT model to generate production-ready code.

Furthermore, the system is engineered to parse the AI's JSON-formatted response, automatically saving the generated code snippets into their designated file paths. It then handles the Git operations natively, staging the new files, committing them under a dedicated bot account, and seamlessly opening a new Pull Request against the main branch. This creates an end-to-end automated pipeline that reduces manual boilerplate coding, accelerates prototyping, and ensures that all AI-generated code is funneled through standard peer-review processes before merging.

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

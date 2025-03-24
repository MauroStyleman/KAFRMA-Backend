# Ghost Hunting AI - Service

## We have developed a service using LLM, RAG, and MCP that generates a guided tour with puzzles for each location, based on your own text files.

## Frontend
Link to the frontend repository: [KAFRMA-Frontend](https://github.com/MauroStyleman/KAFRMA-Frontend)

## Team
- **Kacper Chrolowski**  
  - [LinkedIn](https://www.linkedin.com/in/kacper-chrolowski-b16606212/)
- **Frans Dillen**  
  - [LinkedIn](https://www.linkedin.com/in/frans-dillen-99b42a235/)
- **Mauro Styleman**  
  - [LinkedIn](https://www.linkedin.com/in/mauro-styleman-696936258/)

## Usage
```bash
python main.py
```
## Setup Requirements

### Logs

You need to create a log directory in the root of the project.
### MCP

Create a new directory named credentials in the root of the project.
Inside this directory, create a .env file containing the following variables:
GOOGLE_DRIVE_FOLDER_ID: Specifies the folder where all data passed to the RAG is stored.
OPENROUTER_API_KEY: Stores your LLM API key.

### Additional Requirements

Ensure you have Python installed (recommended version: 3.8 or higher).
Install the required dependencies using:
pip install -r requirements.txt
Make sure your API keys are valid and have the necessary permissions.
Verify that your Google Drive folder contains the correct data before running the service.
Ensure these steps are completed to enable the service to function correctly.

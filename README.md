# Google Agent Development Kit (ADK) Project

This project is set up for developing agents using the Google Agent Development Kit (ADK).

## [Open in Firebase Studio](https://studio.firebase.google.com/import?url=https://github.com/luissala/adk-template)

This project works in Firebase Studio, simply click the button below:
[![Open in Firebase Studio](https://camo.githubusercontent.com/7a349c395a3a2a9050cc583b82b267a1d6ed7d62240f4e6f86753b5dfa157bf6/68747470733a2f2f63646e2e666972656261736573747564696f2e6465762f62746e2f6f70656e5f6461726b5f33324032782e706e67)](https://studio.firebase.google.com/import?url=https://github.com/luissala/adk-template)

## Getting Started

This project uses Poetry for dependency management and packaging.

1.  **Install Poetry**: If you don't have Poetry installed, follow the official installation guide: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

2.  **Install Dependencies**: Navigate to the project root directory in your terminal and run:

```bash
$ poetry install
```

3. **Create a  `.env` File:** Copy `agents/.sample.env` to `agents/.env` and edit it to include either an AI Studio API Key or Vertex AI project details.

```bash
# USING VERTEX AI? 
# If so, change to TRUE and edit the GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION variables.
# Otherwise, change to FALSE and add your GOOGLE_API_KEY.
export GOOGLE_GENAI_USE_VERTEXAI=FALSE

# GOOGLE AI STUDIO API KEY
export GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE

# VERTEX AI
export GOOGLE_CLOUD_PROJECT=PASTE_YOUR_ACTUAL_PROJECT_ID
export GOOGLE_CLOUD_LOCATION=us-central1
```

4. **Run ADK:**

```bash
$ poetry env activate
$ adk web ./agents

or

$ poetry run adk web ./agents
```

## Learn More
* [Google Agent Development Kit Documentation](https://google.github.io/adk-docs)
# LangChain-demo

This is a demo project to demonstrate the usage of the LangChain framework.

Currently, this project integrates with the following Large Language Models (LLMs):

- OpenAI (https://openai.com/index/openai-api/)
- AFS (https://docs.twcc.ai/docs/user-guides/twcc/afs/api-and-parameters/conversation-api)

In the future, we plan to add support for additional APIs such as Ollama and others.
Stay tuned for updates!

## Start the project

### Prerequisites

- Poetry
- Pyenv

> more details on how to install and setup pyenv and poetry can be found in the [appendix](docs/appendix.md)
> (or enable `virtualenvs.prefer-active-python` to `true`)

### Initial project

1. Clone this repository

2. Install dependencies using `poetry`

    ```shell
    poetry install --no-root
    ```
3. Signup for [LangSmith](https://smith.langchain.com)
4. Remember the API key from the LangSmith-Personal-API Keys

### Configure project

Checkout Available models:

- OpenAI: https://platform.openai.com/docs/models
- AFS: https://docs.twcc.ai/docs/user-guides/twcc/afs/available-model/

1. Modify the `config/config.yaml` file to set the `model` and `question` fields
2. Create a `.env` file based on the `.env.example` file. `cp .env.example .env`
3. Set all the environment variables in the `.env` file

### Start the project

Run the following command to start the FastAPI server using Uvicorn:

```shell
poetry run uvicorn main:app --reload
```

or 

```shell
poetry run fastapi dev main.py
```

## Common Error Resolutions

If you encounter the following error:
> TypeError: 'FieldInfo' object is not a mapping

You can resolve it by installing a specific version of the Pydantic library. Run the following command in your terminal:

```shell
pip install pydantic==1.10.2
```
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

> more details on how to install and setup pyenv and poetry can be found in the appendix

[//]: # (or enable `virtualenvs.prefer-active-python` to `true`)

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

## Common Error Resolutions

If you encounter the following error:
> TypeError: 'FieldInfo' object is not a mapping

You can resolve it by installing a specific version of the Pydantic library. Run the following command in your terminal:

```shell
pip install pydantic==1.10.2
```

## Appendix

### Install and setup pyenv and poetry

#### Arch Linux

1. Install pyenv

   ```shell
   yay -S pyenv
   ```
   Add the following lines to your shell configuration file

   ```shell
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```

2. Install python using pyenv

   ```shell
   pyenv install 3.12.2
   ```

3. Install poetry

   Switch current shell and check which python executable is using

      ```shell
      pyenv shell 3.12.2
      which python
      ```

   Should return something like `/home/user/.pyenv/shims/python`. then run the following command

      ```shell
      curl -sSL https://install.python-poetry.org | python -
      ```
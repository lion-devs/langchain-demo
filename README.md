# langchain-demo


## Basic dependencies

```shell
pip install langchain
pip install -qU langchain-openai
pip install python-dotenv
pip install fastapi
```

## Start the project

1. Signup for [LangSmith](https://smith.langchain.com)
2. Copy the API key from the LangSmith-Personal-API Keys
3. Create a `.env` file based on the `.env.example` file. `cp .env.example .env`
4. Set all the environment variables in the `.env` file
5. Run the following command to start the FastAPI server

```shell
fastapi dev main.py
```


## Common Error Resolutions

If you encounter the following error:
> TypeError: 'FieldInfo' object is not a mapping

You can resolve it by installing a specific version of the Pydantic library. Run the following command in your terminal:
```shell
pip install pydantic==1.10.2
```
import uvicorn
from typing import List, Dict
import datetime
import pandas as pd
import requests
from fastapi import FastAPI, APIRouter, HTTPException
from config.common import Settings
from utils.logger import logger

base_setting=Settings()
root_path=base_setting.api_main_path

logger.info('Initialising comment classification API')

app = FastAPI(
        title="Comment Analysis API",
        version="0.0.1",
        openapi_url=f'{root_path}/openapi.json',
        docs_url = f'{root_path}/docs',
        redoc_url = f'{root_path}/redoc'
    )
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
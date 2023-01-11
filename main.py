import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from lib.postgresql import database, engine
from modules.user import router as user_router
from tables import metadata as psql_metadata

load_dotenv()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix='/user')


@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(psql_metadata.create_all)
    await engine.dispose()
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

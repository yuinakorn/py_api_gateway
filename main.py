from fastapi import FastAPI

from routers import auth_router, query_router
# allow CORS origin
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values

config_env = dotenv_values(".env")

app = FastAPI(docs_url="/api-docs", redoc_url=None)

origins = [
    config_env["CORS_ORIGIN1"]
]

print(origins)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(query_router.router)
app.include_router(auth_router.router)
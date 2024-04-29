from fastapi import FastAPI

from routers import auth_router, query_router

app = FastAPI(docs_url="/api-docs", redoc_url=None)


app.include_router(query_router.router)
app.include_router(auth_router.router)
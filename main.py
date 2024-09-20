from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.api.routers import api_router
from app.core.config import APP_VERSION, APP_NAME
from app.core.database import Base, engine
from app.core.exceptions import NotFoundError, InvalidInputError
from app.utils.jsend import JSendResponse

app = FastAPI(
    title=APP_NAME,
    description='Esto es un proyecto diseñado en FastAPI',
    version=APP_VERSION,
    openapi_tags=[
        {
            "name": "Auth",
            "description": "Todas las operaciones relacionadas con la autenticación.",
        }
    ]
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


"""@app.middleware("http")
async def validate_doc_access(request: Request, call_next):
    if request.url.path.startswith("/docs") or request.url.path.startswith("/redoc"):
        password = request.query_params.get("password")
        if password != "secret_password":
            raise HTTPException(status_code=401, detail="No autorizado")
    return await call_next(request)"""


@app.on_event("startup")
def startup_event():
    # Crear las tablas en la base de datos al iniciar la aplicación
    Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
def shutdown_event():
    # Aquí puedes poner cualquier lógica de limpieza que necesites cuando la aplicación se apague
    pass


@app.exception_handler(NotFoundError)
async def not_found_exception_handler(request: Request, exc: NotFoundError):
    jsend_model = JSendResponse(status="fail", message=str(exc), status_code=400)
    return jsend_model


@app.exception_handler(InvalidInputError)
async def invalid_input_exception_handler(request: Request, exc: InvalidInputError):
    jsend_model = JSendResponse(status="fail", message=str(exc), status_code=400)
    return jsend_model


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

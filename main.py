from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from user.interface.controllers.user_controller import router as user_router

app = FastAPI()
app.include_router(user_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=400,
        content=exc.errors(),
    )

@app.get("/health")
def health_check():
    return {"status": "OK"}


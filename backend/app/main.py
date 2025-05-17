from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.routes import auth

# Create FastAPI app
app = FastAPI(
    title="School Management System API",
    description="API for School Management System",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Error handlers
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": str(exc)},
    )

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

# Root endpoint
@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to School Management System API"}

# Health check endpoint
@app.get("/api/health", tags=["health"])
async def health_check():
    return {"status": "ok"}

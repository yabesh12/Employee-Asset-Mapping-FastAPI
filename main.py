from api.employee.employee_api_endpoints import router as employee_router
from api.asset.asset_api_endpoints import router as asset_router
from api.asset_mapping.asset_mapping_endpoint import router as asset_mapping_router
from api.dashboard.dashboard_api_endpoints import router as dashboard_router
from fastapi import FastAPI
from fastapi.openapi.models import Info
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html



# main.py
openapi_info = Info(
    title="Employee Asset Mapping API",
    version="1.0",
    description="API documentation for Employee Asset Mapping.",
)

app = FastAPI(openapi_info=openapi_info)


# Include routers
app.include_router(employee_router, prefix="/employee", tags=["Employee"])
app.include_router(asset_router, prefix="/asset", tags=["Asset"])
app.include_router(asset_mapping_router, prefix="/mapping", tags=["Mapping"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])



# Root path endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Asset Mapping API"}

# Include Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Employee Asset Mapping API", redoc_url=None)


@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()
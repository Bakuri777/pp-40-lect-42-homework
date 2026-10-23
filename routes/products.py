from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from repositories.product_repository import ProductRepository
from schemas.product import ProductCreate, ProductResponse
from service.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])


def get_product_service(db: AsyncSession = Depends(get_db)):
    return ProductService(ProductRepository(db))


@router.get("/", response_model=list[ProductResponse])
async def get_products(
    service: ProductService = Depends(get_product_service)
):
    return await service.get_all_product()


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):
    return await service.get_product(product_id)


@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(
    data: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    return await service.create_product(data)

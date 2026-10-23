from fastapi import FastAPI

from core.config import settings
from routes import order_items, auth, user, products

app = FastAPI(debug=settings.debug)

app.include_router(order_items.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(products.router)



"""
{
  "id": 2,
  "name": "saxeli",
  "email": "test@example.com",
  "is_active": true
}


"""
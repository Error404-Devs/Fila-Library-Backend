from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints.books import books_router
from app.api.endpoints.authors import authors_router
from app.api.endpoints.publishers import publishers_router
from app.api.endpoints.collections import collections_router

router = FastAPI()

origins = ["http://localhost:5173"]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router.include_router(books_router, prefix="/api")
router.include_router(authors_router, prefix="/api")
router.include_router(publishers_router, prefix="/api")
router.include_router(collections_router, prefix="/api")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=8000)

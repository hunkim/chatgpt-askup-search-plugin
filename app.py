import os
from typing import Optional

import httpx
from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/.well-known", StaticFiles(directory=".well-known"),
          name=".well-known")


API_BASE_URL = "https://openapi.naver.com/v1/search/"

# Set your Naver API credentials here or as environment variables
NAVER_CLIENT_ID = os.environ["NAVER_CLIENT_ID"]
NAVER_CLIENT_SECRET = os.environ["NAVER_CLIENT_SECRET"]


async def get_naver_headers():
    return {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
    }


@app.get("/search/web", response_model=dict, summary="Web search")
async def search_web(query: str, headers: dict = Depends(get_naver_headers)):
    """
    Relay Naver web search results.

    Args:
        query (str): Search query.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL + "webkr.json", params={"query": query}, headers=headers)
    return response.json()


@app.get("/search/blog", response_model=dict, summary="Blog search")
async def search_blog(query: str, headers: dict = Depends(get_naver_headers)):
    """
    Relay Naver blog search results.

    Args:
        query (str): Search query.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL + "blog.json", params={"query": query}, headers=headers)
    return response.json()


@app.get("/search/movie", response_model=dict, summary="Movie search")
async def search_movie(query: str, headers: dict = Depends(get_naver_headers)):
    """
    Relay Naver movie search results.

    Args:
        query (str): Search query.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL + "movie.json", params={"query": query}, headers=headers)
    return response.json()


@app.get("/search/news", response_model=dict, summary="News search")
async def search_news(query: str, headers: dict = Depends(get_naver_headers)):
    """
    Relay Naver news search results.

    Args:
        query (str): Search query.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL + "news.json", params={"query": query}, headers=headers)
    return response.json()


@app.get("/search/local", response_model=dict, summary="Local search")
async def search_local(query: str, headers: dict = Depends(get_naver_headers)):
    """
    Relay Naver local search results.

    Args:
        query (str): Search query.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL + "local.json", params={"query": query}, headers=headers)
    return response.json()


@app.get("/search/book", response_model=dict, summary="Book search")
async def search_book(query: str, headers: dict = Depends(get_naver_headers)):
    """
    Relay Naver book search results.

    Args:
        query (str): Search query.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL + "book.json", params={"query": query}, headers=headers)
    return response.json()


@app.get("/search/image", response_model=dict, summary="Image search")
async def search_image(query: str, headers: dict = Depends(get_naver_headers)):
    """
    Relay Naver image search results.

    Args:
        query (str): Search query.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL + "image", params={"query": query}, headers=headers)
    return response.json()


@app.get("/search/shop", response_model=dict, summary="Shop search")
async def search_shop(query: str, headers: dict = Depends(get_naver_headers)):
    """
    Relay Naver shop search results.

    Args:
        query (str): Search query.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL + "shop.json", params={"query": query}, headers=headers)
    return response.json()
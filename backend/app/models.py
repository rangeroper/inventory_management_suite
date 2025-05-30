from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Tag(BaseModel):
    id: Optional[str] = None  # DB-generated ID
    name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Tote(BaseModel):
    id: Optional[str] = None  # typically generated by DB
    barcode: str
    description: str
    location: Optional[str] = None
    status: Optional[str] = Field(default="in-use", description="Status of the tote")
    tags: Optional[List[str]] = []  # list of tag names
    weight: Optional[float] = None
    qr_url: Optional[str] = None
    qr_image: Optional[str] = None  # base64 string or URL
    images: Optional[List[str]] = []  # list of image URLs or base64 strings
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ToteCreate(BaseModel):
    barcode: str
    description: str
    location: Optional[str] = None
    status: Optional[str] = "in-use"
    tags: Optional[List[str]] = []
    weight: Optional[float] = None
    images: Optional[List[str]] = []

class ToteUpdate(BaseModel):
    barcode: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[List[str]] = None
    weight: Optional[float] = None
    images: Optional[List[str]] = None

class TagCreate(BaseModel):
    name: str

class TagUpdate(BaseModel):
    name: str

"""
Pseudo database schema used for all SQL optimization exercises.

These dataclasses document the table structure referenced in queries.py.
No real database connection is required — treat them as the schema contract.

Schema overview
---------------

users
    id          INT         PK
    email       VARCHAR(255)
    name        VARCHAR(100)
    status      VARCHAR(20)   -- 'active' | 'inactive' | 'banned'
    created_at  TIMESTAMP

orders
    id          INT         PK
    user_id     INT         FK -> users.id
    total       DECIMAL(10,2)
    status      VARCHAR(20)   -- 'pending' | 'paid' | 'shipped' | 'cancelled'
    created_at  TIMESTAMP

order_items
    id          INT         PK
    order_id    INT         FK -> orders.id
    product_id  INT         FK -> products.id
    quantity    INT
    unit_price  DECIMAL(10,2)

products
    id          INT         PK
    name        VARCHAR(255)
    description TEXT
    category_id INT         FK -> categories.id
    price       DECIMAL(10,2)
    stock       INT

categories
    id          INT         PK
    name        VARCHAR(100)
    parent_id   INT         FK -> categories.id  (nullable, for sub-categories)

Indexes that currently exist (minimal, intentionally sparse)
------------------------------------------------------------
    users.id            (PK)
    orders.id           (PK)
    order_items.id      (PK)
    products.id         (PK)
    categories.id       (PK)
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class User:
    id: int
    email: str
    name: str
    status: str
    created_at: datetime


@dataclass
class Order:
    id: int
    user_id: int
    total: Decimal
    status: str
    created_at: datetime


@dataclass
class OrderItem:
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: Decimal


@dataclass
class Product:
    id: int
    name: str
    description: str
    category_id: int
    price: Decimal
    stock: int


@dataclass
class Category:
    id: int
    name: str
    parent_id: Optional[int]

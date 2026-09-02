from database.database_connection import Base
from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey


class Product(Base):
    __tablename__="products"

    product_id=Column(String(20),primary_key=True)

    product_name=Column(String(100),nullable=False)

    category=Column(String(100),nullable=False)

    price=Column(Float,nullable=False)



class Store(Base):
    __tablename__="stores"

    store_id=Column(String(20),primary_key=True)

    store_name=Column(String(100),nullable=False)

    city=Column(String(100),nullable=False)

    state=Column(String(50),nullable=False)



class Sale(Base):
    __tablename__="sales"

    sale_id   =Column(Integer,primary_key=True)

    product_id=Column(String(20),ForeignKey("products.product_id"),nullable=False)

    store_id=Column(String(20),ForeignKey("stores.store_id"),nullable=False)

    quantity=Column(Integer,nullable=False)

    price=Column(Float,nullable=False)

    total_amount=Column(Float,nullable=False)

    sale_type=Column(String(30))

    sale_date=Column(Date,nullable=False)


class Inventory(Base):
    __tablename__="inventories"

    inventory_id=Column(Integer,primary_key=True,autoincrement=True)

    product_id=Column(String(20),ForeignKey("products.product_id"))

    stock_quantity=Column(Integer,nullable=False)

    reorder_level=Column(Integer,nullable=False)

    stock_status=Column(String(30))
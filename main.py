from fastapi import FastAPI,Query,Path
from typing import Union,List,Set
from pydantic import BaseModel


class Item(BaseModel):
    """
        Item model
        name:商品名称
    """
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

object={
    "name": "李重楼",
    "description": "小数描述",
    "price": 12.23,
    "tax": 1.23
}

print(list(object))
print(dict(object))

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/item/{path_param}")
async def path_param(
    path_param:int= Path(title="The ID of the item to get",default=...),
    q: Union[str, None] = Query(default=None,min_length=3, max_length=5)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}],"path_param": path_param}
    if (q):
        results.update({"q": q})
    return results


@app.get("/items/")
async def query_param(is_required: bool, skip: int = 0, limit: int = 10):
    return {"list": fake_items_db[skip: skip + limit], "is_required": is_required}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    print(item_dict)
    return item

@app.patch("/item/{item_id}")
async def create_item(item_id:int,item: Item):
    return {"item_id": item_id, **item.dict()}

@app.get('/shop')
async def get_shopping_list():
    return {"message": "Hello World"}


class Image(BaseModel):
    url: str
    name: str

class Goods(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags:Set[str]=set(),
    place:List[str]=[],
    img: Union[List[Image], None] = None
    

@app.post('/shop/goods')
async def add_goods(goods:Goods):
    print(goods)
    return {"goods": goods}

@app.get('/shop/goods/images')
async def get_goods_images():
    return [
            {
                "name": "顶视图",
                "url": "top-img.png"
            },
            {
                "name": "侧视图",
                "url": "left-img.png"
            }
        ]
    
@app.get('/shop/goods/{goods_id}/images')
async def get_goods_images(goods_id:int):
    return {
            "goods_id":goods_id,
                "name": "顶视图",
                "url": "top-img.png"
            }


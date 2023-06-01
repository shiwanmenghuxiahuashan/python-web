from fastapi import FastAPI,Query,Path,Cookie,Header,Form, File, UploadFile
from typing import Union,List,Set
from pydantic import BaseModel


class Item(BaseModel):
    """
        Item model
        name:商品名称
    """
    item_id:str
    name: str=""
    description: Union[str, None] = None
    price: float=0.0
    tax: Union[float, None] = None


app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

# response_model_exclude_unset 会忽略默认值
@app.get("/item/{path_param}", response_model=Item, response_model_exclude_unset=True)
async def path_param(
    path_param:int= Path(title="The ID of the item to get",default=...),
    q: Union[str, None] = Query(default=None,min_length=0, max_length=1)
):
    items= [{"item_id": "Foo"}, {"item_id": "Bar"},{"item_id": "3"}]
    results = {**items[path_param],"path_param": path_param}
    if (q):
        results.update({"q": q})
    return results

# Header 参数 查询参数
@app.get("/items/")
async def query_param(
    is_required: bool,
    skip: int = 0,
    limit: int = 10,
    user_agent:Union[str,None]=Header(default=None)
    ):
    
    return {
        "user_agent":user_agent,
        "list": fake_items_db[skip: skip + limit], 
        "is_required": is_required
    }

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    print(item_dict)
    return item

# 响应模型 response_model 会限制返回值，item_id 会被忽略
@app.patch("/item/{item_id}",response_model=Item)
async def create_item(item_id:int,item: Item):
    return {"item_id": item_id, **item.dict()}



# -----------------------------------------------------------



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
    
@app.get('/shop')
async def get_shopping_list():
    return {"message": "Hello World"}

@app.post('/shop/goods')
async def add_goods(goods:Goods):
    print(goods)
    return {"goods": goods}

@app.get('/shop/goods/images')
async def get_goods_images(ads_id:Union[str,None]=Cookie(default=None)):
    return [
            {"ads_id":ads_id},
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


@app.post('/shop/login')
async def login(username: str = Form(), password: str = Form()):
    return {
            "username":username,
            "password": password,
            }

@app.post('/shop/files')
async def create_upload_file(file:UploadFile):
   return {"filename": file.filename}


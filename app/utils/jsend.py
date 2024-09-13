from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union, List, Any


class JSendResponse(JSONResponse):
    def _init_(self,
                 status: str,
                 data: Union[List[BaseModel], BaseModel, Any] = None,
                 message=None,
                 status_code: int = 200,  # Default HTTP status code
                 *args,
                 **kwargs):
        content = {
            "status": status,
            "message": message
        }

        if status_code != 204:  # Only include data if it's not a 204 No Content response
            encoded_data = jsonable_encoder(data)
            content["data"] = encoded_data

        super()._init_(content=content if status_code != 204 else None, status_code=status_code, *args, **kwargs)

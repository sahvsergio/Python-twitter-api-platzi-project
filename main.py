
# library imports 
#python
from uuid import UUUID#assigns a unique identifier
import datetime import date
from typing import Optional

#Pydantic

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#fastapi
from fastapi import FastAPI


app=FastAPI()

#Models
class UserBase(BaseModel): 
    user_id:UUID=Field(
        ...
        )   
    email:EmailStr=Field(
        ...
            )


class User(UserBase):
    user_id:UUID=Field(
        ...
        )   
    email:EmailStr=Field(
        ...
            )
    
    first_name:str=Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name:str=Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date:Optional[date]=Field(Default=None)
    
class UserLogin(UserBase):
    password:str=Field(
        ...,
        min_length=8)    
    
    
class Tweet(BaseModel):
    pass    


@app.get(
    path='/',)
def home():
    """
    Title:
    Description:
    Parameters:
    Returns:
    """
    return {"Twiter API":'Working'}


x

"""tweets
#create on the show

/ ->Show all tweets
/Post -> create a  tweet
create on my own

/tweets/{tweet-id}/->show  a specific  tweet
/tweets/{tweet-id}/delete a specific tweet
/tweets/{tweet-id}/update ->udpate a specific tweet


users
/Signup ->Register a user
/Login->Login a user
/users ->Show all users
/users/{user_id} ->s/show a specific user information
/users/{user_id}/delete ->delete a specific user account
/users/{user_id}/udpate ->update a specific  user account





"""

if __name__ == "__main__":
   import uvicorn
   uvicorn.run(app, host="localhost", port=8000)
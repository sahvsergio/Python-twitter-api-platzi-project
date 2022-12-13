
# library imports 
#python
from uuid import UUID #assigns a unique identifier
from datetime import date
from datetime import datetime
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
        min_length=8,
        max_length=64
        )    
    
    
class Tweet(BaseModel):
    tweet_id:UUID=Field(...)
    content:str=Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at:datetime= Field(default=datetime.now())
    updated_at:Optional[datetime]=Field(default=None)     


#esqueleto de las path operations

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

# library imports 
#python
from uuid import UUID #assigns a unique identifier
from datetime import date
from datetime import datetime
from typing import Optional,List #

#Pydantic

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#fastapi
from fastapi import FastAPI
from fastapi import status


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
    
class UserRegister(User):
    password: str = Field(
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

#Path Operations




## Users
### Registers a user
@app.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Registers a users',
    tags=['Users']
)
def signup():
    """
    Signup
    
    This path operation  registers a user in the app
    
    Parameters:
    -Request body Parameter
        user-UserRegister
        
    Returns a Json with the basic user information:
    user_id :UUID
    -email : Emailstr
    first_name:str
    last_name: str
    birth_date:str
    """


@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Logins a users',
    tags=['Users']
)
def login():
    pass



@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Shows all users',
    tags=['Users']
)
def shows_all_users   ():
    pass

@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Shows a single user',
    tags=['Users']
)
def show_a_user():
    pass


@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Deletes a user',
    tags=['Users']
)

def delete_a_user():
    pass


@app.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Updates a user',
    tags=['Users']
   )

def update_a_user():
    pass


## Tweets

###Show all tweets
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
    tags=['Tweets'])

def home():
    """
    Title:
    Description:
    Parameters:
    Returns:
    """
    
### Post a Tweet    
@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a tweet',
    tags=['Tweets']
)
def post():
    pass

### Show a Tweet
@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Shows a tweet',
    tags=['Tweets']
)    
def show_a_tweet():
    pass
    
###Delete a tweet    
@app.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a  tweet',
    tags=['Tweets']
)

def delete_a_tweett():
    pass
    
@app.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Updates a tweet tweet',
    tags=['Tweets']
)
def update_a_tweet():
        pass
"""tweets
#create on the show

/ ->Show all tweets
/Post -> create a  tweet
create on my own

/tweets/{tweet-id}/->show  a specific  tweet
/tweets/{tweet-id}/delete a specific tweet
/tweets/{tweet-id}/update ->udpate a specific tweet





"""

if __name__ == "__main__":
   import uvicorn
   uvicorn.run(app, host="localhost", port=8000)
   
   """- controllers
	- __init__.py
	- auth.py
	- tweet.py
	- user.py
-models
	- __init__.py
	- Tweet.py
	- User.py
-venv
.gitignore
main.py
README.md
requirements.py
"""



from typing import Union
from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import BaseModel

import os
from supabase import create_client, Client
import json

# 환경변수를 설정해요. 클라우드에 같이 올릴 수 없기 떄문에 로컬 환경에서 관리돼요.
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# 주어진 환경변수로 https://supabase.com에서 생성한 프로젝트를 초기화해요.
# 이미지 업로드, 디비 등 다양한 것들을 손쉽게 사용할 수 있어요.
supabase: Client = create_client(url, key)

# 백엔드 웹서버를 초기화해요. 저희가 만든 앱은 디자인이 예쁘고 액션이 많고 관리해야할 상태가 많아요.
# 여러모로 파이썬의 GUI로 구현할 수 없다고 판단했고 frontend를 react로, backend를 python + supabase + fastApi로 구성해요 

app = FastAPI()

# Health Check
@app.get("/")
def read_root():
    return {"Hello": "World"}


# 유저 목록이에요. 
# 타입이 없는 언어지만 Type Doc을 통해서 문서화, 타입을 강제화 하고 싶었는데 POC하다가 잘 안되서 포기했어요.
@app.get("/users")
def read_uesrs():
    response = supabase.table('users').select("*").execute()
    print(response)
    return response


# 강아지 목록이에요.
# 추후 유저가 많아지면 인증정보에서 해당 유저의 개만 가져오도록 필터가 필요해요. 
@app.get("/dogs")
def read_dogs():
    response = supabase.table('dogs').select("*").execute()
    print(response)
    return response

# 강아지 입력 Dto에요
# 이름은 필수고 경우에 따라 사진을 받을 수 있어요. 
# 원래 사진 업로드도 구현하려 했으나 FormData 자체를 업로드하는 과정에서 디코딩 에러가 나는데 못잡았어요.
# 프론트에서 직접 업로드 후 url을 전송해요. 
class DogInput(BaseModel):
    user_id: str
    name: str
    imageUrl: str | None

@app.post("/dogs")
def create_dog(dog: DogInput):
    dog_json = dog.model_dump_json()
    response = supabase.table('dogs').insert(json.dumps(dog_json))
    print(response)
    return response

# 똥 목록 get 요청이에요.

@app.get("/poops")
def read_poops():
    response = supabase.table('poops').select("*").execute()
    print(response)
    return response

# 똥 모델이에요.
# shape는 똥의 모양이에요. 0부터 5까지 있어요.
# color는 똥의 색깔이에요. 이 값은 추후 고도화 여지가 있어서 hex값을 그대로 받은 후 백엔드에서 색깔연산을 할 예정이에요. 
class PoopInput(BaseModel):
    dog_id: str
    shape: str
    color: str


# 똥 생성 요청이에요.

@app.post("/poops")
def create_poop(dog: PoopInput):
    dog_json = dog.model_dump_json()
    response = supabase.table('poops').insert(json.dumps(dog_json))
    print(response)
    return response

# 디자인 화면이랑 구현은 프로젝트 코드에 구현되어 있어요.
# 똥 목록 화면까지 구현 했고 이후 똥 생성과 한 주 요약을 구현하면 되는 상황이에요. 
# 미완성 부분 + post 요청을 날릴 때 프로덕션에 올린 백엔드 서버가 에러가 간헐적으로 발생해 시간 내 완성을 할 수 없다고 판단했어요.
# 초기 논의때 스펙을 너무 크게 잡아서 개발은 실제 돌아갈 수 있을 정도로는 완성하지 못했어요. 
# 그래서 임시로 해커톤처럼 UX,UI 플로우를 볼 수 있도록 구성했어요.


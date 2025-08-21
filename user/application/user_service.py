from user.domain.user import User
from user.domain.repository.user_repo import IUserRespository
from user.infra.repository.user_repo import UserRepository
from datetime import datetime
from ulid import ULID
from fastapi import HTTPException
from utils.crypto import Crypto

class UserService:
    def __init__(self):
        self.user_repo: IUserRespository = UserRepository() # 현재는 의존성 역전 원칙을 위배하고 있음
        self.ulid = ULID()
        self.crypto = Crypto()

    def create_user(self, name: str, email: str, password: str):
        _user = None

        try:
            _user = self.user_repo.find_by_email(email)
        except HTTPException as e:
            if e.status_code == 422:
                raise e

        if _user:
            raise HTTPException(status_code=422)
        
        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=self.crypto.encrypt(password),
            created_at=now,
            updated_at=now
        )
        self.user_repo.save(user)
        return user
        
        
        
        
        
        
        
        
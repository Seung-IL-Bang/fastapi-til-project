from datetime import datetime
from ulid import ULID
from fastapi import HTTPException
from utils.crypto import Crypto

from user.domain.user import User
from user.domain.repository.user_repo import IUserRespository

class UserService:
    
    def __init__(
        self, 
        user_repo: IUserRespository # Container에서 주입받음
    ):
        self.user_repo = user_repo
        self.ulid = ULID()
        self.crypto = Crypto()

    def create_user(
        self, 
        name: str, 
        email: str, 
        password: str,
        memo: str | None = None
    ):
        # 이메일 중복 체크
        if self.user_repo.exists_by_email(email):
            raise HTTPException(status_code=422, detail="Email already exists")
        
        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=self.crypto.encrypt(password),
            memo=memo,
            created_at=now,
            updated_at=now
        )
        self.user_repo.save(user)
        return user
        
    def update_user(
        self,
        user_id: str,
        name: str | None = None,
        password: str | None = None
    ):
        user = self.user_repo.find_by_id(user_id)

        if name:
            user.name = name
        if password:
            user.password = self.crypto.encrypt(password)
        user.updated_at = datetime.now()

        self.user_repo.update(user)

        return user
        
    def get_users(
        self,
        page: int,
        size: int
    ):
        total_count, users = self.user_repo.get_users(page, size)
        return total_count, users
        
        
        
        
        
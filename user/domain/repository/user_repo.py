from abc import ABCMeta, abstractmethod
from user.domain.user import User

class IUserRespository(metaclass=ABCMeta):

    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_email(self, email: str) -> User:
        """
        이메일로 유저를 조회한다.
        조회한 유저가 없을 경우 422 에러를 발생시킨다.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, user_id: str) -> User:
        """
        유저 아이디로 유저를 조회한다.
        조회한 유저가 없을 경우 422 에러를 발생시킨다.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        """
        이메일로 유저 존재 여부를 확인한다.
        """
        raise NotImplementedError

    @abstractmethod
    def get_users(self, page: int, size: int) -> tuple[int, list[User]]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: str):
        raise NotImplementedError
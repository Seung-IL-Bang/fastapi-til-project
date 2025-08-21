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
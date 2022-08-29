# 상수를 넣는 공간 (어떤 환경에도 변경되지 않는 것)
from dataclasses import dataclass, asdict
from os import path, environ

# 파일 위치를 기준으로 프로젝트를 가리키고 있음
# config 파일 위치가 바뀐다면 base_dir도 변경되어야함
base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 Configuration
    dictionary 형태로 unpacking 하기 쉬움
    asdict(LocalConfig()) -> 클래스를 Dict로 변환
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


# 로컬 서버
@dataclass
class LocalConfig(Config):  # 상속관계
    PROJ_RELOAD: bool = True


# 운영 서버
@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    """
    환경 불러오기 (환경변수 이름인 API_ENV 를 보고 환경을 정의)
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))

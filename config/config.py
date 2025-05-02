import logging
import logging.config
from dataclasses import dataclass
from environs import Env

@dataclass
class Date:
    format_wb: str
    format_tg: str
    tz: str

@dataclass
class TgBot:
    webhook_url: str
    token: str
    username_admins: list[str]
    max_size_input_file: int
    free_period_days: int

@dataclass
class DB:
    host: str
    port: int
    database: str
    user: str
    password: str

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

@dataclass
class GoogleSpreadSheets:
    cred_file_path: str
    ss_id: str 
    
@dataclass
class Storage:
    use_redis: bool
    redis_host: str
    redis_port: int
    
@dataclass
class TBank:
    terminal: str
    password: str
    url_success_payment: str

@dataclass
class Config:
    domain: str
    debug: bool
    key: str
    sentry_dsn: str
    tg_bot: TgBot
    date: Date
    gs: GoogleSpreadSheets
    db: DB
    storage: Storage
    tbank: TBank
    

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        debug=True if env('DEBUG') == "True" else False,
        domain=env("DOMAIN"),
        key=env("ENCRYPTION_KEY"),
        sentry_dsn=env("SENTRY_DSN"),
        tg_bot=TgBot(
            webhook_url=env("DOMAIN")+"/webhook",
            token=env('TGBOT_TOKEN'),
            username_admins=env("USERNAME_ADMINS"),
            max_size_input_file=int(env("MAX_SIZE_BYTES")),
            free_period_days=int(env("FREE_PERIOD_DAYS"))
        ),
        date=Date(
            format_wb=env("DATE_FORMAT_WB"),
            format_tg=env("DATE_FORMAT_TG"),
            tz=env("TZ"),
        ),
        db=DB(
            host=env('DB_HOST'),
            port=env('DB_PORT'),
            database=env('DB_NAME'),
            user=env('DB_USER'),
            password=env('DB_PASS'),
        ),
        gs=GoogleSpreadSheets(
            cred_file_path=env("CREDENTIALS_FILE_PATH"),
            ss_id=env("SPREADSHEET_ID")
        ),
        storage=Storage(
            use_redis=True if env("USE_REDIS") == "True" else False,
            redis_host=env("REDIS_HOST"),
            redis_port=env("REDIS_PORT")
        ),
        tbank=TBank(
            terminal=env("TBANK_TERMINAL"),
            password=env("TBANK_PASSWORD"),
            url_success_payment=env("TBANK_SUCCESS_PAYMENT")
        )
    )

settings = load_config()

# Определяем конфигурацию логирования
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': logging.DEBUG,
            'stream': 'ext://sys.stdout',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': logging.DEBUG,
    },
}


logging.config.dictConfig(LOGGING_CONFIG)


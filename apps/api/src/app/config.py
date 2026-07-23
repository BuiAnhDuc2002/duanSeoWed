from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    database_url: str = "sqlite:///./app.sqlite3"
    wordpress_allow_auto_publish: bool = False
    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_service_role_key: str = ""
    r2_account_id: str = ""
    r2_access_key_id: str = ""
    r2_secret_access_key: str = ""
    r2_bucket_private: str = "ai-seo-private"
    r2_presigned_url_ttl_seconds: int = 900
    r2_max_image_bytes: int = 25 * 1024 * 1024
    r2_max_audio_bytes: int = 100 * 1024 * 1024
    r2_max_video_bytes: int = 1024 * 1024 * 1024


settings = Settings()

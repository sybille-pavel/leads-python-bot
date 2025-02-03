from pydantic_settings import BaseSettings, SettingsConfigDict


class GoogleSheetsSetting(BaseSettings):
    credentials_json: str
    spreadsheet_id: str
    sheet_name: str

    model_config = SettingsConfigDict(env_file='.env', env_prefix='GOOGLE_SHEETS_', extra='allow')


google_sheets_setting = GoogleSheetsSetting()

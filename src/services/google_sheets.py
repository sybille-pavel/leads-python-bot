import gspread
from oauth2client.service_account import ServiceAccountCredentials
from core.logger import logger

class GoogleSheetsClient:
    def __init__(self, credentials_json, spreadsheet_id, sheet_name):
        # Указываем области доступа
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

        # Загружаем учетные данные
        self.credentials_json = credentials_json
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name

        # Авторизация через сервисный аккаунт
        self.client = self.authenticate_google_sheets()

    def authenticate_google_sheets(self):
        """Авторизация с использованием сервисного аккаунта и ключа"""
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_json, self.scope)
        client = gspread.authorize(creds)
        return client

    def get_worksheet(self):
        """Получаем доступ к таблице и листу"""
        sheet = self.client.open_by_key(self.spreadsheet_id)
        worksheet = sheet.worksheet(self.sheet_name)
        return worksheet

    def append_data(self, name: str, contact: str, product: str, time: str):
        """Добавление строки в таблицу с именованными параметрами"""
        try:
            worksheet = self.get_worksheet()
            row = [name, contact, product, time]
            worksheet.append_row(row)
        except Exception as e:
            logger.warning('Ошибка при добавлении данных в таблицу')
            logger.warning(e)

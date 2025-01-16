# management/commands/import_excel.py
import pandas as pd
from django.core.management.base import BaseCommand
from user import models as users
import uuid
class Command(BaseCommand):
    help = "Excel faylidan ma'lumotlarni yuklash"

    def handle(self, *args, **kwargs):
        file_path = "avazbek.xlsx"  # Excel faylingizning yo'li
        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
                    users.User.objects.create(
                        username=str(uuid.uuid4()),
                        password=(row[2]), 
                        login_provider=row.get(2, None),  
                        full_name=row.get(1, None),
                        phone_number=row.get(2, None),
                    )

        self.stdout.write(self.style.SUCCESS("Ma'lumotlar muvaffaqiyatli yuklandi!"))

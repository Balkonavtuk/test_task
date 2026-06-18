from django.core.management.base import BaseCommand
from django.utils import timezone
from payments.models import Client, Payment
from datetime import datetime

class Command(BaseCommand):
    help = 'Загружает тестовые данные (клиенты и платежи)'

    def handle(self, *args, **options):

        # Создаём клиентов
        clients_data = [
            {'id': 1, 'first_name': 'Ivan', 'last_name': 'Ivanov', 'country': 'Russia'},
            {'id': 2, 'first_name': 'Alexey', 'last_name': 'Smirnov', 'country': 'Russia'},
            {'id': 3, 'first_name': 'Sergey', 'last_name': 'Sidorov', 'country': 'USA'},
            {'id': 4, 'first_name': 'Dmitry', 'last_name': 'Petrov', 'country': 'USA'},
            {'id': 5, 'first_name': 'Oleg', 'last_name': 'Kolovin', 'country': 'Germany'},
        ]

        for client in clients_data:
            Client.objects.get_or_create(
                id=client['id'],
                defaults={
                    'first_name': client['first_name'],
                    'last_name': client['last_name'],
                    'country': client['country']
                }
            )
            self.stdout.write(f"Клиент {client['first_name']} {client['last_name']} создан/обновлён")

        # Создаём платежи
        payments_data = [
            {'id': 1, 'payer_id': 5, 'amount': 100.00, 'percent': 13, 'pay_date': '2018-08-11 10:37:50+03'},
            {'id': 2, 'payer_id': 2, 'amount': 130.53, 'percent': 18, 'pay_date': '2018-08-15 15:32:43+03'},
            {'id': 3, 'payer_id': 4, 'amount': 55.11, 'percent': 13, 'pay_date': '2018-09-01 09:30:35+03'},
            {'id': 4, 'payer_id': 1, 'amount': 67.27, 'percent': 13, 'pay_date': '2018-09-04 19:25:11+03'},
            {'id': 5, 'payer_id': 3, 'amount': 143.74, 'percent': 22, 'pay_date': '2018-09-11 11:32:59+03'},
        ]

        for payment in payments_data:
            dt = datetime.fromisoformat(payment['pay_date'])
            if dt.tzinfo is None:
                dt = timezone.make_aware(dt, timezone.get_default_timezone())
            else:
                dt = dt.astimezone(timezone.UTC)

            Payment.objects.get_or_create(
                id=payment['id'],
                defaults={
                    'payer_id': payment['payer_id'],
                    'amount': payment['amount'],
                    'percent': payment['percent'],
                    'pay_date': dt
                }
            )
            self.stdout.write(f"Платёж {payment['id']} создан/обновлён")

        self.stdout.write(self.style.SUCCESS('Все данные успешно загружены!'))
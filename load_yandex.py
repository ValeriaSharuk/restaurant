from django_cron import CronJobBase, Schedule
from django.core.management import call_command
import yadisk
import datetime


class GoCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24  # каждые 24 часа
    RUN_AT_TIMES = ['12:00']  # В 12 часов
    schedule = Schedule(run_at_times=RUN_AT_TIMES, run_every_mins=RUN_EVERY_MINS)  # Задaть график работы автоматической выгрузки
    code = "main.GoCronJob"

    def do(self):
        call_command('pg_dump —dbname = "postgres" —file =”cronBD.sql” —username = "postgres" –-password = "Ebaty1620", —host = "localhost" —port = ""')

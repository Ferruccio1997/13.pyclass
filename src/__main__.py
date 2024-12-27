import schedule
import time
from lib.classes.CsvSource import CsvSource
from lib.classes.JsonSource import JsonSource
from lib.classes.TxtSource import TxtSource


# Funcao para verificar novos arquivos
def check_for_new_files():
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()
    json_source.check_for_new_files()

# Agenda a execução da funcao check_for_new_files() a cada segundo
schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSource()
txt_source = TxtSource()
json_source = JsonSource()

# Executa o loop principal
while True:
    schedule.run_pending()
    time.sleep(1)
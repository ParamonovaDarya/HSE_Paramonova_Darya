
Задание 1 (парсинг)
Напишите скрипт, который будет производить сбор данных с выбранной вами
страницы на сайте ЦБ РФ либо осуществлять загрузку xsl, xslx, pdf, csv или иного
файла с данными в рабочую директорию с последующим его парсингом.
У класса должен быть только один публичный метод start(). Все остальные методы,
содержащие логику по выгрузке и сохранению данных, должны быть приватными.
Определите структуру для хранения. Для ключевой ставки ЦБ РФ это может быть
словарь (dict), где ключом будет выступать дата, а значением — размер ключевой
ставки на указанную дату.
Оберните весь написанный код парсера в класс ParserCBRF.

import requests
from bs4 import BeautifulSoup
import zipfile
import io
import csv

class ParserCBRF:

    def __init__(self):
        self.soup = None
        self.csv_file_name = "cbr_data.csv"

    def __getdata__(self):
        url = "https://cbr.ru/ec_research/vserossiyskoe-obsledovanie-domokhozyaystv-po-potrebitel-skim-finansam/"
        r = requests.get(url)
        r.raise_for_status()
        self.soup = BeautifulSoup(r.text, 'html.parser')

    def __householddataExtractor__(self):
        file = self.soup.find(id="a_145697file").get('href')
        response = requests.get(f"https://cbr.ru{file}")
        with zipfile.ZipFile(io.BytesIO(response.content)) as myzip:
            myzip.extract("5th_wave_hh_230323.csv", self.csv_file_name)

    def __csvUnderTheHudWork__(self, searchkey, searchterm):
        counter = 0
        householdFilecsv = open(self.csv_file_name, "r", encoding="cp1251", newline="")
        householdDictreder = csv.DictReader(householdFilecsv)
        for row in householdDictreder:
            if row[searchkey] == searchterm:
                counter += 1
        print(counter)
        householdFilecsv.close()

    def __main__(self, searchkey, searchterm):
        self.__getdata__()
        self.__householddataExtractor__()
        self.__csvUnderTheHudWork__(searchkey, searchterm)

    def start(self, searchkey, searchterm):
        self.__main__(searchkey, searchterm)

nice = ParserCBRF()
nice.start("psu", "Ленинградская область")
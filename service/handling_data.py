from io import BytesIO
import re
import asyncio
import io
from itertools import zip_longest
from openpyxl import load_workbook, Workbook
from openpyxl.utils.exceptions import InvalidFileException
from openpyxl.styles import PatternFill

class InputDataHandler:
    
    @classmethod
    def _handle_A_value(cls, value):
        if value:
            value = str(value).strip().lower()
        else: 
            value = None

        return value
    
    @classmethod
    def _handle_B_value(cls, value):
        if isinstance(value, int) or isinstance(value, float):
            if value >= 0:
                return value 
            elif value < 0:
                return None
        elif value:
            value = re.search(r'\d+', value)
            if value:
                value = int(value.group())
            else:
                value = None
        else: 
            value = None
    
        return value
    
    @classmethod
    def _handle_С_value(cls, value):
        return value
    
    @classmethod
    async def validate(cls, file_buffer: BytesIO) -> list:
        try:
            workbook = load_workbook(filename=file_buffer)
        except:
            return "cant_read"
        sheet = workbook.active
        rows = sheet.iter_rows(min_row=2, max_col=3, values_only=True)
        flag = False
        for index, row in enumerate(rows, start=2):  # Начинаем с 2, чтобы индексация совпадала с Excel
            sheet.cell(row=index, column=1).fill = PatternFill(fill_type=None)
            sheet.cell(row=index, column=2).fill = PatternFill(fill_type=None)
            sheet.cell(row=index, column=3).fill = PatternFill(fill_type=None)
            if row[0] is None and row[1] is None and row[2] is None:
                continue
            
            if row[0] is None or not isinstance(row[1], (int, float)):
                red_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")

                if row[0] is None:
                    sheet.cell(row=index, column=1).fill = red_fill  # Исправлен индекс столбца
                    sheet.cell(row=index, column=1).value = "отсутствует артикул"
                    flag = True

                if row[1] is None:
                    sheet.cell(row=index, column=2).fill = red_fill  # Исправлен индекс столбца
                    sheet.cell(row=index, column=2).value = "!!!!" + "отсутствует стоимость"
                    flag = True
                elif not isinstance(row[1], (int, float)):
                    sheet.cell(row=index, column=2).fill = red_fill  # Исправлен индекс столбца
                    value = sheet.cell(row=index, column=2).value or ""
                    sheet.cell(row=index, column=2).value = "!!!!" + str(value) 
                    flag = True

        if flag:
            buffer = BytesIO()
            workbook.save(buffer)
            workbook.close()
            buffer.seek(0)
            return buffer
        
        workbook.close()
        return "no_errors"
    
    @classmethod
    async def beutify_input(cls, file_buffer: BytesIO) -> dict:
        workbook = load_workbook(filename=file_buffer)
        sheet = workbook.active
        columns_a, columns_b, columns_c = [], [], []
        values = sheet.iter_rows(values_only=True)
        for v in values:
            if len(v) > 2: 
                columns_a.append(cls._handle_A_value(v[0]))
                columns_b.append(cls._handle_B_value(v[1]))
                columns_c.append(cls._handle_С_value(v[2]))
            elif len(v) > 1:
                columns_a.append(cls._handle_A_value(v[0]))
                columns_b.append(cls._handle_B_value(v[1]))
                columns_c.append(None)
            elif len(v) > 0:
                columns_a.append(cls._handle_A_value(v[0]))
                columns_b.append(None)
                columns_c.append(None)
            else:
                columns_a.append(None)
                columns_b.append(None)
                columns_c.append(None)

        stacked = []
        for a, b, c in list(zip_longest(columns_a, columns_b, columns_c)):
            if a and b:
                stacked.append({"article": a, "value": b, "supplier": c})
                
        return stacked
    
    @classmethod
    def beutify_input_test(cls, file_buffer: BytesIO) -> dict:
        workbook = load_workbook(filename=file_buffer)
        sheet = workbook.active
        columns_a, columns_b, columns_c = [], [], []
        values = sheet.iter_rows(values_only=True)
        for v in values:
            if len(v) > 2: 
                columns_a.append(cls._handle_A_value(v[0]))
                columns_b.append(cls._handle_B_value(v[1]))
                columns_c.append(cls._handle_С_value(v[2]))
            elif len(v) > 1:
                columns_a.append(cls._handle_A_value(v[0]))
                columns_b.append(cls._handle_B_value(v[1]))
                columns_c.append(None)
            elif len(v) > 0:
                columns_a.append(cls._handle_A_value(v[0]))
                columns_b.append(None)
                columns_c.append(None)
            else:
                columns_a.append(None)
                columns_b.append(None)
                columns_c.append(None)

        stacked = []
        for a, b, c in list(zip_longest(columns_a, columns_b, columns_c)):
            if a and b:
                stacked.append({"article": a, "value": b, "supplier": c})
                
        return stacked
    
    @classmethod
    async def create_xlsx(cls, missed_articles: list):
        workbook = Workbook()
        sheet = workbook.active
        for i, v in enumerate(missed_articles, start=1):
            sheet[f"A{i}"] = v
            
        excel_file_output = io.BytesIO()
        workbook.save(excel_file_output)
        excel_file_output.seek(0)
        return excel_file_output
    
    @classmethod
    async def add_missed_article(cls, uploaded_file: BytesIO, articles: list[int]):
        workbook = load_workbook(uploaded_file)
        sheet = workbook.active
        # вставить пустые строки
        for i in range(len(articles)):
            sheet.insert_rows(2)
        
        # нужно добавить в конец файла артикулы, а потом провалидировать, чтобы подсветить
        # перед валидацией убрать все раскрашенные ячейки
        for i in range(2, len(articles) + 2):
            sheet[f"A{i}"] = articles[i-2]
            
        excel_file_output = io.BytesIO()
        workbook.save(excel_file_output)
        excel_file_output.seek(0)
        return excel_file_output
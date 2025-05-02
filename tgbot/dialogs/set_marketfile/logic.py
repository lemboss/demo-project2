from .states import SetMarketfileSG
from ..show_report.states import ShowReportSG
from ..show_capitalization.states import ShowCapitalizatonSG
from tgbot.logic import Scenario
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram.types import Message, BufferedInputFile
from service.user_data import UserData
from ..show_report.logic import report_logic as report_logic_detalization
from ..show_capitalization.logic import report_logic as report_logic_capitalization
from io import BytesIO

class BaseMarketfileHandler:
    def __init__(self):
        self.file = None
        self.state = None
        
    async def set_state(self, state):
        self.state = state
        
    async def set_file(self, file: BytesIO = None, filename: str = None):
        self.file = file
        self.filename = filename
            
    async def clean_old(self, dialog_manager: DialogManager):
        await Scenario.clean_messages(dialog_manager)
        
    async def send_file(self, message: Message, dialog_manager: DialogManager):
        sd = dialog_manager.start_data
        doc = BufferedInputFile(self.file.read(), self.filename)
        msg = await message.answer_document(document=doc)
        sd["msgs_to_delete"].append(msg.message_id)
        
    async def to_scene(self, dialog_manager: DialogManager):
        await dialog_manager.start(self.state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)        
    
class MarketfileMain(BaseMarketfileHandler):
    def __init__(self):
        self.state = SetMarketfileSG.file
        
    async def set_file(self):
        self.file = await UserData.get_example_file()
        self.filename = "Шаблон таблицы.xlsx"
   
class MarketfileOverflow(BaseMarketfileHandler):
    def __init__(self):
        self.state = SetMarketfileSG.overflow_file
    
    async def set_file(self):
        self.file = await UserData.get_example_file()
        self.filename = "Шаблон таблицы.xlsx"    
    
class MarketfileIncorrectExtencion(BaseMarketfileHandler):
    def __init__(self):
        self.state = SetMarketfileSG.incorrect_file_extencion
        
    async def set_file(self):
        self.file = await UserData.get_example_file()
        self.filename = "Шаблон таблицы.xlsx"
        
class MarketfileIncorrectRows(BaseMarketfileHandler):
    def __init__(self):
        self.state = SetMarketfileSG.incorrect_file_rows
        
    async def set_file(self, file: BytesIO = None, filename: str = None):
        if file is not None and filename is not None:
            self.file = file
            self.filename = filename
            
class MarketfileSuccess(BaseMarketfileHandler):
    def __init__(self):
        self.state = SetMarketfileSG.success
        
    async def send_file(self, message: Message, dialog_manager: DialogManager):
        return
    
class MarketfileToShowReport(BaseMarketfileHandler):
    def __init__(self, message: Message):
        self.state = ShowReportSG.standart
        self.message = message
        
    async def send_file(self, message: Message, dialog_manager: DialogManager):
        return
    
    async def to_scene(self, dialog_manager):
        return await report_logic_detalization(self.message, dialog_manager)
    
class MarketfileToShowCapitalization(BaseMarketfileHandler):
    def __init__(self, message: Message):
        self.state = ShowCapitalizatonSG.report
        self.message = message
        
    async def send_file(self, message: Message, dialog_manager: DialogManager):
        return
    
    async def to_scene(self, dialog_manager):
        return await report_logic_capitalization(self.message, dialog_manager)
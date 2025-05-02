from tgbot.dialogs.get_reports.states import GetReportsSG
from tgbot.dialogs.menu.states import MainMenuSG
from tgbot.dialogs.set_expences.states import SetExpencesSG
from tgbot.dialogs.set_marketfile.states import SetMarketfileSG
from tgbot.dialogs.set_token.states import SetTokenSG
from tgbot.dialogs.show_report.states import ShowReportSG
from tgbot.dialogs.update_data.states import UpdateDataSG
from tgbot.dialogs.show_capitalization.states import ShowCapitalizatonSG
from tgbot.dialogs.payments.states import PaymentsSG
from aiogram.fsm.state import State
from .enum import Step

class StepsMoving:
    def __init__(self, state: State):
        self.state = state
        
    def get_equal(self) -> str:
        match self.state:
            case MainMenuSG.menu:
                return Step.MENU.value
            case ShowReportSG.select_dates:
                return Step.SELECT_DATES_REPORT.value
            case GetReportsSG.menu:
                return Step.REPORTS_MENU.value
            case SetExpencesSG.menu:
                return Step.SET_EXPENCES_MENU.value
            case SetExpencesSG.set_stable:
                return Step.SET_EXPENCES_STABLE.value
            case SetExpencesSG.set_variable:
                return Step.SET_EXPENCES_VARIABLE.value
            case SetExpencesSG.pre_report:
                return Step.SET_EXPENCES_PRE_REPORT.value
            case SetMarketfileSG.file:
                return Step.SET_FILE.value
            case SetMarketfileSG.overflow_file:
                return Step.SET_FILE_OVERFLOW.value
            case SetMarketfileSG.incorrect_file_extencion:
                return Step.SET_FILE_INCORRECT_EXTENCION.value
            case SetMarketfileSG.incorrect_file_rows:
                return Step.SET_FILE_INCORRECT_ROWS.value
            case SetMarketfileSG.missed_articles:
                return Step.SET_FILE_MISSED_ARTICLES.value
            case SetMarketfileSG.success:
                return Step.SET_FILE_SUCCESS_MENU.value
            case SetTokenSG.set_token:
                return Step.SET_TOKEN.value
            case SetTokenSG.step1:
                return Step.SET_TOKEN_INSTRUCTION_STEP1.value
            case SetTokenSG.step2:
                return Step.SET_TOKEN_INSTRUCTION_STEP2.value
            case SetTokenSG.step3:
                return Step.SET_TOKEN_INSTRUCTION_STEP3.value
            case SetTokenSG.step4:
                return Step.SET_TOKEN_INSTRUCTION_STEP4.value
            case SetTokenSG.success:
                return Step.SET_TOKEN_SUCCESS_MENU.value
            case ShowReportSG.standart:
                return Step.STANDART_REPORT.value
            case ShowReportSG.deep:
                return Step.DEEP_REPORT.value
            case ShowReportSG.missed_supplier:
                return Step.MISSED_SUPPLIER_REPORT.value
            case UpdateDataSG.menu:
                return Step.MENU.value
            case PaymentsSG.create:
                return Step.PAYMENT_CREATE.value
            case PaymentsSG.success:
                return Step.PAYMENT_SUCCESS.value
            case PaymentsSG.fail:
                return Step.PAYMENT_FAIL.value

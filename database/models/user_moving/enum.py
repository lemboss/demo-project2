from enum import Enum

class Step(Enum):
    MENU = "menu"
    
    UPDATE_DATA_MENU = "update_data_menu"
    SET_TOKEN = "set_token"
    SET_TOKEN_INSTRUCTION_STEP1 = "set_token_instruction_step1"
    SET_TOKEN_INSTRUCTION_STEP2 = "set_token_instruction_step2"
    SET_TOKEN_INSTRUCTION_STEP3 = "set_token_instruction_step3"
    SET_TOKEN_INSTRUCTION_STEP4 = "set_token_instruction_step4"
    SET_TOKEN_SUCCESS_MENU = "set_token_success_menu"
    
    SET_FILE = "set_file"
    SET_FILE_OVERFLOW = "set_file_overflow"
    SET_FILE_INCORRECT_EXTENCION = "set_file_incorrect_extencion"
    SET_FILE_INCORRECT_ROWS = "set_file_incorrect_rows"
    SET_FILE_MISSED_ARTICLES = "set_file_missed_articles"
    SET_FILE_SUCCESS_MENU = "set_file_success_menu"
    
    SET_EXPENCES_MENU = "set_expences_menu"
    SET_EXPENCES_VARIABLE = "set_expences_variable"
    SET_EXPENCES_STABLE = "set_expences_stable"
    SET_EXPENCES_CONFIRM = "set_expences_confirm"
    SET_EXPENCES_PRE_REPORT = "set_expences_pre_report"
    
    REPORTS_MENU = "reports_menu"
    
    SELECT_DATES_REPORT = "select_dates_calendat"
    SHOW_CAPITALIZATION = "capitalization"
    
    STANDART_REPORT = "standart_report"
    DEEP_REPORT = "deep_report"
    MISSED_SUPPLIER_REPORT = "missed_supplier_report"
    
    PAYMENT_CREATE = "payment_create"
    PAYMENT_SUCCESS = "payment_success"
    PAYMENT_FAIL = "payment_fail"

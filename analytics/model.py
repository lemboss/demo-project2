from datetime import date
from dataclasses import dataclass, asdict

@dataclass
class SpreadSheetRow:
    date_: date
    new_users: int
    active_users: int
    blocked_users: int
    scenario_menu: int
    scenario_menu_uniqie: int
    scenario_set_token: int
    scenario_set_token_uniqie: int
    scenario_set_file: int
    scenario_set_file_uniqie: int
    scenario_choose_week: int
    scenario_choose_week_uniqie: int
    scenario_standart_report: int
    scenario_standart_report_uniqie: int
    scenario_deep_report: int
    scenario_deep_report_uniqie: int
    scenario_missed_supplier_report: int
    scenario_missed_supplier_report_uniqie: int
    scenario_payment_create: int
    scenario_payment_success: int
    scenario_payment_fail: int

    def asdict(self):
        return asdict(self)
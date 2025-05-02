class MediaPath:
    path_media = "tgbot/media/"
    path_storage = "tgbot/storage/"
    class Images:
        def __init__(self):
            self.main = MediaPath.path_media + "image_main.png"
            self.main_after = MediaPath.path_media + "image_main_after.png"
            self.set_token = MediaPath.path_media + "image_set_token.png"
            self.example_file = MediaPath.path_media + "image_example_file.jpg"
            self.wait = MediaPath.path_media + "animation_wait_report.gif"
            self.report = MediaPath.path_media + "image_report.png"
            self.capitaliztion = MediaPath.path_media + "image_capitalization.png"
            self.choose_week = MediaPath.path_media + "image_choose_week.png"
            self.select_next = MediaPath.path_media + "image_select_next.png"
            self.w_suppliers = MediaPath.path_media + "image_suppliers.png"
            self.wo_suppliers = MediaPath.path_media + "image_w-out_suplliers.png"
            self.set_stable_expence = MediaPath.path_media + "image_set_stable_expence.png"
            self.update_data = MediaPath.path_media + "image_update_data.png"
            self.success_token = MediaPath.path_media + "image_success_token.png"
            self.success_marketfile = MediaPath.path_media + "image_success_marketfile.png"
            self.expences_menu = MediaPath.path_media + "image_expences.png"
            self.stable_expences = MediaPath.path_media + "image_set_stable_expence.png"
            self.variable_expences = MediaPath.path_media + "image_variable_expences.png"
            self.pre_report_expence = MediaPath.path_media + 'image_set_pre_report_expence.png'
            self.get_reports_menu = MediaPath.path_media + 'image_get_reports_menu.png'
            self.wait_data_wb = MediaPath.path_media + 'image_wait_data_wb.png'
            self.payment_manage = MediaPath.path_media + "image_manage_payment.png"
            self.payment_success = MediaPath.path_media + "image_payment_success.png"
            self.payment_fail = MediaPath.path_media + "image_payment_fail.png"
            
            self.temp_pre_report_expence = MediaPath.path_storage + "pre_report_expence_{chat_id}_{timestamp}.png"
            self.temp_report = MediaPath.path_storage + "report_{chat_id}_{timestamp}.png"
            self.temp_capitaliaztion = MediaPath.path_storage + "capitalization_{chat_id}_{timestamp}.png"
            self.temp_w_suppliers = MediaPath.path_storage + "w_suppliers_{chat_id}_{timestamp}.png"
            self.temp_wo_suppliers = MediaPath.path_storage + "wo_suppliers_{chat_id}_{timestamp}.png"
            
            self.instruction_step1 = MediaPath.path_media + "step1.png"
            self.instruction_step2 = MediaPath.path_media + "step2.png"
            self.instruction_step3 = MediaPath.path_media + "step3.png"
            self.instruction_step4 = MediaPath.path_media + "step4.png"
            
    class Video:
        def __init__(self):
            self.preview = MediaPath.path_media + "preview.mp4"
            
    class Docs:
        def __init__(self):
            self.example = MediaPath.path_media + "шаблон.xlsx"
            
    class Fonts:
        def __init__(self):
            self.montserrat = MediaPath.path_media + "montserrat.ttf"
            self.montserrat_semibold = MediaPath.path_media + "montserrat_semibold.ttf"
            self.montserrat_bold = MediaPath.path_media + "montserrat_bold.ttf"
            
    def __init__(self):
        self.image = MediaPath.Images()
        self.doc = MediaPath.Docs()
        self.font = MediaPath.Fonts()
        self.video = MediaPath.Video()
        
path = MediaPath()

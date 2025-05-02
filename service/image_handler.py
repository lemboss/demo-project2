from PIL import Image, ImageDraw, ImageFont
from tgbot.media.path import path
from io import BytesIO

class PutText:
    
    def __init__(self):
        self.image_report = Image.open(path.image.report)
        self.image_stable_expence = Image.open(path.image.pre_report_expence)
        self.image_suppliers = Image.open(path.image.w_suppliers)
        self.image_wo_suppliers = Image.open(path.image.wo_suppliers)
        self.image_capitalization = Image.open(path.image.capitaliztion)
        
        montserrat_semibold_path = path.font.montserrat_semibold
        montserrat_bold_path = path.font.montserrat_bold
        font_size_params = 36
        font_size_week = 52
        self.montserrat_semibold_params = ImageFont.truetype(montserrat_semibold_path, font_size_params)
        self.montserrat_semibold_week = ImageFont.truetype(montserrat_semibold_path, font_size_week)
        self.montserrat_bold_params = ImageFont.truetype(montserrat_bold_path, font_size_params) 
        self.montserrat_bold_week = ImageFont.truetype(montserrat_bold_path, font_size_week)
  
        self.color = (255, 255, 255)
        self.pos_week = (230, 140)
        
    def get_font(self, font_path, font_size):
        return ImageFont.truetype(font_path, font_size)
        
    def draw_text(self, text: str, pos: tuple[int, int], font: ImageFont, draw: ImageDraw):
        draw.text(pos, text, fill=self.color, font=font)     
        
    def image_to_bytes(self, image):
        image_bytes = BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes.seek(0)
        
        return image_bytes
        
    def handle_report(self,
                      week: str,
                      sum_retail_amount: int,
                      sum_wb: int, 
                      sum_input: int, 
                      tax: int,
                      stable_expence_distrib: int,
                      variable_expence:int,
                      income: int,
                      net_income: int,
                      rent: int,
                      x_px = 550,
                      y_px = 125,
                      interval = 59
        ) -> BytesIO:
        image = self.image_report.copy()
        draw = ImageDraw.Draw(image)
        
        font_week = self.montserrat_bold_week
        font_params = self.montserrat_semibold_params
        pos_week = (490, 45)
        self.draw_text(week, pos_week, font_params, draw)
        self.draw_text(sum_retail_amount, (x_px, y_px), font_params, draw)
        self.draw_text(sum_wb, (x_px, y_px+(interval*1)), font_params, draw)
        self.draw_text(sum_input, (x_px, y_px+(interval*2)), font_params, draw)
        self.draw_text(tax, (x_px, y_px+(interval*3)), font_params, draw)
        self.draw_text(stable_expence_distrib, (x_px, y_px+(interval*4)), font_params, draw)
        self.draw_text(variable_expence, (x_px, y_px+(interval*5)), font_params, draw)
        self.draw_text(income, (x_px, y_px+(interval*6)), font_params, draw)
        self.draw_text(net_income, (x_px, y_px+(interval*7)), font_params, draw)
        self.draw_text(rent, (x_px, y_px+(interval*8)), font_params, draw)

        image_bytes = self.image_to_bytes(image) 
        return image_bytes
    
    def handle_pre_report_expence(self, 
                     week: str,
                     stable_expence: int, 
                     x_px = 580,
                     y_px = 323
                     ) -> BytesIO:
        image = self.image_stable_expence.copy()
        draw = ImageDraw.Draw(image)
        font_params = self.montserrat_bold_params
        font_week = self.montserrat_bold_week
        
        self.draw_text(week, self.pos_week, font_week, draw)
        self.draw_text(stable_expence, (x_px, y_px), font_params, draw)
        image_bytes = self.image_to_bytes(image) 
        
        return image_bytes
    
    def handle_suppliers(self, week: str):
        image = self.image_suppliers.copy()
        draw = ImageDraw.Draw(image)
        font_week = self.montserrat_bold_week
        
        self.draw_text(week, self.pos_week, font_week, draw)
        
        image_bytes = self.image_to_bytes(image) 
        
        return image_bytes
    
    def handle_wo_suppliers(self, week: str):
        image = self.image_wo_suppliers.copy()
        draw = ImageDraw.Draw(image)
        font_week = self.montserrat_bold_week
        
        self.draw_text(week, self.pos_week, font_week, draw)
        
        image_bytes = self.image_to_bytes(image) 

        return image_bytes
    
    def handle_capitalization(self,
                      count_remains: int,
                      to_clients: int,
                      from_clients: int,
                      in_warehouses: int,
                      all_remains: int,
                      x_px = 550,
                      y_px = 180,
                      interval = 59
        ) -> BytesIO:
        image = self.image_capitalization.copy()
        draw = ImageDraw.Draw(image)
        
        font_params = self.montserrat_semibold_params

        self.draw_text(count_remains, (x_px, y_px), font_params, draw)
        self.draw_text(in_warehouses, (x_px, y_px+(interval*1)), font_params, draw)
        self.draw_text(to_clients, (x_px, y_px+(interval*2)), font_params, draw)
        self.draw_text(from_clients, (x_px, y_px+(interval*3)), font_params, draw)
        self.draw_text(all_remains, (x_px, y_px+(interval*4)), font_params, draw)
        image_bytes = self.image_to_bytes(image) 
        return image_bytes
    
text_putter = PutText()
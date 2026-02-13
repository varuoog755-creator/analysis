from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

class ViralCardGenerator:
    def __init__(self):
        self.width = 800
        self.height = 400
        self.bg_color = (15, 23, 42) # Premium slate
        self.text_color = (255, 255, 255)
        self.accent_color = (56, 189, 248) # Sky blue
        self.accent_green = (34, 197, 94)

    def generate_viral_card(self, keyword, data):
        """Generates a shareable image for a trend."""
        img = Image.new('RGB', (self.width, self.height), color=self.bg_color)
        draw = ImageDraw.Draw(img)
        
        # Draw Border
        draw.rectangle([10, 10, self.width-10, self.height-10], outline=self.accent_color, width=2)
        
        # Title
        try:
            # Try to use a clean font if available, else default
            font_title = ImageFont.load_default(size=40)
            font_sub = ImageFont.load_default(size=20)
        except:
            font_title = ImageFont.load_default()
            font_sub = ImageFont.load_default()

        draw.text((40, 40), f"TREND PULSE: {keyword.upper()}", fill=self.accent_color, font=font_title)
        draw.text((40, 100), "Market Intelligence Report | Phase 1 Verified", fill=self.text_color, font=font_sub)
        
        # Mock Graph Line (Simplified)
        points = [(100, 300), (200, 250), (300, 280), (400, 150), (500, 100), (600, 120), (700, 80)]
        draw.line(points, fill=self.accent_green, width=5)
        
        # Save
        filename = f"viral_{keyword.replace(' ', '_')}.png"
        img.save(filename)
        return filename

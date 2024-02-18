from app import app
from models import db, User, Brand, Laptop, Phone, Accessory, SoundDevice
from datetime import datetime

def seed_database():
    with app.app_context():
        # Delete existing records
        db.session.query(User).delete()
        db.session.query(Brand).delete()
        db.session.query(Laptop).delete()
        db.session.query(Phone).delete()
        db.session.query(Accessory).delete()
        db.session.query(SoundDevice).delete()
        db.session.commit()

        # Create users
        users = [
            User(role='student'),
            User(role='employee'),
            User(role='teacher'),
            User(role='developer')
        ]
        db.session.add_all(users)

        # Create brands
        smartphone_brands = ["Apple", "Samsung", "Google", "OnePlus", "Xiaomi"]
        laptop_brands = ["Apple", "Dell", "HP", "Lenovo", "Asus", "Microsoft"]
        brands = smartphone_brands + laptop_brands
        for brand_name in brands:
            db.session.add(Brand(name=brand_name, logo_url=f"https://source.unsplash.com/200x200/?{brand_name}"))

        # Create laptops
        laptops = [
            ("MacBook Pro", "Apple", 2000, "new", "https://source.unsplash.com/500x500/?laptop"),
            ("XPS 13", "Dell", 1500, "used", "https://source.unsplash.com/500x500/?dell,laptop"),
            ("Pavilion 15", "HP", 1200, "new", "https://source.unsplash.com/500x500/?hp,laptop"),
            ("ThinkPad X1 Carbon", "Lenovo", 1300, "used", "https://source.unsplash.com/500x500/?lenovo,laptop"),
            ("ZenBook 14", "Asus", 1400, "new", "https://source.unsplash.com/500x500/?asus,laptop"),
            ("Inspiron 15", "Dell", 1100, "new", "https://source.unsplash.com/500x500/?dell,laptop"),
            ("Envy 13", "HP", 1000, "used", "https://source.unsplash.com/500x500/?hp,laptop"),
            ("Legion 5", "Lenovo", 900, "new", "https://source.unsplash.com/500x500/?lenovo,laptop"),
            ("VivoBook 15", "Asus", 1200, "used", "https://source.unsplash.com/500x500/?asus,laptop"),
            ("MacBook Air", "Apple", 1800, "used", "https://source.unsplash.com/500x500/?apple,laptop"),
            ("Surface Laptop", "Microsoft", 1300, "new", "https://source.unsplash.com/500x500/?microsoft,laptop"),
            ("Latitude 14", "Dell", 1200, "used", "https://source.unsplash.com/500x500/?dell,laptop"),
            ("EliteBook 840", "HP", 1500, "new", "https://source.unsplash.com/500x500/?hp,laptop"),
            ("IdeaPad 5", "Lenovo", 950, "used", "https://source.unsplash.com/500x500/?lenovo,laptop"),
            ("VivoBook S15", "Asus", 1100, "new", "https://source.unsplash.com/500x500/?asus,laptop"),
        ]
        for name, brand_name, price, status, image_url in laptops:
          brand = Brand.query.filter_by(name=brand_name).first()
          if brand is None:
              print(f"Brand '{brand_name}' not found in the database.")
          else:
             db.session.add(Laptop(name=name, brand_id=brand.id, price=price, status=status, image_url=image_url))
        db.session.commit()

        # Create phones
        phones = [
            ("iPhone 12", "Apple", 700, "new", "https://source.unsplash.com/500x500/?iphone"),
            ("Galaxy S21", "Samsung", 600, "used", "https://source.unsplash.com/500x500/?samsung,phone"),
            ("Pixel 5", "Google", 500, "new", "https://source.unsplash.com/500x500/?google,phone"),
            ("OnePlus 9 Pro", "OnePlus", 550, "used", "https://source.unsplash.com/500x500/?oneplus,phone"),
            ("Redmi Note 10", "Xiaomi", 400, "new", "https://source.unsplash.com/500x500/?xiaomi,phone"),
            ("iPhone 11", "Apple", 600, "used", "https://source.unsplash.com/500x500/?iphone"),
            ("Galaxy Note 20", "Samsung", 650, "new", "https://source.unsplash.com/500x500/?samsung,phone"),
            ("Pixel 4a", "Google", 450, "used", "https://source.unsplash.com/500x500/?google,phone"),
            ("OnePlus 8T", "OnePlus", 500, "new", "https://source.unsplash.com/500x500/?oneplus,phone"),
            ("Mi 11", "Xiaomi", 450, "used", "https://source.unsplash.com/500x500/?xiaomi,phone"),
            ("iPhone SE", "Apple", 300, "new", "https://source.unsplash.com/500x500/?iphone"),
            ("Galaxy A52", "Samsung", 500, "used", "https://source.unsplash.com/500x500/?samsung,phone"),
            ("Pixel 6", "Google", 600, "new", "https://source.unsplash.com/500x500/?google,phone"),
            ("OnePlus Nord", "OnePlus", 550, "used", "https://source.unsplash.com/500x500/?oneplus,phone"),
        ]
        for name, brand_name, price, status, image_url in phones:
          brand = Brand.query.filter_by(name=brand_name).first()
          if brand is None:
              print(f"Brand '{brand_name}' not found in the database.")
          else:
            db.session.add(Phone(name=name, brand_id=brand.id, price=price, status=status, image_url=image_url))
        db.session.commit()

        # Create accessories
        accessories = [
            ("Wireless Earbuds", "https://source.unsplash.com/500x500/?earbuds"),
            ("Smartwatch", "https://source.unsplash.com/500x500/?smartwatch"),
            ("Bluetooth Speaker", "https://source.unsplash.com/500x500/?speaker"),
            ("Phone Case", "https://source.unsplash.com/500x500/?phone,case"),
            ("Laptop Sleeve", "https://source.unsplash.com/500x500/?laptop,sleeve"),
            ("USB-C Adapter", "https://source.unsplash.com/500x500/?adapter"),
            ("Wireless Charger", "https://source.unsplash.com/500x500/?wireless,charger"),
            ("External Hard Drive", "https://source.unsplash.com/500x500/?external,hard,drive"),
            ("Gaming Mouse", "https://source.unsplash.com/500x500/?gaming,mouse"),
            ("Laptop Stand", "https://source.unsplash.com/500x500/?laptop,stand"),
            ("Screen Protector", "https://source.unsplash.com/500x500/?screen,protector"),
            ("Keyboard Cover", "https://source.unsplash.com/500x500/?keyboard,cover"),
            ("Camera Lens Kit", "https://source.unsplash.com/500x500/?camera,lens"),
            ("Fitness Tracker", "https://source.unsplash.com/500x500/?fitness,tracker"),
            ("HDMI Cable", "https://source.unsplash.com/500x500/?hdmi,cable"),
        ]
        for name, image_url in accessories:
            db.session.add(Accessory(name=name, price=1000, image_url=image_url))
        db.session.commit()

        # Create sound devices
        sound_devices = [
            ("Bose QuietComfort 35 II", 300, "https://source.unsplash.com/500x500/?headphones"),
            ("Anker Soundcore Life Q30", 200, "https://source.unsplash.com/500x500/?headphones"),
            ("JBL Live 650BTNC", 150, "https://source.unsplash.com/500x500/?headphones"),
            ("Sony WH-H910N", 250, "https://source.unsplash.com/500x500/?headphones"),
            ("Beats Studio3 Wired", 350, "https://source.unsplash.com/500x500/?headphones"),
            ("Logitech Z623", 100, "https://source.unsplash.com/500x500/?speaker"),
            ("Creative T15", 120, "https://source.unsplash.com/500x500/?speaker"),
            ("Koss Porta Pro", 130, "https://source.unsplash.com/500x500/?headphones"),
            ("Audio-Technica ATH-M50xBT", 200, "https://source.unsplash.com/500x500/?headphones"),
            ("Shure BLX Wireless", 250, "https://source.unsplash.com/500x500/?microphone"),
            ("AKG K371", 220, "https://source.unsplash.com/500x500/?headphones"),
            ("Sennheiser HD 4.50 BT", 270, "https://source.unsplash.com/500x500/?headphones"),
            ("Jabra Elite 85h", 300, "https://source.unsplash.com/500x500/?headphones"),
            ("Plantronics BackBeat Go 910", 180, "https://source.unsplash.com/500x500/?headphones"),
            ("Bowers & Wilkins PX7", 350, "https://source.unsplash.com/500x500/?headphones"),
        ]
        for name, price, image_url in sound_devices:
            db.session.add(SoundDevice(name=name, price=price, image_url=image_url))

        # Commit all changes to the database
        db.session.commit()

if __name__ == '__main__':
    app.app_context().push()
    seed_database()

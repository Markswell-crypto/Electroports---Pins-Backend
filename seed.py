from app import app
from models import db, User, Brand, Laptop, Phone, Accessory, SoundDevice, Review, Order, OrderItem
from faker import Faker

fake = Faker()

def seed_database():
    with app.app_context():
        # Delete existing records
        db.session.query(User).delete()
        db.session.query(Brand).delete()
        db.session.query(Laptop).delete()
        db.session.query(Phone).delete()
        db.session.query(Accessory).delete()
        db.session.query(SoundDevice).delete()
        db.session.query(Review).delete()
        db.session.query(OrderItem).delete()
        db.session.query(Order).delete()

        # Commit deletion of existing records
        db.session.commit()

        # Create users
        users = [
            User(username='admin', email='admin@gmail.com', role='admin', password='1234'),
            User(username='gerald', email='gerald@gmail.com', password='gerald'),
            User(username='joyce', email='joyce@gmail.com', password='joyce'),
            User(username='brian', email='brian@gmail.com', password='brian'),
            User(username='leon', email='leon@gmail.com', password='leon'),
            User(username='mercy', email='mercy@gmail.com', password='mercy'),
            User(username='maxy', email='maxy@gmail.com', role='admin', password='maxy')
        ]
        db.session.add_all(users)

        # Create brands
        smartphone_brands = ["Apple", "Samsung", "Google", "OnePlus", "Xiaomi"]
        laptop_brands = ["Apple", "Dell", "HP", "Lenovo", "Asus", "Microsoft"]
        brands = smartphone_brands + laptop_brands
        for brand_name in brands:
            db.session.add(Brand(name=brand_name, logo_url=f"https://source.unsplash.com/200x200/?{brand_name}"))

        # Commit brands
        db.session.commit()

        # Create laptops
        laptops = [
            ("MacBook Pro", "Apple", 10000, "new", "https://source.unsplash.com/500x500/?laptop"),
            ("XPS 13", "Dell", 45000, "used", "https://source.unsplash.com/500x500/?dell,laptop"),
            ("Pavilion 15", "HP", 62000, "new", "https://source.unsplash.com/500x500/?hp,laptop"),
            ("ThinkPad X1 Carbon", "Lenovo", 33000, "used", "https://source.unsplash.com/500x500/?lenovo,laptop"),
            ("ZenBook 14", "Asus", 34000, "new", "https://source.unsplash.com/500x500/?asus,laptop"),
            ("Inspiron 15", "Dell", 21000, "new", "https://source.unsplash.com/500x500/?dell,laptop"),
            ("Envy 13", "HP", 30000, "used", "https://source.unsplash.com/500x500/?hp,laptop"),
            ("Legion 5", "Lenovo", 29000, "new", "https://source.unsplash.com/500x500/?lenovo,laptop"),
            ("VivoBook 15", "Asus", 32000, "used", "https://source.unsplash.com/500x500/?asus,laptop"),
            ("MacBook Air", "Apple", 78000, "used", "https://source.unsplash.com/500x500/?apple,laptop"),
            ("Surface Laptop", "Microsoft", 33000, "new", "https://source.unsplash.com/500x500/?microsoft,laptop"),
            ("Latitude 14", "Dell", 22000, "used", "https://source.unsplash.com/500x500/?dell,laptop"),
            ("EliteBook 840", "HP", 15000, "new", "https://source.unsplash.com/500x500/?hp,laptop"),
            ("IdeaPad 5", "Lenovo", 2500, "used", "https://source.unsplash.com/500x500/?lenovo,laptop"),
            ("VivoBook S15", "Asus", 21000, "new", "https://source.unsplash.com/500x500/?asus,laptop"),
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
            ("iPhone 12", "Apple", 70000, "new", "https://source.unsplash.com/500x500/?iphone"),
            ("Galaxy S21", "Samsung", 60000, "used", "https://source.unsplash.com/500x500/?samsung,phone"),
            ("Pixel 5", "Google", 50000, "new", "https://source.unsplash.com/500x500/?google,phone"),
            ("OnePlus 9 Pro", "OnePlus", 55000, "used", "https://source.unsplash.com/500x500/?oneplus,phone"),
            ("Redmi Note 10", "Xiaomi", 40000, "new", "https://source.unsplash.com/500x500/?xiaomi,phone"),
            ("iPhone 11", "Apple", 40000, "used", "https://source.unsplash.com/500x500/?iphone"),
            ("Galaxy Note 20", "Samsung", 65000, "new", "https://source.unsplash.com/500x500/?samsung,phone"),
            ("Pixel 4a", "Google", 45000, "used", "https://source.unsplash.com/500x500/?google,phone"),
            ("OnePlus 8T", "OnePlus", 50000, "new", "https://source.unsplash.com/500x500/?oneplus,phone"),
            ("Mi 11", "Xiaomi", 45000, "used", "https://source.unsplash.com/500x500/?xiaomi,phone"),
            ("iPhone SE", "Apple", 30000, "new", "https://source.unsplash.com/500x500/?iphone"),
            ("Galaxy A52", "Samsung", 50000, "used", "https://source.unsplash.com/500x500/?samsung,phone"),
            ("Pixel 6", "Google", 60000, "new", "https://source.unsplash.com/500x500/?google,phone"),
            ("OnePlus Nord", "OnePlus", 55000, "used", "https://source.unsplash.com/500x500/?oneplus,phone"),
        ]
        for name, brand_name, price, status, image_url in phones:
            brand = Brand.query.filter_by(name=brand_name).first()
            if brand is None:
                print(f"Brand '{brand_name}' not found in the database")
            else:
                db.session.add(Phone(name=name, brand_id=brand.id, price=price, status=status, image_url=image_url))
        db.session.commit()

        # Create accessories
        accessories = [
            ("Wireless Earbuds", 999, "https://source.unsplash.com/500x500/?earbuds"),
            ("Smartwatch", 4999, "https://source.unsplash.com/500x500/?smartwatch"),
            ("Bluetooth Speaker", 2499, "https://source.unsplash.com/500x500/?speaker"),
            ("Phone Case", 500, "https://source.unsplash.com/500x500/?phone,case"),
            ("Laptop Sleeve", 200, "https://source.unsplash.com/500x500/?laptop,sleeve"),
            ("USB-C Adapter", 1000, "https://source.unsplash.com/500x500/?adapter"),
            ("Wireless Charger", 2500, "https://source.unsplash.com/500x500/?wireless,charger"),
            ("External Hard Drive", 8000, "https://source.unsplash.com/500x500/?external,hard,drive"),
            ("Gaming Mouse", 3000, "https://source.unsplash.com/500x500/?gaming,mouse"),
            ("Laptop Stand", 4000, "https://source.unsplash.com/500x500/?laptop,stand"),
            ("Screen Protector", 3500, "https://source.unsplash.com/500x500/?screen,protector"),
            ("Keyboard Cover", 1500, "https://source.unsplash.com/500x500/?keyboard,cover"),
            ("Camera Lens Kit", 7000, "https://source.unsplash.com/500x500/?camera,lens"),
            ("Fitness Tracker", 6000, "https://source.unsplash.com/500x500/?fitness,tracker"),
            ("HDMI Cable", 2000, "https://source.unsplash.com/500x500/?hdmi,cable"),
        ]
        for name, price, image_url in accessories:
            db.session.add(Accessory(name=name, price=price, image_url=image_url))
        db.session.commit()

        # Create sound devices
        sound_devices = [
            ("Bose QuietComfort 35 II", 3000, "https://source.unsplash.com/500x500/?headphones"),
            ("Anker Soundcore Life Q30", 2000, "https://source.unsplash.com/500x500/?headphones"),
            ("JBL Live 650BTNC", 1500, "https://source.unsplash.com/500x500/?headphones"),
            ("Sony WH-H910N", 2500, "https://source.unsplash.com/500x500/?headphones"),
            ("Beats Studio3 Wired", 3500, "https://source.unsplash.com/500x500/?headphones"),
            ("Logitech Z623", 1000, "https://source.unsplash.com/500x500/?speaker"),
            ("Creative T15", 1200, "https://source.unsplash.com/500x500/?speaker"),
            ("Koss Porta Pro", 1300, "https://source.unsplash.com/500x500/?headphones"),
            ("Audio-Technica ATH-M50xBT", 2000, "https://source.unsplash.com/500x500/?headphones"),
            ("Shure BLX Wireless", 2500, "https://source.unsplash.com/500x500/?microphone"),
            ("AKG K371", 2200, "https://source.unsplash.com/500x500/?headphones"),
            ("Sennheiser HD 4.50 BT", 2700, "https://source.unsplash.com/500x500/?headphones"),
            ("Jabra Elite 85h", 3000, "https://source.unsplash.com/500x500/?headphones"),
            ("Plantronics BackBeat Go 910", 1800, "https://source.unsplash.com/500x500/?headphones"),
            ("Bowers & Wilkins PX7", 3500, "https://source.unsplash.com/500x500/?headphones"),
        ]
        for name, price, image_url in sound_devices:
            db.session.add(SoundDevice(name=name, price=price, image_url=image_url))

        # Commit sound devices
        db.session.commit()

        # Create reviews
        for _ in range(20):
            user_id = fake.random_int(min=1, max=4)  # Assuming you have at least 4 users
            component_type = fake.random_element(elements=('laptop', 'phone', 'accessory', 'sound device'))
            component_id = fake.random_int(min=1, max=15)  # Adjust the max value based on the number of records in each component type
            rating = fake.random_int(min=1, max=5)
            comment = fake.text(max_nb_chars=150)
            review = Review(user_id=user_id, component_type=component_type, component_id=component_id, rating=rating, comment=comment)
            db.session.add(review)

        # Commit reviews
        db.session.commit()

        # Create orders and order items
        for _ in range(10):
            user_id = fake.random_int(min=1, max=4)  # Assuming you have at least 4 users
            total_price = fake.random_int(min=1000, max=100000)
            order_date = fake.date_time_between(start_date='-30d', end_date='now')
            order = Order(user_id=user_id, total_price=total_price, order_date=order_date)
            db.session.add(order)
            db.session.commit()  # Commit the order first to get the order_id
            order_id = order.id
            # Add order items
            for _ in range(fake.random_int(min=1, max=5)):
                component_type = fake.random_element(elements=('laptop', 'phone', 'accessory', 'sound device'))
                component_id = fake.random_int(min=1, max=15)  # Adjust the max value based on the number of records in each component type
                quantity = fake.random_int(min=1, max=5)
                order_item = OrderItem(order_id=order_id, component_type=component_type, component_id=component_id, quantity=quantity)
                db.session.add(order_item)

        # Commit orders and order items
        db.session.commit()

if __name__ == '__main__':
    app.app_context().push()
    seed_database()

                      

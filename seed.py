import os
from app import app, db, bcrypt
from models import User, Brand, Phone, Laptop, Accessory, SoundDevice, Review, Order, OrderItem
from datetime import datetime

def seed_database():
    
    # Use app context
    with app.app_context():
        
        # Delete all existing data from the tables
        db.session.query(OrderItem).delete()
        db.session.query(Order).delete()
        db.session.query(Review).delete()
        db.session.query(SoundDevice).delete()
        db.session.query(Accessory).delete()
        db.session.query(Laptop).delete()
        db.session.query(Phone).delete()
        db.session.query(Brand).delete()
        db.session.query(User).delete()
        db.session.commit()

        # Users
        users_data = [
            {"username": "admin", "email": "admin@gmail.com", "role": "admin", "password": bcrypt.generate_password_hash('1234').decode('utf-8')},
            {"username": "gerald", "email": "gerald@gmail.com", "password": bcrypt.generate_password_hash('gerald').decode('utf-8')},
            {"username": "joyce", "email": "joyce@gmail.com", "password": bcrypt.generate_password_hash('joyce').decode('utf-8')},
            {"username": "brian", "email": "brian@gmail.com", "password": bcrypt.generate_password_hash('brian').decode('utf-8')},
            {"username": "leon", "email": "leon@gmail.com", "password": bcrypt.generate_password_hash('leon').decode('utf-8')},
            {"username": "mercy", "email": "mercy@gmail.com", "password": bcrypt.generate_password_hash('mercy').decode('utf-8')},
            {"username": "maxy", "email": "maxy@gmail.com", "role": "admin", "password": bcrypt.generate_password_hash('maxy').decode('utf-8')}
            ]

        users = [User(**data) for data in users_data]

        # Brands
        brands_data = [
            {"name": "Apple", "logo_url": "https://example.com/apple_logo.jpg"},
            {"name": "Samsung", "logo_url": "https://example.com/samsung_logo.jpg"},
            {"name": "Google", "logo_url": "https://example.com/google_logo.jpg"},
            {"name": "OnePlus", "logo_url": "https://example.com/oneplus_logo.jpg"},
            {"name": "Xiaomi", "logo_url": "https://example.com/xiaomi_logo.jpg"},
            {"name": "Dell", "logo_url": "https://example.com/dell_logo.jpg"},
            {"name": "Microsoft", "logo_url": "https://example.com/microsoft_logo.jpg"},
            {"name": "Lenovo", "logo_url": "https://example.com/lenovo_logo.jpg"},
            {"name": "Asus", "logo_url": "https://example.com/asus_logo.jpg"},
            ]
        brands = [Brand(**data) for data in brands_data]

        # Phones
        phones_data = [
            {
                "brand": brands[0],  # Apple brand
                "name": "iPhone 12 Pro Max",
                "price": 90099,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/iPhone-12-Pro-Max.jpeg",
                "description": "5G goes Pro. A14 Bionic rockets past every other smartphone chip. The Pro camera system takes low-light photography to the next level — with an even bigger jump on iPhone 12 Pro Max. And Ceramic Shield delivers four times better drop performance. Let’s see what this thing can do."
            },
            {
                "brand": brands[0],  # Apple brand
                "name": "iPhone 12",
                "price": 70099,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/iPhone-12.jpeg",
                "description": "5G speed. A14 Bionic, the fastest chip in a smartphone. An edge-to-edge OLED display. Ceramic Shield with four times better drop performance. And Night mode on every camera. iPhone 12 has it all — in two perfect sizes."
            },
            {
                "brand": brands[1],  # Samsung brand
                "name": "Galaxy Z Fold2 5G",
                "price": 110099,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Galaxy-Z-Fold2-5G.jpg",
                "description": "A mind-bending glass screen that folds like a book. A hands-free camera that shoots when you wave. A precision-crafted hinge that transforms a cutting-edge smartphone into something much more. Meet the anything but ordinary Galaxy Z Fold2 5G."
            },
            {
                "brand": brands[1],  # Samsung brand
                "name": "Galaxy S21 Ultra 5G",
                "price": 120049,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Galaxy-S21-Ultra5G.jpg",
                "description": "Introducing Galaxy S21 Ultra 5G. The highest resolution photos and video on a smartphone. Galaxy's fastest processor yet. A battery that goes all-day—and then some. First-ever S Pen compatibility. A striking new design. It's an Ultra that easily lives up to its name."
            },
            {
                "brand": brands[2],  # Google brand
                "name": "Pixel 5 5G 128GB",
                "price": 69049,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Pixel-5-5G-128GB.jpeg",
                "description": "What happens when you bring together the ultimate Google phone and the speed of 5G?* You get Pixel 5. The super-fast Google phone at a helpful price."
            },
            {
                "brand": brands[2],  # Google brand
                "name": "Pixel 4a 5G UW 128GB",
                "price": 50499,
                "status": "used",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Pixel-4a-5G-UW-128GB.jpeg",
                "description": "Pixel 4a with 5G is the budget-friendly, super-fast phone from Google. It has the helpful stuff you need in a phone, with an extra boost of 5G speed."
            },
            {
                "brand": brands[3],  # LG brand
                "name": "V40 ThinQ - Aurora Black",
                "price": 90879,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/V40-ThinQ-Aurora-Black.jpeg",
                "description": "Capture moments at different angles with this Verizon LG V40 ThinQ smartphone. The five-camera design offers multiple ways to take selfies and other photos, and the 6.4-inch display lets you view them clearly in vibrant colors. This LG V40 ThinQ smartphone has a Boombox speaker so you can enjoy DTS:X surround sound wherever you go."
            },
            {
                "brand": brands[3],  # LG brand
                "name": "G8X ThinQ - Aurora Black",
                "price": 77999,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/G8X-ThinQ-Aurora-Black.jpeg",
                "description": "LG G8X ThinQ Cell Phone for AT&T: Do more at once with this LG G8X ThinQ smartphone. The 6.4-inch OLED FullVision display connects to a detachable secondary display to create a foldable dual-screen experience, while the 32.0MP front camera lets you capture favorite moments. This LG G8X ThinQ smartphone features a Snapdragon 855 processor, 6GB of RAM, and 128GB storage for seamless performance."
            },
            {
                "brand": brands[4],  # Sony brand
                "name": "Xperia 1 II 256GB",
                "price": 114999,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Xperia-1-II-256GB.jpeg",
                "description": "Stay connected with this unlocked Sony Xperia 1 II smartphone. The 6.5-inch 4K OLED HDR screen delivers detailed visuals and easy menu navigation, while the octa-core Qualcomm Snapdragon processor and 8GB of RAM provide fast processing speeds. This black Sony Xperia 1 II smartphone has 256GB of built-in storage to hold files and applications, and the triple 12.0MP camera lets you capture stunning, clear photos."
            },
            {
                "brand": brands[4],  # Sony brand
                "name": "Xperia 5 II 128GB",
                "price": 89999,
                "status": "new",
                "image_url": "https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Xperia-5-II-128GB.jpeg",
                "description": "Level up your entertainment and creativity with a 120Hz 21:9 CinemaWide™ 6.1” HDR OLED display and technology from Sony's audio, video, and award-winning Alpha camera series. Featuring one front-facing 8MP camera and three 12MP rear cameras with ZEISS® optics, Real-time Eye AF, up to 20fps with AF/AE tracking, and Photography Pro with RAW lets you capture stunning images in almost any lighting condition. It also has the world’s first 4K"
            }
        ]
        phones = [Phone(**data) for data in phones_data]

        # Laptops
        laptops_data = [
            {
                "brand": brands[0],  # Apple brand
                "name": "MacBook Pro 13”",
                "description": "The Apple M1 chip gives the 13‑inch MacBook Pro speed and power beyond belief. With up to 2.8x CPU performance. Up to 5x the graphics speed. Apple's most advanced Neural Engine for up to 11x faster machine learning. And up to 20 hours of battery life — the longest of any Mac ever. It’s the most popular pro notebook, taken to a whole new level.",
                "price": 149900,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/MacBook-Pro-13.jpeg"
            },
            {
                "brand": brands[0],  # Apple brand
                "name": "MacBook Pro 16”",
                "description": "Designed for those who defy limits and change the world, the 16-inch MacBook Pro is by far the most powerful notebook Apple has ever made. With an immersive Retina display, superfast processors, advanced graphics, the largest battery capacity ever in a MacBook Pro, Magic Keyboard, and massive storage, it's the ultimate pro notebook for the ultimate user.",
                "price": 279900,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/MacBook-Pro-16.jpeg"
            },
            {
                "brand": brands[0],  # Apple brand
                "name": "MacBook Air",
                "description": "Apple's thinnest, lightest notebook, completely transformed by the Apple M1 chip. CPU speeds up to 3.5x faster. GPU speeds up to 5x faster. With Apple's most advanced Neural Engine for up to 9x faster machine learning. The longest battery life ever in a MacBook Air. And a silent, fanless design. This much power has never been this ready to go.",
                "price": 124900,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/MacBook-Air.jpeg"
            },
            {
                "brand": brands[6],  # Samsung brand
                "name": "Galaxy Book Pro 360",
                "description": "Turn heads and turn around your work-life balance with the premium PC that converts to a top-of-the-line tablet. With a redesigned S Pen, a brilliant Super AMOLED screen, the latest Intel® 11th Gen Core™ processor, Intel® Evo™ certification and with Samsung's latest wi-fi chip, you get the power to flip from getting work done to fun instantly.",
                "price": 129999,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/Galaxy-Book-Pro-360.jpg"
            },
            {
                "brand": brands[6],  # Samsung brand
                "name": "Galaxy Book Flex2 Alpha",
                "description": "Everything you love in a Galaxy PC, taken further. The ultra-slim Galaxy Book Flex2 ⍺ sits at the top of its class with a super vivid QLED touchscreen, the latest Intel® 11th Gen Core™ processor and a 2-in-1 design that transforms from a laptop to a tablet. With a super-fast-charging battery that lasts 18.5 hours¹ and innovations galore, this Galaxy Book was made to exceed all expectations.",
                "price": 104999,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/Galaxy-Book-Flex2-Alpha.jpg"
            },
            {
                "brand": brands[6],  # Samsung brand
                "name": "Galaxy Book Pro",
                "description": "PC power that’s smartphone thin. Samsung's lightest Galaxy Book yet gives you a powerful Intel® 11th Gen Core™ processor, Intel® Evo™ certification, an advanced AMOLED screen and comes equipped with their latest wi-fi chip. Finish important projects, download huge files fast or watch movies in brilliant color. Discover the perfect mix of portability and Accessoryivity.",
                "price": 119999,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/Galaxy-Book-Pro.jpg"
            },
            {
                "brand": brands[2],  # Dell brand
                "name": "XPS 15 Touch Laptop",
                "description": "XPS laptops and 2-in-1s are precision-crafted with premium materials, featuring stunning displays and the performance you demand to express your creative self and your big ideas.",
                "price": 279999,
                "status":'New',
                "image":'https://modern-being.s3.us-west-2.amazonaws.com/laptops/XPS-15-Touch-Laptop.jpeg'
            },
            {
                "brand": brands[7],  # Dell brand
                "name": "ALIENWARE X15 R1 GAMING LAPTOP",
                "price": 339999,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/Alienware-x15-R1.jpeg",
                "description": "With iconic designs, high-performance gaming, and premium features, Alienware delivers the most immersive experiences."
            },
            {
                "brand": brands[7],  # Dell brand
                "name": "G5 15 5500",
                "price": 126999,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/Dell-G5-15-5500.jpeg",
                "description": "G Series equips you with all the essentials you need to experience split-second responsiveness and immersive gameplay."
            },
            {
                "brand": brands[8],  # Microsoft brand
                "name": "Surface Pro X",
                "price": 149999,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/Surface-Pro-X.jpeg",
                "description": "With Microsoft SQ® 1 and new Microsoft SQ® 2 chipsets, blazing-fast LTE connectivity, their thinnest Surface features two USB-C® ports and a stunning, virtually edge-to-edge 13” touchscreen, plus new choice of colors. Surface Pro X Keyboard and rechargeable Surface Slim Pen sold separately."
            },
            {
                "brand": brands[8],  # Microsoft brand
                "name": "Surface Book 3",
                "price": 139999,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/Surface-Book-3.jpeg",
                "description": "Meet the laptop that can handle your biggest demands. The most powerful Surface laptop yet combines speed, graphics, and immersive gaming with the versatility of a laptop, tablet, and portable studio. Feature's a high-resolution touchscreen."
            },
            {
                "brand": brands[8],  # Microsoft brand
                "name": "Surface Laptop 4",
                "price": 139999,
                "status": "New",
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/laptops/Surface-Laptop-4.jpeg",
                "description": "Style and speed. Stand out on HD video calls backed by Studio Mics. Capture ideas on the vibrant touchscreen. Do it all with a perfect balance of sleek design, speed, immersive audio, and significantly longer battery life than before."
            }
            ]
        laptops = [Laptop(**data) for data in laptops_data]

        # Accessories
        accessories_data = [
            {
                "name": "Quest 2 — Advanced All-In-One Virtual Reality Headset",
                "description": "Oculus Quest 2 is our most advanced all-in-one VR system yet. Every detail has been engineered to make virtual worlds adapt to your movements, letting you explore awe-inspiring games and experiences with unparalleled freedom. No PC or console required. Get the most out of each moment with blazing-fast performance and next-generation graphics. Stay focused with a stunning display that features 50% more pixels than the original Quest. Or take a break from the action and grab front-row seats to live concerts, exclusive events and more. The redesigned Touch controllers feature improved ergonomics and intuitive controls that transport your gestures, motions and actions directly into VR. You can even connect your VR headset to a gaming-compatible computer with an Oculus Link cable to access hundreds of PC VR games and experiences. Quest 2 also lets you bring your friends into the action. With live casting, you can share your VR experience with people around you. Or meet up with friends in virtual worlds to battle in multiplayer competitions or just spend some time together. With Oculus Quest 2, there’s no end in sight to what you can play, create and discover in virtual reality.",
                "price": 19900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Quest-2-Advanced-All-In-One-Virtual-Reality-Headset.jpg"
            },
            {
                "name": "Lenovo Star Wars",
                "description": "The smartphone-powered augmented reality experience brings an all-new Star Wars experience right into your home. Start the app, put on the headset, and begin your journey with three epic experiences. Wield a lightsaber and villains, train yourself in strategic combat against invading forces, and master the strategy of intergalactic Holochess",
                "price": 16500,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Lenovo-Star-Wars.jpg"
            },
            {
                "name": "HoloLens 2",
                "description": "HoloLens 2 offers the most comfortable and immersive mixed reality experience available-enhanced by the reliability, security, and scalability of Azure.",
                "price": 350000,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/HoloLens2.png"
            },
            {
                "name": "dynaEdge",
                "description": "The dynaEdge™ AR Smart Glasses enable multiple usage scenarios, including See-What-I-See, Remote Expert, Document Retrieval, Workflow Instructions and Real-Time Data Capture, making it the enterprise solution for tomorrow—starting today.",
                "price": 189900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/dynaEdge.png"
            },
            {
                "name": "Raptor",
                "description": "Raptor is the world’s first cycling computer for people, not bikes. Raptor is designed to enhance every ride by projecting an unobtrusive AR layer of information out in front of the cyclist’s eyes. Having real-time information projected out in front of you allows you to keep your eyes on the road ahead – increasing safety while focusing on performance, body posture, and accomplishments or simply soaking in the views and enjoying an amazing bike ride. Raptor’s HD front-facing camera allows you to relive your unforgettable moments with real-time metrics embedded in the videos.",
                "price": 59900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Raptor.png"
            },
            {
                "name": "Magic Leap 1",
                "description": "Magic Leap 1 is a lightweight, wearable computer that seamlessly blends the digital and physical worlds, allowing digital content to coexist with real world objects and the people around you. It sees what you see and uses its understanding of surroundings and context to create unbelievably believable experiences.",
                "price": 229500,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Magic-Leap-1.png"
            },
            {
                "name": "Moverio BT-40S Smart Glasses with Intelligent Touch Controller",
                "description": "Offering outstanding image quality and an intuitive touch controller, Epson Moverio BT-40S smart glasses take AR applications to the next level. Featuring innovative Si-OLED technology and dual-binocular displays – all in a comfortable design, they're the next generation of wearable, second-screen solutions.",
                "price": 99900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Moverio-BT-40S-Smart-Glasses-with-Intelligent-Touch-Controller.jpeg"
            },
            {
                "name": "Glass",
                "description": "Glass is a small, lightweight wearable computer with a transparent display for hands-free work.",
                "price": 116700,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Glass-2.jpg"
            },
            {
                "name": "X2 Mixed Reality Glasses",
                "description": "Lightweight mixed reality glasses. At 9.8 ounces, the X2 Mixed Reality Glasses fit a wide field of view, contain powerful sensors, and come with the VisionEye SLAM SDK into an exceptionally minimalistic form factor.",
                "price": 195000,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/X2-Mixed-Reality-Glasses.png"
            },
            {
                "name": "Kai Gesture Controller",
                "description": "The KAI is an intuitive device capable of tracking the slightest movements of your wrist and all four fingers to recognize gestures. It then processes these gestures on-board, allowing you to interact with your digital world easily. Virtual reality, Gaming, Presentations, Hardware Control & so on… The applications of the Kai are virtually endless.",
                "price": 15000,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/Kai-Gesture.png"
            },
            {
                "name": "NeoRhythm",
                "description": "NeoRhythm is a wearable technology using PEMF to entrain your brain. It has multiple programs for improved sleep, theta meditation, deep relaxation, improved focus, pain control, enhancing mental capacity, and energy and vitality.",
                "price": 29900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/NeoRhythm.jpeg"
            },
            {
                "name":         "CaptoGlove Wireless Virtual Reality Glove for Gaming and Smart Devices",
                "description": "CaptoGlove is a smart controller with advanced technology to precisely detect a wide variety of hand and finger movements. These gestures are translated into control commands which are sent directly to connected devices (such as PCs, VR Headsets, Smart Home, Internet of Things, iOS/Android Phones/Tablets/Consoles) to interact and control them faster, more naturally, and effectively. One glove can be used as a single controller or coupled with another CaptoGlove for use as a pair via a Bluetooth Low Energy (BTLE).",
                "price": 49000,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/CaptoGlove-Wireless-VR&Smart-Devices.jpeg"
            },
            {
                "name": "TACTIGON Skin Developer Kit",
                "description": "Tactigon SKIN is a programmable wearable to enable gesture control for robots, PC games, VR/AR, computers, 3D printers, drones, apps, and more.",
                "price": 80000,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/TACTIGON-Skin.jpeg"
            },
            {
                "name": "TeraRanger Evo Swipe Plus",
                "description": "Detect people movement, trigger actions based on proximity, understand customer engagement and perform touchless gesture recognition with one compact ToF sensor.",
                "price": 12900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/TeraRanger-Evo-Swipe-Plus.jpeg"
            },
            {
                "name": "Apple Watch Nike SE (GPS) 44mm",
                "price": 30900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Apple-Watch-Nike-SE.jpeg",
                "description": "With Apple Watch Nike SE, you can track your workouts and listen to Audio Guided Runs with the Nike Run Club app. Sync music for motivation to your watch. Turn on Nike Twilight Mode for enhanced visibility. And choose from exclusive Nike watch faces and bands."
            },
            {
                "name": "Fēnix 6X Pro Solar GPS/GLONASS/Galileo Watch",
                "price": 84999,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Fēnix-6X-Pro-Solar-GPS:GLONASS:Galileo-Watch.jpeg",
                "description": "Keep track of your fitness progress with this Garmin fenix 6X Pro Solar multisport GPS watch. The satellite navigation gives you the confidence to venture into paths less beaten, while the solar charging capability extends the battery life when outdoors. This Garmin fenix 6X Pro Solar multisport GPS watch features pace guidance assistance to keep you on your toes."
            },
            {
                "name": "Fēnix 5 Sapphire GPS Smartwatch 47mm Fiber-Reinforced Polymer",
                "price": 74999,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Fēnix-5-Sapphire-GPS-Smartwatch-47mm-Fiber-Reinforced-Polymer.jpeg",
                "description": "Ensure powerful performance by using this Fenix 5 sapphire watch. It monitors heart rate and location so that you can tell exactly how much exercise you've done, and it includes up to 24 hours of battery performance with the GPS on. Exceptional ruggedization combines with a sapphire lens to ensure this Fenix 5 sapphire watch resists daily abuse."
            },
            {
                "name": "Sense Advanced Health & Fitness Smartwatch",
                "price": 24995,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Sense-Advanced-Health-&-Fitness-Smartwatch.jpeg",
                "description": "Meet Fitbit Sense--the advanced health smartwatch that helps you tune into your body and guides you toward better health. Assess your heart for AFib right from your wrist, detect and manage stress, better understand your sleep quality and even keep an eye on patterns in your skin temperature or well-being with SpO2. Plus, Sense unlocks a 6-month trial of personalized guidance and advanced insights for new Fitbit Premium users."
            },
            {
                "name": "Versa 3 Health & Fitness Smartwatch",
                "price": 19995,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Versa-3-Health-&-Fitness-Smartwatch.jpeg",
                "description": "Meet Fitbit Versa 3--the smartwatch with everything you need to just go. Track your pace & distance--and leave your phone at home--with built-in GPS. You can also get call, text and app notifications, use Google Assistant or Amazon Alexa Built-in and control Spotify, Deezer and Pandora when your phone is nearby.* Plus with Active Zone Minutes, 20+ exercise modes and 6+ day battery with 12-minute fast charging, you've got all the motivation you need to reach your health & fitness goals.(Notifications work when your phone is nearby. Voice assistant not available in all countries, see fitbit.com/voice. Subscriptions required for use of music services; not available in all countries.Battery life varies with use and other factors; up to 12 hours with continuous GPS. 12-minute fast charging adds 24 hours of battery life)"
            },
            {
                "name": "Fossil - Gen 5 LTE Smartwatch (Cellular) 45mm",
                "price": 34900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Fossil-Gen-5-LTE-Smartwatch.jpeg",
                "description": "Tech for real life. This 45mm Gen 5 LTE touchscreen smartwatch features a black silicone strap, phone-free calling functionality, 8GB storage capacity and three smart battery modes to extend battery life for multiple days. Fossil Gen 5 LTE smartwatches work exclusively with Verizon branded Android phones (not unlocked phones) on the Verizon Network with qualified Numbershare data plan. NumberShare is required to activate service on LTE smartwatches. Numbershare is available with an eligible Verizon monthly plan. Adding a smartwatch to your Verizon data plan will incur additional monthly charges. Customers must have a compatible Android Smartphone (4G or 5G) active on their Verizon account. Compatible Android smartphone must have OS 6.0 or later, excluding Go edition, with an updated version of the MVS app \"My Verizon Services\" (v.1.0.104.2 or later) and must be HD voice capable, have HD voice turned On and be on an eligible plan. LTE smartwatches do not support a standalone activation, only activation via NumberShare is eligible. For more detailed information, please refer to your Verizon Connected Devices plan. Fossil Gen 5"
            }
        ]
        accessories = [Accessory(**data) for data in accessories_data]

        # Sound Devices
        sound_devices_data = [
            {
                "name": "One (2nd Gen)",
                "description": "Get rich, room-filling sound with Sonos One, and control it with your voice, the Sonos app, Apple AirPlay 2, and more.",
                "price": 19900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/One-2nd-Gen.png"            
                },
            {
                "name": "Move",
                "description": "Get brilliant sound anywhere with the weatherproof and drop-resistant Move. Control with your voice, the Sonos app, and Apple AirPlay 2 at home, and stream via Bluetooth® when WiFi isn't available.",
                "price": 39900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Move.png"            
                },
            {
                "name": "HomePod mini",
                "description": "Jam-packed with innovation, HomePod mini delivers unexpectedly big sound for a speaker of its size. At just 3.3 inches tall, it takes up almost no space but fills the entire room with rich 360‑degree audio that sounds amazing from every angle.",
                "price": 9900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/HomePod-mini.jpeg"            
                },
            {
                "name": "Echo (4th Gen)",
                "description": "Talk about well-rounded. Echo combines premium sound, a built-in Zigbee smart home hub, and a temperature sensor. Powerful speakers deliver clear highs, dynamic mids, and deep bass for rich, detailed sound that adapts to any room.",
                "price": 7999,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Echo-4th-Gen.jpg"
                },
            {
                "name": "Echo Studio",
                "description": "You've never heard an Echo like this before. Echo Studio creates an immersive, 3-dimensional soundscape, wrapping you in studio-quality audio from every direction.",
                "price": 19999,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Echo-studio.jpeg"
                },
            {
                "name": "Nest Audio",
                "description": "Nest Audio adapts to your environment and whatever you’re listening to. So music sounds better. And news, radio, and audiobooks sound even clearer.",
                "price": 9999,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Nest-Audio.png"
                },
            {
                "name": "Nest Mini",
                "description": "Nest Mini. Still mini. Even more mighty.",
                "price": 3499,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Nest-Mini.png"
                },
            {
                "name": "Bose Smart Speaker 500",
                "description": "It’s powerfully simple. Fill any room with wall-to-wall stereo sound, while built-in voice control puts millions of songs at the tip of your tongue.",
                "price": 29900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Bose-Smart-Speaker-500.png"
                },
            {
                "name": "Bose Home Speaker 300",
                "description": "The Bose Home Speaker 300 brings room-rocking bass and 360° lifelike sound to a space-saving size. Plus, with built-in voice assistants, like the Google Assistant and Alexa, all of your favorite music is just an ask away. Turn it up and feel the difference.",
                "price": 19900,
                "image": "https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Bose-Home-Speaker-300.png"
                }
        ]
        sound_devices = [SoundDevice(**data) for data in sound_devices_data]

        reviews_data = [
            {
                "comment": "Great Device, highly recommended.",
                "phone_id": None,
                "laptop_id": None,
                "accessory_id": None,
                "sound_device_id": None,
            },
            {
                "comment": "Amazing Sound, exceeded my expectations.",
                "phone_id": None,
                "laptop_id": None,
                "accessory_id": None,
                "sound_device_id": None,
            },
        ]

        reviews = [Review(**data) for data in reviews_data]

        # Add objects to session and commit changes
        db.session.add_all(users + brands + phones + laptops + accessories + sound_devices + reviews)
        db.session.commit()
        print("Seeding Successful")
if __name__ == '__main__':
    seed_database()

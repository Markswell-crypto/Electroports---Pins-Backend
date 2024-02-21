from flask_restful import Resource, reqparse
from models import db, SoundDevice

sound_device_parser = reqparse.RequestParser()
sound_device_parser.add_argument('name', type=str, help='Sound device name', required=True)
sound_device_parser.add_argument('price', type=int, help='Sound device price', required=True)
sound_device_parser.add_argument('image_url', type=str, help='Image URL', required=False)
sound_device_parser.add_argument('description', type=str, help='Sound device description', required=False)  # Add description field

class SoundDevicesResource(Resource):
    def get(self):
        try:
            sound_devices = SoundDevice.query.all()
            return {
                "sound_devices": [
                    {
                        "id": device.id,
                        "name": device.name,
                        "price": device.price,
                        "image_url": device.image_url,
                        "description": device.description  # Add description field
                    }
                    for device in sound_devices
                ]
            }
        except Exception as e:
            return {"message": "An error occurred while retrieving sound devices.", "error": str(e)}, 500

    def post(self):
        try:
            args = sound_device_parser.parse_args()
            new_sound_device = SoundDevice(
                name=args['name'],
                price=args['price'],
                image_url=args['image_url'],
                description=args.get('description')  # Add description field
            )

            db.session.add(new_sound_device)
            db.session.commit()

            return {
                "sound_device": {
                    "id": new_sound_device.id,
                    "name": new_sound_device.name,
                    "price": new_sound_device.price,
                    "image_url": new_sound_device.image_url,
                    "description": new_sound_device.description  # Add description field
                }
            }, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the sound device.", "error": str(e)}, 500

class SoundDeviceByIDResource(Resource):
    def get(self, id):
        try:
            sound_device = SoundDevice.query.get(id)
            if not sound_device:
                return {"message": "Sound device not found."}, 404
            return {
                "sound_device": {
                    "id": sound_device.id,
                    "name": sound_device.name,
                    "price": sound_device.price,
                    "image_url": sound_device.image_url,
                    "description": sound_device.description  # Add description field
                }
            }
        except Exception as e:
            return {"message": "An error occurred while retrieving the sound device.", "error": str(e)}, 500

    def delete(self, id):
        try:
            sound_device = SoundDevice.query.get(id)
            if not sound_device:
                return {"message": "Sound device not found."}, 404
            db.session.delete(sound_device)
            db.session.commit()
            return {"message": "Sound device deleted successfully."}, 204
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while deleting the sound device.", "error": str(e)}, 500

    def patch(self, id):
        try:
            args = sound_device_parser.parse_args()
            sound_device = SoundDevice.query.get(id)
            if not sound_device:
                return {"message": "Sound device not found."}, 404
            sound_device.name = args['name']
            sound_device.price = args['price']
            sound_device.image_url = args['image_url']
            sound_device.description = args.get('description', sound_device.description)  # Add description field
            db.session.commit()
            return {
                "sound_device": {
                    "id": sound_device.id,
                    "name": sound_device.name,
                    "price": sound_device.price,
                    "image_url": sound_device.image_url,
                    "description": sound_device.description  # Add description field
                }
            }
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the sound device.", "error": str(e)}, 500

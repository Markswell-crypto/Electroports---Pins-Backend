from flask_restful import Resource, reqparse
from models import db, SoundDevice

sound_device_parser = reqparse.RequestParser()
sound_device_parser.add_argument('name', type=str, help='Sound Device name', required=True)
sound_device_parser.add_argument('price', type=int, help='Sound Device price', required=True)

class SoundDevicesResource(Resource):
    def get(self):
        sound_devices = SoundDevice.query.all()
        return {"sound_devices": [{"id": device.id, "name": device.name, "price": device.price} 
                                  for device in sound_devices]}

    def post(self):
        args = sound_device_parser.parse_args()
        new_sound_device = SoundDevice(name=args['name'], price=args['price'])

        db.session.add(new_sound_device)
        db.session.commit()

        return {"sound_device": {"id": new_sound_device.id, "name": new_sound_device.name,
                                 "price": new_sound_device.price}}, 201

class SoundDeviceByIDResource(Resource):
    def delete(self, id):
        sound_device = SoundDevice.query.get(id)

        if not sound_device:
            return {"message": "Sound Device not found."}, 404

        db.session.delete(sound_device)
        db.session.commit()

        return {"message": "Sound Device deleted successfully."}, 204

    def patch(self, id):
        sound_device = SoundDevice.query.get(id)

        if not sound_device:
            return {"message": "Sound Device not found."}, 404

        args = sound_device_parser.parse_args()
        sound_device.name = args['name']
        sound_device.price = args['price']

        db.session.commit()

        return {"sound_device": {"id": sound_device.id, "name": sound_device.name,
                                 "price": sound_device.price}}
from datetime import datetime
from json import loads

from flask import Blueprint, g, current_app, request, jsonify
from requests import codes
from werkzeug.exceptions import BadRequest
from webargs import fields
from webargs.flaskparser import parser

from rodeo.models.picture import Picture
from rodeo.stores.picture import PictureStore


api = Blueprint('picture_api_v1', __name__, url_prefix='/api/v1/picture')


def to_model(resource):
    # XXX this may make your code cleaner
    pass
    

def from_model(model):
    # XXX implementing this may make your code cleaner
    pass

@api.route('', methods=['POST'])
def create_payment_request():
    """
    Create a new `Picture`.
    """
    print request.data
    
    picture = PictureStore.create(Picture(**loads(request.data)))

    return (jsonify({'created_at': picture.created_at,
                     'updated_at': picture.updated_at,
                     'author': picture.author,
                     'file_id': picture.file_id,
                     'id': picture.id,
                     'edition': picture.edition}),
                     201)

@api.route('/<picture_id>', methods=['GET'])
def get_payment_request(picture_id):
    """
    Get an existing `Picture`.

    :param picture_id - Picture id

    """
    print picture_id
    picture = PictureStore.retrieve(picture_id) 
    return (jsonify({'created_at': picture.created_at,
                     'updated_at': picture.updated_at,
                     'author': picture.author,
                     'file_id': picture.file_id,
                     'id': picture.id,
                     'edition': picture.edition}),
                     200) 

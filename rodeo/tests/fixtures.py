from datetime import datetime
from uuid import uuid4

PICTURE = {
    'created_at': datetime.now(),
    'updated_at': datetime.now(),
    'author': "Sam",
    'file_id': "sdfsd",
    'id': uuid4().hex,
    'edition': 0,
}

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.sdbms import DBHelper

def test_db_connection():
    db = DBHelper()
    assert db.conn is not None
    assert db.c is not None
#!/usr/bin/python3
"""Application file storage instance"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

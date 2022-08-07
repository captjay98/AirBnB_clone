#!/usr/bin/python3
"""a Filestorage Instance is created."""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

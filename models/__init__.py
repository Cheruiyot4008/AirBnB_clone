#!/usr/bin/python3
"""Defining the __init__ magic methodology for models dir"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

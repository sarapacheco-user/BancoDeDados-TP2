from flask import Blueprint, render_template, request, redirect
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection import get_db_connection

from flask import Flask, render_template, request

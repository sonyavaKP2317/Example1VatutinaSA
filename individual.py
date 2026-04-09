import hashlib
import pandas as pd
import matplotlib.pyplot as plt

def get_hash(text):
  return hashlib.sha256(text.encode()).hexdigest()

#1. Расчетный контейнер
etalon =
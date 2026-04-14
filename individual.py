#Контейнер контроля и обеспечения целостности XML-схем
#Реализация модуля верификации (вычисления хеша)
import hashlib
import hmac
import os
import pandas as pd
import matplotlib.pyplot as plt

secret1 = os.environ['INTERCEPT_KEY']
secret2 = os.environ['VERIFY_SECRET_KEY']
secret3 = os.environ['SCHEMA_STORAGE']
secret4 = os.environ['AUDIT_SECRET_KEY']
print("Секретные ключи для контейнера обеспечения целостности XML-схем:")
print("Модуль перехвата:", secret1)
print("Модуль верификации:", secret2)
print("Модуль хранения:", secret3)
print("Модуль аудита:", secret4)

try:
  secret2 = os.environ['VERIFY_SECRET_KEY']
  secret2_bytes = secret2.encode()
  print("[OK] Ключ загружен")
except:
  print("[ERROR] Ключ не найден! Дальнейшее выполнение невозможно")
  exit(1)
  
def get_hash(text):
  return hmac.new(secret2_bytes, text.encode(), hashlib.sha256).hexdigest()

#1. Расчетный контейнер
etalon = '''<?xml version="1.0"?>
<xs:schema>
  <xs:element name="LaboratoryOrder">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="PatientID" type="xs:string"/>
        <xs:element name="TestCode" type="xs:string"/>
        <xs:element name="TestDate" type="xs:date"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema> '''

hash_etalon = get_hash(etalon)

schemas = [
  etalon, '''<?xml version="1.0"?>
  <xs:schema>
    <xs:element name="LaboratoryOrder">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="PatientID" type="xs:integer"/>
          <xs:element name="TestCode" type="xs:string"/>
          <xs:element name="TestDate" type="xs:date"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
  </xs:schema>''',
  etalon, '''<?xml version="1.0"?>
  <xs:schema>
    <xs:element name="LaboratoryOrder">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="PatientID" type="xs:data"/>
           <xs:element name="TestCode" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
  </xs:schema>''',
  etalon, etalon, '''<?xml version="1.0"?>
  <xs:schema>
    <xs:element name="LaboratoryOrder">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="PatientID" type="xs:string"/>
           <xs:element name="TestCode" type="xs:string"/>
           <xs:element name="Result" type="xs:string"/>
           <xs:element name="TestDate" type="xs:date"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
     </xs:schema>''',
  '''<?xml version="1.0"?>
  <xs:schema>
    <xs:element name="MedicalOrder">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="PatientID" type="xs:string"/>
           <xs:element name="TestCode" type="xs:string"/>
           <xs:element name="TestDate" type="xs:date"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    </xs:schema>''', etalon, etalon,
  '''<?xml version="1.0"?>
  <xs:schema>
    <xs:element name="LaboratoryOrder">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="PatientNumber" type="xs:string"/>
          <xs:element name="TestCode" type="xs:string"/>
           <xs:element name="TestDate" type="xs:date"/>
        </xs:sequence>
        </xs:complexType>
        </xs:element>
        </xs:schema>''',
  etalon, etalon, '''<?xml version="3.0"?>
  <xs:schema>
    <xs:element name="LaboratoryOrder">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="PatientID" type="xs:string"/>
          <xs:element name="Testik_KODE" type="xs:string"/>
          <xs:element name="Testik_DATE" type="xs:date"/>
          </xs:sequence>
           </xs:complexType>
           </xs:element>
           </xs:schema>''',
  etalon, etalon, etalon, etalon, etalon, etalon, etalon, etalon, etalon, etalon, etalon, '''<<xml version="1.0"?>
  <xs:schema>
    <xs:element name="Laboratory0rder">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="PatientID" type="xs:string"/>
            <xs:element name="TestCode" type="xs:string"/>
            <xs:element name="TestDate" type="xs:date"/>
            </xs:sequence>
            </xs:complexType>
            </xs:element>
            </xs:schema>''', '''<?xml version="2.0"?>
            <xs:schema>
            <xs:element name="LaboratoryOrder">
            <xs:complexType>
            <xs:sequence>
            <xs:element name="PatientID" type="xs:string"/>
            <xs:element name="TestCode" type="xs:string"/>
            <xs:element name="TestDate" type="xs:date"/>
            </xs:sequence>
            </xs:complexType>
            </xs:element>
            </xs:schema>''']

Y = []
hash_list = []
res_list = []
act_list = []

for i in range(len(schemas)):
  Y.append(i+1)
  h = get_hash(schemas[i])
  hash_list.append(h)
  if h == hash_etalon:
     res_list.append("Схема целостна")
     act_list.append("Передача для обработки")
  else:
     res_list.append("Схема нарушена!")
     act_list.append("Блокировка схемы. Подмена эталонной копией")
    
  print(f"\nПроверка {i+1} схемы")
  print(f"Хеш схемы: {h}")
  print(f"Результат проверки: {res_list[i]} -> {act_list[i]}")

#2. Контейнер для табличного вывода
table = list(zip(Y, hash_list, res_list, act_list))
tfame = pd.DataFrame(table, columns = (["N", "Хеш", "Статус","Действие"]))
print(tfame.to_string(max_colwidth=50))

#3. Контейнер визуализации
ok = res_list.count("Схема целостна")
bad = res_list.count("Схема нарушена!")
total = ok + bad

plt.figure()
plt.pie([ok, bad], labels=[f"Целостные схемы ({ok})", f"Нарушенные схемы ({bad})"], autopct="%1.1f%%")
plt.title("Результаты проверки (измененные)")
plt.savefig("chartpie_ind.png")

plt.figure()
plt.bar([f"Целостные схемы ({ok})", f"Нарушенные схемы ({bad})"], [ok, bad]) 
plt.title("Сравнение (измененное)")
plt.savefig("chartbar_ind.png")
plt.close()

plt.figure()
vals = []
for x in res_list:
  if x == "Схема целостна":
    vals.append(1)
  else:
    vals.append(0)
plt.plot(Y, vals)
plt.xlabel("Номер проверки")
plt.ylabel(f"1 - целостна ({ok}), 0 - нарушена({bad})")
plt.title("Динамика проверок (измененная)")
plt.savefig("chartline_ind.png")
plt.close()
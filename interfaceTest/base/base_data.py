#!/bin/python3
# -*- encoding:utf-8 -*-


from interfaceTest.base.baseLogin import BaseLogin
from interfaceTest.common.readData import ReadDataBase
import random

diagnosis_base_information = ReadDataBase()
patient_base_information = BaseLogin()
choice_int = random.randint(0, len(patient_base_information.get_login_token()))

for patient_information in patient_base_information.get_login_token():
    patient_id = patient_information['patientId']
    encounter_id = patient_information['encounterId']
    reservation_id = patient_information['id']

diagnosis_information = {"diagnosis": diagnosis_base_information.get_diagnosis_information()[choice_int][1],
                         "diagnosisId": diagnosis_base_information.get_diagnosis_information()[choice_int][0],
                         "diagnosisType": "1",
                         "remarks": "null",
                         "resId": reservation_id,
                         "priority": 1}

order_submit_information = {"id":"null",
                            "encounterId": encounter_id,
                            "itemList":[
                                {"name":"碳酸钙维生素D3片",
                                 "fullName":"碳酸钙/维生素D3片[钙尔奇D][600mg*30]",
                                 "aliasName":"碳酸钙/维生素D3片",
                                 "orderMasterType":"medicine",
                                 "orderMasterId":27179,
                                 "medicineId":3652,
                                 "instructionId":49,
                                 "frequenceId":2,"frequenceData":
                                     {"id":2,
                                      "name":"Bid",
                                      "quantity":2,
                                      "interval":1,
                                      "intervalUnit":"天",
                                      "remarks":"每日两次",
                                      "status":1,
                                      "outId":"5",
                                      "outCode":"Bid",
                                      "pinyin":"Bid",
                                      "hospitalId":1},
                                 "durationId":1,
                                 "dosage":30,
                                 "dosageUnit":"片",
                                 "usage":"口服用药",
                                 "outputUnit":"瓶[30片]",
                                 "outputPrice":29.91,
                                 "price":0.997,
                                 "dermaticFlag":0,
                                 "eqUnit":"mg",
                                 "eqQty":600,
                                 "outputFactor":30,
                                 "specs":"600mg*30",
                                 "remarks":"",
                                 "phcForm":"片剂",
                                 "tradeName":"钙尔奇D",
                                 "vendor":"惠氏制药有限公司",
                                 "unit":"片",
                                 "priorityType":"NORM",
                                 "status":"null",
                                 "quantity":1,
                                 "amount":0.997,
                                 "treatmentDays":1,
                                 "targetHisLocCode":"null",
                                 "targetHisLocName":"null"}],"remarks":"null"}




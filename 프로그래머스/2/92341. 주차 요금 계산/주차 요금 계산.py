'''
기본 3시간 5000원 
이후 10분당 600원 

입차 이후 출차 내역이 없다면 23:59 출차
18:59 ~ 23:59
34 + 300 = 334

5000 + (334-180)/10 * 600 = 14600

누적 주차 시간이 기본시간 이하 => 5000원
초과 시간이 단위 시간으로 나누어 떨어지지 않으면 => 올림
[a] => a보다 작지 않은 최소 정수

fees = [기본 시간, 기본 요금, 단위시간, 단위요금]
records = ["시각, 차량번호, IN", ]


'''

import math

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    
    car_records = {}
    for record in records:
        time, car_number, in_out = record.split()
        if car_number not in car_records:
            car_records[car_number] = []
        car_records[car_number].append((in_out, time))
        
    sorted_car_records = sorted(car_records.keys())
    
    result = []
    for car_number in sorted_car_records:
        total_time = 0
        in_time = 0
        for in_out, time in car_records[car_number]:
            if in_out == "IN":
                hour, minute = map(int,time.split(":"))
                in_time = hour * 60 + minute
            elif in_out == "OUT":
                hour, minute = map(int,time.split(":"))
                out_time = hour * 60 + minute
                total_time += out_time - in_time
                in_time = -100

        ## 마지막이 in이라면 in_time에 시간이 남아있을 것
        if in_time != -100:
            out_time = 23*60 + 59
            total_time += out_time - in_time
        
        if total_time <= base_time:
            fee = base_fee
        else:
            fee = base_fee + math.ceil((total_time - base_time)/unit_time) * unit_fee
        
        result.append(fee)
        
    return result


'''
car_records = {"3961":[
                        ["IN","16:00"],
                        ["OUT","18:00"],
                        ["IN","23:58"]
                        ],
                "0202":[
                        ["IN","16:00"],
                        ["OUT","18:00"]
                        ]
                }
'''
-- 2024-02-23 https://school.programmers.co.kr/learn/courses/30/lessons/151136
-- CAR_RENTAL_COMPAY_CAR: 대여중인 자동차 정보 테이블
-- OPTIONS: column. 키워드 리스트 'a', 'b', 'c', ...
-- CAR_RENTAL_COMPAY_CAR에서 CAR_TYPE 이 'SUV'인 차들의 평균 일일 대여 요금(DAILY_FEE의 평균값) 출력
-- 평균 일일 대여 요금 소수 첫 번째 자리에서 반올림. 컬럼명 AVERAGE_FEE 지정

SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'
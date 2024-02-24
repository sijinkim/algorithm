-- 2024-02-24 https://school.programmers.co.kr/learn/courses/30/lessons/157339
-- CAR_RENTAL_COMPANY_CAR: 대여 중인 자동차 정보 (렌탈 가능 자동차 정보)
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY: 자동차 대여 기록 정보
-- CAR_RENTAL_COMPANY_DISCOUNT_PLAN: 자동차 종류 별 대여 기간 별 할인 정책(자동차 타입과 대여 기간 타입에 따라 할인율 다르게 책정되는 시스템)

-- 자동차 종류가 '세단' 또는 'SUV'인 자동차 중, 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
-- 30일 대여 금액이 50만원 이상 200만원 미만인 자동차 정보 조회


WITH rental_pool AS (
SELECT 
    car.CAR_ID AS CAR_ID,
    car.CAR_TYPE AS CAR_TYPE,
    car.DAILY_FEE AS DAILY_FEE,
    car.DAILY_FEE * 30 AS MONTHLY_FEE
FROM CAR_RENTAL_COMPANY_CAR AS car
WHERE car.CAR_ID NOT IN (
    SELECT CAR_ID 
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS history
        WHERE history.END_DATE >= '2022-11-01' AND history.START_DATE <= '2022-12-01'
    )
    AND car.CAR_TYPE IN ('SUV', '세단')
) 
SELECT 
    rental_pool.CAR_ID AS CAR_ID,
    rental_pool.CAR_TYPE AS CAR_TYPE,
    FLOOR(rental_pool.MONTHLY_FEE * (100-discount.discount_rate) * 0.01) AS FEE
FROM rental_pool
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS discount
    ON rental_pool.CAR_TYPE = discount.CAR_TYPE
WHERE discount.DURATION_TYPE = '30일 이상'
    AND FLOOR(rental_pool.MONTHLY_FEE * (100-discount.discount_rate) * 0.01) BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC

-- '30일 이상' 정책을 가지고 있지 않는 경우에 대한 테스트 고려되지 않음
-- '30일 이상' 정책을 가지고 있는 경우는 discount_rate 적용하고,
-- '30일 이상' 정책을 가지고 있지 않은 경우는 discount_rate 미적용한 total FEE 가 출력되게 하려면?
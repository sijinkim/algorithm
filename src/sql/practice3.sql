-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/131537
-- 오프라인 테이블과 온라인 테이블에서 2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품 ID, 유저ID, 판매량 조회
-- 오프라인 테이블의 USER_ID 는 NULL로 표시
-- 판매일 기준 오름차순, 판매일 동일할 경우 상품 ID 기준 오름차순, 상품 ID도 동일할 경우 유저 ID 기준 오름차순
-- JOIN 조건 없이, 수평 통합 => UNION ALL 

SELECT 
    *
FROM (
    (SELECT 
        DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
        PRODUCT_ID, 
        USER_ID, 
        SALES_AMOUNT
    FROM ONLINE_SALE
    WHERE SALES_DATE BETWEEN '2022-03-01' and '2022-03-31')
    UNION ALL
    (SELECT
        DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
        PRODUCT_ID, 
        NULL AS USER_ID, 
        SALES_AMOUNT
    FROM OFFLINE_SALE
    WHERE SALES_DATE BETWEEN '2022-03-01' and '2022-03-31')) union_table
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC

    
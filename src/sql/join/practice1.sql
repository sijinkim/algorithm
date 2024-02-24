-- 2024-02-23 https://school.programmers.co.kr/learn/courses/30/lessons/133027
-- FIRST_HALF: 아이스크림 가게의 상반기 주문 정보
-- JULY: 아이스크림 가게의 7월 주문 정보 => DISTINCT(SHIPMENT_ID, FLAVOR)
-- 7월 총 주문량과 상반기 총 주문량을 더한 값이 큰 순서대로 상위 3개 맛 조회

SELECT
    FLAVOR
FROM(
    SELECT *
    FROM FIRST_HALF
    UNION ALL
    SELECT *
    FROM JULY
) AS union_table
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3
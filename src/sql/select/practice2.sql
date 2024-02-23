-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/131536
-- 동일한 회원이 동일한 상품을 재구매한 데이터 조회: 재구매한 회원 ID,재구매한 상품ID.
-- 회원 ID 기준 오름차순, 회원 ID 같다면 상품 ID 기준 내림차순
-- (동일 날짜, 회원ID, 상품ID) unique
SELECT
    USER_ID,
    PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID 
    HAVING COUNT(*) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC

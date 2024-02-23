-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/131112
-- FOOD_FACTORY: 식품공장 정보 테이블
-- ADDRESS 컬럼의 주소값이 '강원도'에 해당하는 경우만 조회
-- ADDRESS e.g. 강원도 정선군 남면 칠현로 679
-- LIKE '강원도%' 개선 => SQL STRING FUNCTION 사용(SUBSTRING() 사용시 idx 1부터 시작 주의)

SELECT 
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS
FROM FOOD_FACTORY
WHERE SUBSTRING(ADDRESS, 1, 3) = '강원도'
ORDER BY FACTORY_ID

SELECT 
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS
FROM FOOD_FACTORY
WHERE LEFT(ADDRESS, 3) = '강원도'
ORDER BY FACTORY_ID
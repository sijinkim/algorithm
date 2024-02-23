-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/133025
-- FIRST_HALF: 아이스크림 상반기 주문 정보 테이블
-- ICECREAM_INFO: 아이스크림 성분 정보 테이블(foreign key: FLAVOR)
-- 상반기 아이스크림 총주문량이 3000보다 높고, 주 성분이 과일인 아이스크림 맛 조회
-- 총 주문량이 큰 순서대로 정렬

SELECT F.FLAVOR
FROM FIRST_HALF F
JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
WHERE F.TOTAL_ORDER > 3000
    AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC;
-- foreign key 기준으로 table join 하여 하나의 통합 테이블 만들고,
-- WHERE 로 조건줘서 해당하는 데이터 포인트 뽑기
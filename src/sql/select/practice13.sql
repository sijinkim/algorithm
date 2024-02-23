-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/131118
-- REST_INFO: 식당 정보 테이블
-- REST_REVIEW: 식당 리뷰 정보 테이블
-- REST_INFO.ADDRESS 기준 '서울'에 위치한 식당을 출력하되, => ID
-- 위 테이블의 REST_ID 기준 REST_REVIEW 테이블과 조인
-- 위 테이블에서 REST_ID 기준 GROUP BY
-- 평균 리뷰 점수 기준 내림차순 정렬, 동일할 경우 좋아요 수 기준 내림차순 정렬

-- 서브쿼리 이용하여 '서울' 위치 테이블 추출 후, 해당 테이블에 review join
SELECT 
    seoul_rest.REST_ID,
    seoul_rest.REST_NAME,
    seoul_rest.FOOD_TYPE,
    seoul_rest.FAVORITES,
    seoul_rest.ADDRESS,
    ROUND(AVG(review.REVIEW_SCORE), 2) AS SCORE
FROM
    (SELECT 
        REST_ID, 
        REST_NAME, 
        FOOD_TYPE, 
        FAVORITES, 
        ADDRESS
        FROM REST_INFO
        WHERE LEFT(ADDRESS, 2) = '서울') AS seoul_rest
JOIN REST_REVIEW AS review
    ON seoul_rest.REST_ID = review.REST_ID
GROUP BY seoul_rest.REST_ID
ORDER BY SCORE DESC, seoul_rest.FAVORITES DESC

-- JOIN 조건으로 '서울'에 해당하는 식당 필터링
SELECT 
    I.REST_ID,
    I.REST_NAME,
    I.FOOD_TYPE,
    I.FAVORITES,
    I.ADDRESS,
    ROUND(AVG(R.REVIEW_SCORE), 2) AS SCORE
FROM REST_REVIEW R
JOIN REST_INFO I 
    ON R.REST_ID = I.REST_ID
    AND LEFT(I.ADDRESS, 2) = '서울'
GROUP BY I.REST_ID
ORDER BY SCORE DESC, I.FAVORITES DESC

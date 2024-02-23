-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/131120
-- MEMBER_PROFILE: 식당 리뷰 사이트 회원 정보
-- 생일이 3월인 여성 회원 ID, 이름, 성별, 생년월일 조회.
-- 조건) 전화번호가 NULL인 경우 출력 제외. 회원 ID를 기준으로 오름차순 정렬
SELECT 
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE 
    TLNO IS NOT NULL
    AND MONTH(DATE_OF_BIRTH) = 3
    AND GENDER = 'W'
ORDER BY MEMBER_ID

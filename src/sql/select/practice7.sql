-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/132203
-- DOCTOR: 종합병원 소속 의사 정보 테이블
-- MCDP_CD 조건에 해당하는 의사 정보 추출
SELECT 
    DR_NAME,
    DR_ID,
    MCDP_CD,
    DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME
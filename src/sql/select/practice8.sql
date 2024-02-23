-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/132201
-- PATIENT: 병원 등록 환자 정보 테이블
-- 12세 이하인 여자 환자 조회
-- 전화번호가 없는 경우(NULL), 'NONE'으로 치환 출력 => IFNULL()
SELECT
    PT_NAME,
    PT_NO,
    GEND_CD,
    AGE,
    IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME
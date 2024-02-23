-- 2024-02-23: (https://school.programmers.co.kr/learn/courses/30/lessons/59036#fn1)
-- ANIMAL_INS: 동물 보호소 동물 정보 테이블
-- 동물 보호소에 들어온 동물 중 아픈 동물(ANIMAL_INS.INTAKE_CONDITION = 'Sick')의 아이디와 이름 조회. 아이디 순으로 정렬

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID

-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/59037
-- ANIMAL_INS: 동물 보호소 동물 정보 테이블
-- 동물 보호소에 들어온 동물 중 젊은 동물(ANIMAL_INS.INTAKE_CONDITION 이 Aged가 아닌 경우)의 아이디와 이름 조회. 아이디 순으로 정렬

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID
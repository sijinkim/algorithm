-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/131535
-- USER_INFO: 의류 쇼핑몰 가입 회원 정보
-- 2021년에 가입한 회원 중 나이가 20세 이상 29세 이하인 회원이 몇 명인지 출력
SELECT COUNT(*)
FROM USER_INFO
WHERE JOINED LIKE '2021-%' and AGE LIKE '2%'
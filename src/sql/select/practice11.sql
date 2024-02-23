-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/144853
-- DATE TYPE도 string function 으로 비교 가능

SELECT 
    BOOK_ID, 
    DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE LEFT(PUBLISHED_DATE, 4) = '2021'
    AND CATEGORY = '인문'
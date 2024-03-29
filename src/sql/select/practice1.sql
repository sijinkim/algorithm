-- 2024-02-23: https://school.programmers.co.kr/learn/courses/30/lessons/164673
-- BOARD_ID 기준으로 USED_GOODS_BOARD, USED_GOODS_REPLY INNER JOIN: 게시판 글 ID 기준으로 글과 댓글 조회
-- WHERE BOARD.CREATED_DATE LIKE '2022-10%': 2022년 10월에 작성된 게시판 글들을 대상으로 해당 게시판 글의 댓글 조회
-- ORDER BY REPLY.CREATED_DATE ASC, BOARD.TITLE ASC;: 댓글 작성 일을 기준으로 오름차순 출력하고, 동일한 작성 일 가질 경우 게시판 글 제목 오름차순 출력
SELECT 
    B.TITLE, 
    B.BOARD_ID,
    R.REPLY_ID, 
    R.WRITER_ID, 
    R.CONTENTS, 
    DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_REPLY AS R
    ON B.BOARD_ID = R.BOARD_ID
WHERE B.CREATED_DATE LIKE '2022-10%'
ORDER BY R.CREATED_DATE ASC, B.TITLE ASC;

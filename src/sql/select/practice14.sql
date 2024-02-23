-- 2024-02-23 https://school.programmers.co.kr/learn/courses/30/lessons/273711
-- ITEM_INFO: 아이템 정보 테이블
-- ITEM_TREE: 아이템 관계 정보 테이블
-- 아이템의 희귀도(ITEM_INFO.RARITY)가 'RARE'인 아이템들의 다음 업그레이드 아이템 조회
-- 업그레이드 아이템의 ID, NAME, RARITY 출력
-- 아이템 ID를 기준으로 내림차순 정렬

-- ITEM_TREE.parent_ITEM_ID 기준으로 ITEM_INFO JOIN
-- ITEM_TREE.ITEM_ID 기준으로 ITEM_INFO JOIN
-- WHERE parent_ITEM_ID.RARITY = 'RARE' => 기준 아이템이 'RARE'인 경우의 row만 테이블에 남김
-- 해당 테이블에서 기준 아이템의 업그레이드 아이템, 즉 child item 정보 select.



SELECT
    tree.ITEM_ID,
    # tree.PARENT_ITEM_ID,
    # parent_info.RARITY AS parent_rarity,
    child_info.ITEM_NAME AS ITEM_NAME,
    child_info.RARITY AS RARITY
FROM ITEM_TREE AS tree
LEFT JOIN ITEM_INFO as parent_info
    ON tree.PARENT_ITEM_ID = parent_info.ITEM_ID
LEFT JOIN ITEM_INFO as child_info
    ON tree.ITEM_ID = child_info.ITEM_ID
WHERE PARENT_ITEM_ID IS NOT NULL
    AND parent_info.RARITY = "RARE"
ORDER BY ITEM_ID DESC


SELECT
    tree.ITEM_ID AS ITEM_ID,
    child_item.ITEM_NAME AS ITEM_NAME,
    child_item.RARITY AS RARITY
FROM ITEM_TREE AS tree
JOIN ITEM_INFO AS parent_item
    ON tree.PARENT_ITEM_ID = parent_item.ITEM_ID
    AND parent_item.RARITY = 'RARE'
JOIN ITEM_INFO AS child_item
    ON tree.ITEM_ID = child_item.ITEM_ID
ORDER BY ITEM_ID DESC
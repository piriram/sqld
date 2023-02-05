-- 코드를 입력하세요
SELECT COUNT(distinct(NAME))
FROM ANIMAL_INS
-- count는 null을 세지않음
where name is not null
-- WHERE 절 빼도됨
-- where name <> null
-- where name != null 은 안됨
-- 모든 NULL은 서로 다른 NULL로써, 객체처럼 각자 다른 것이라고 알고 있습니다.
-- NULL에는 comparison operator 사용을 안 하는 것이 오류가 안 나는 방법입니다.

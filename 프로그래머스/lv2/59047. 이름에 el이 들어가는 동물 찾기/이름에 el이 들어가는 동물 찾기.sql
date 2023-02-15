-- 코드를 입력하세요
-- 이번엔 소문자로 입력해보자
SELECT animal_id,name
from animal_ins
where name like "%el%"
and animal_type = "Dog"
order by name

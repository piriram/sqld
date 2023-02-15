-- SELECT ANIMAL_ID, NAME, 
-- CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
--      WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
--      ELSE 'X' END
-- FROM ANIMAL_INS;
SELECT
    animal_id,
    name,
    IF(sex_upon_intake LIKE 'Neutered%' OR sex_upon_intake LIKE 'Spayed%', 'O', 'X') AS '중성화'

FROM animal_ins
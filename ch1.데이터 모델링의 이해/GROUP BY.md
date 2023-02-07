# [MySQL]그룹화하여 데이터 조회(GROUP BY)

* 1.개념
  * 유형별로 갯수를 가져오고 싶을 때(cf.COUNT 함수는 전체 갯수만을 가져옴)
  * HAVING과 차이점
    * GROUP BY : 특정 컬럼을 그룹화
    * HAVING : 특정 컬럼을 그룹화한 결과에 조건을 건다.
    * WHERE : 그룹화 하기 전
* 2.사용법
    * 컬럼 그룹화
  ```sql
  SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할 컬럼;
  ```
    * 조건 처리 후에 컬럼 그룹화
  ```sql
  SELECT 컬럼 FROM 테이블 WHERE 조건식 GROUP BY 그룹화할 컬럼;
  ```
    * 컬럼 그룹화 후에 조건 처리
  ```sql
  SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할 컬럼 HAVING 조건식;
  ```
    * 조건 처리 후에 컬럼 그룹화 후에 조건 처리
  ```sql
  SELECT 컬럼 FROM 테이블 WHERE 조건식 GROUP BY 그룹화할 컬럼 HAVING 조건식;
  ```
    * ORDER BY가 존재하는 경우
  ```sql
  SELECT 컬럼 FROM 테이블 [WHERE 조건식]
  GROUP BY 그룹화할 컬럼 [HAVING 조건식] ORDER BY 컬럼1 [, 컬럼2, 컬럼3 ...];
  ```
* 3.예시<br>
ex.type 1 초과인, type 그룹화하여 name 갯수 조회 (조건 처리 후 컬럼 그룹화)
쿼리
```sql
SELECT type, COUNT(name) AS cnt FROM hero_collection WHERE type > 1 GROUP BY type;
```
ex.type 그룹화하여 name 갯수를 가져온 후, 그 중에 갯수가 2개 이상인 데이터 조회 (조건 처리 후에 컬럼 그룹화 후에 조건 처리)
```sql
SELECT type, COUNT(name) AS cnt FROM hero_collection GROUP BY type HAVING cnt >= 2;
```
ex.type 1 초과인, type 그룹화하여 name 갯수를 가져온 후, 그 중에 갯수가 2개 이상인 데이터 조회 (조건 처리 후에 컬럼 그룹화 후에 조건 처리)

```sql
SELECT type, COUNT(name) AS cnt FROM hero_collection WHERE type > 1 GROUP BY type HAVING cnt >= 2;
```
ex.type 1 초과인, type 그룹화하여 name 갯수를 가져온 후, 그 중에 갯수가 2개 이상인 데이터를 type 내림차순 정렬로 조회 (내림차순 정렬)
```sql
SELECT type, COUNT(name) AS cnt FROM hero_collection
WHERE type > 1 GROUP BY type HAVING cnt >= 2 ORDER BY type DESC;
```

  

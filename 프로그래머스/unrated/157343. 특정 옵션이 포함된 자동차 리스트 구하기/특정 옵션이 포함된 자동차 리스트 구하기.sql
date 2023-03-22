-- 코드를 입력하세요
SELECT
    car_id, car_type, daily_fee, options
FROM
    car_rental_company_car
WHERE
    locate('네비게이션', options)
ORDER BY
    car_id desc
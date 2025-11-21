SELECT 
`How much would you be willing to pay for a repair compared to the cost of replacing your phone with a new one?` AS amount,
COUNT(`How much would you be willing to pay for a repair compared to the cost of replacing your phone with a new one?`) AS total 
FROM survey 
GROUP BY amount;
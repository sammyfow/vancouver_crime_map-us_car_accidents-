SELECT 
`How much would you be willing to pay for a repair compared to the cost of replacing your phone with a new one?` AS amount,
COUNT(`How much would you be willing to pay for a repair compared to the cost of replacing your phone with a new one?`) AS total 
FROM survey WHERE
`If mobile devices were easier and cheaper to repair, how likely would you be to keep your device longer before replacing it?`
IN ('Much more likely', 'Somewhat more likely')
GROUP BY amount;

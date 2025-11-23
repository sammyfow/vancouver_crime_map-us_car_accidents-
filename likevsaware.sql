SELECT 
`If mobile devices were easier and cheaper to repair, how likely would you be to keep your device longer before replacing it?` AS amount,
COUNT(`If mobile devices were easier and cheaper to repair, how likely would you be to keep your device longer before replacing it?`) AS total 
FROM survey WHERE
`Have you heard of the "Right to Repair" movement?` = 'Yes'
GROUP BY amount;
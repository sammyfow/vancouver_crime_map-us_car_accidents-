SELECT 
`How often do you typically replace your mobile phone?` AS amount,
COUNT(`How often do you typically replace your mobile phone?`) AS total 
FROM survey 
GROUP BY amount;
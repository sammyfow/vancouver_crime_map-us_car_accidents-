SELECT 
`How often do you typically replace your mobile phone?` AS amount,
COUNT(`How often do you typically replace your mobile phone?`) AS total 
FROM survey WHERE
`If mobile devices were easier and cheaper to repair, how likely would you be to keep your device longer before replacing it?`
IN ('Much more likely', 'Somewhat more likely')
GROUP BY amount;
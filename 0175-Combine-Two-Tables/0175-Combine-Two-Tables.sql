SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId
UNION
SELECT firstName, lastName, city, state
FROM Person
RIGHT JOIN Address ON Person.personId = Address.personId
WHERE firstName IS NOT NULL;
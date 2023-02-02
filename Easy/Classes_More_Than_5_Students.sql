# James Crisp

# 596. Class More Than 5 Students

SELECT class, COUNT(class) as classc
FROM Courses
WHERE classc > 4
ORDER BY student;
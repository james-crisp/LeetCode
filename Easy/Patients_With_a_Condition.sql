# James Crisp
# Dec 30, 2022

# 1527. Patients With a Condition

# Write your MySQL query statement below

SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%';
## Question 2

The relational database approach is a good approach because the data in cell-count.csv is highly structured.
 
Here is a list of some advantages to the relational database structure.

1. Data Integrity
   - Relational databases enforce data integrity through constraints like primary keys and foreign keys. This ensures that data remains consistent and accurate (e.g., every sample is linked to a valid subject and project).

3. Scalability
   - Databases are designed to handle large datasets efficiently. As the number of projects, subjects, and samples grows, a database can scale to accommodate the increasing volume of data without performance degradation.

4. Efficient Querying
   - Using SQL, you can perform complex queries to filter, aggregate, and analyze data. For example:
     - Compare responders vs. non-responders.
     - Track changes in cell counts over time.
     - Calculate average relative frequencies for specific conditions or treatments.


## Question 3
```sql
SELECT 
    condition, 
    COUNT(subject_id) AS subject_count
FROM 
    Subjects
GROUP BY 
    condition
ORDER BY 
    subject_count DESC;
```
## Question 4
```sql
SELECT 
    s.sample_id,
    s.sample_type,
    s.time_from_treatment,
    sub.subject_id,
    sub.condition,
    sub.treatment
FROM 
    Samples s
JOIN 
    Subjects sub ON s.subject_id = sub.subject_id
WHERE 
    sub.condition = 'melanoma'
    AND s.sample_type = 'PBMC'
    AND s.time_from_treatment = 0
    AND sub.treatment = 'tr1';
```
## Question 5

### a. 
```sql
WITH FilteredSamples AS (
    SELECT 
        s.sample_id,
        s.project_id,
        s.sample_type,
        s.time_from_treatment,
        sub.subject_id,
        sub.condition,
        sub.treatment
    FROM 
        Samples s
    JOIN 
        Subjects sub ON s.subject_id = sub.subject_id
    WHERE 
        sub.condition = 'melanoma'
        AND s.sample_type = 'PBMC'
        AND s.time_from_treatment = 0
        AND sub.treatment = 'tr1'
)
SELECT 
    fs.project_id,
    COUNT(fs.sample_id) AS sample_count
FROM 
    FilteredSamples fs
GROUP BY 
    fs.project_id
ORDER BY 
    sample_count DESC;
```
### b. 
```sql
WITH FilteredSamples AS (
    SELECT 
        s.sample_id,
        s.sample_type,
        s.time_from_treatment,
        sub.subject_id,
        sub.condition,
        sub.treatment,
        sub.response_status
    FROM 
        Samples s
    JOIN 
        Subjects sub ON s.subject_id = sub.subject_id
    WHERE 
        sub.condition = 'melanoma'
        AND s.sample_type = 'PBMC'
        AND s.time_from_treatment = 0
        AND sub.treatment = 'tr1'
)
SELECT 
    fs.response_status,
    COUNT(fs.sample_id) AS sample_count
FROM 
    FilteredSamples fs
GROUP BY 
    fs.response_status
ORDER BY 
    sample_count DESC;
```
### c. 
```sql

WITH FilteredSamples AS (
    SELECT 
        s.sample_id,
        s.sample_type,
        s.time_from_treatment,
        sub.subject_id,
        sub.condition,
        sub.treatment,
        sub.gender
    FROM 
        Samples s
    JOIN 
        Subjects sub ON s.subject_id = sub.subject_id
    WHERE 
        sub.condition = 'melanoma'
        AND s.sample_type = 'PBMC'
        AND s.time_from_treatment = 0
        AND sub.treatment = 'tr1'
)
SELECT 
    fs.gender,
    COUNT(fs.sample_id) AS sample_count
FROM 
    FilteredSamples fs
GROUP BY 
    fs.gender
ORDER BY 
    sample_count DESC;
```
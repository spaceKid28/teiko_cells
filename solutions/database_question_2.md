 The relational database approach is a good approach because the data in cell-count.csv is highly structured. 
 
 Here is a list of some advantages to the relational database structure.

1. **Data Organization and Structure**
   - A database provides a structured way to store and organize data, ensuring that related information (e.g., projects, subjects, samples, and cell counts) is logically connected and easy to access.

2. **Data Integrity**
   - Relational databases enforce data integrity through constraints like primary keys and foreign keys. This ensures that data remains consistent and accurate (e.g., every sample is linked to a valid subject and project).

3. **Scalability**
   - Databases are designed to handle large datasets efficiently. As the number of projects, subjects, and samples grows, a database can scale to accommodate the increasing volume of data without performance degradation.

4. **Efficient Querying**
   - Using SQL, you can perform complex queries to filter, aggregate, and analyze data. For example:
     - Compare responders vs. non-responders.
     - Track changes in cell counts over time.
     - Calculate average relative frequencies for specific conditions or treatments.

5. **Data Reusability**
   - Once the data is stored in a database, it can be reused for multiple analyses without needing to reload or preprocess the data repeatedly. This saves time and effort for future analytics.

6. **Data Consistency Across Projects**
   - A database ensures that data is stored consistently across hundreds of projects and thousands of samples. For example, all projects can follow the same schema, making it easier to combine and compare data.

7. **Support for Advanced Analytics**
   - By storing data in a structured format, a database makes it easier to integrate with analytics tools (e.g., Python, R, or BI tools) for advanced statistical analysis, machine learning, or visualization.

8. **Data Security**
   - Databases provide mechanisms to control access to data, ensuring that only authorized users can view or modify sensitive information (e.g., patient data).

9. **Versioning and Auditing**
   - Databases can track changes to data over time, making it possible to audit or version datasets. This is particularly useful for scientific research, where reproducibility is critical.

10. **Flexibility for Future Needs**
    - A well-designed database schema can be extended to include new data types or analyses without disrupting the existing structure. For example, you can add new cell populations or statistical results as new research questions arise.

---

### Conclusion
Capturing this information in a database provides a scalable, efficient, and reliable way to manage structured data, enabling advanced analytics and ensuring data integrity across large-scale projects.

## Question 3

SELECT 
    condition, 
    COUNT(subject_id) AS subject_count
FROM 
    Subjects
GROUP BY 
    condition
ORDER BY 
    subject_count DESC;
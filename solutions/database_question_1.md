# Database Schema for Cell Count Data

I would use a relational database approach, as follows.

---

## A. Projects Table
Stores information about each project.

| Column Name   | Data Type | Description                          |
|---------------|-----------|--------------------------------------|
| `project_id`  | INT (PK)  | Unique identifier for the project.   |
| `project_name`| VARCHAR   | Name of the project.                 |
| `description` | TEXT      | Description of the project.          |
| `created_at`  | TIMESTAMP | Timestamp when the project was created. |

---

## B. Subjects Table
Stores information about each subject (e.g., patients or individuals).

| Column Name   | Data Type | Description                              |
|---------------|-----------|------------------------------------------|
| `subject_id`  | INT (PK)  | Unique identifier for the subject.       |
| `project_id`  | INT (FK)  | Foreign key linking to the Projects table. |
| `age`         | INT       | Age of the subject.                      |
| `sex`         | VARCHAR(1)| Sex of the subject (`M` or `F`).         |
| `condition`   | VARCHAR   | Condition of the subject (e.g., melanoma). |
| `treatment`   | VARCHAR   | Treatment type (e.g., `tr1`).            |
| `response`    | VARCHAR(1)| Response to treatment (`y` or `n`).      |

---

## C. Samples Table
Stores information about each sample collected from subjects.

| Column Name           | Data Type | Description                              |
|-----------------------|-----------|------------------------------------------|
| `sample_id`           | INT (PK)  | Unique identifier for the sample.        |
| `subject_id`          | INT (FK)  | Foreign key linking to the Subjects table. |
| `sample_type`         | VARCHAR   | Type of sample (e.g., PBMC).             |
| `time_from_treatment` | FLOAT     | Time from treatment start (in days).     |
| `created_at`          | TIMESTAMP | Timestamp when the sample was collected. |

---

## D. Cell Counts Table
Stores the raw cell counts for each sample.

| Column Name   | Data Type | Description                              |
|---------------|-----------|------------------------------------------|
| `cell_count_id` | INT (PK) | Unique identifier for the cell count record. |
| `sample_id`   | INT (FK)  | Foreign key linking to the Samples table. |
| `b_cell`      | INT       | Count of B cells.                        |
| `cd8_t_cell`  | INT       | Count of CD8 T cells.                    |
| `cd4_t_cell`  | INT       | Count of CD4 T cells.                    |
| `nk_cell`     | INT       | Count of NK cells.                       |
| `monocyte`    | INT       | Count of monocytes.                      |
| `total_count` | INT       | Total count of all cells.                |

---

## E. Relative Frequencies Table
Stores the calculated relative frequencies for each cell type.

| Column Name             | Data Type | Description                              |
|-------------------------|-----------|------------------------------------------|
| `relative_freq_id`      | INT (PK)  | Unique identifier for the relative frequency record. |
| `sample_id`             | INT (FK)  | Foreign key linking to the Samples table. |
| `b_cell_percentage`     | FLOAT     | Relative frequency of B cells.           |
| `cd8_t_cell_percentage` | FLOAT     | Relative frequency of CD8 T cells.       |
| `cd4_t_cell_percentage` | FLOAT     | Relative frequency of CD4 T cells.       |
| `nk_cell_percentage`    | FLOAT     | Relative frequency of NK cells.          |
| `monocyte_percentage`   | FLOAT     | Relative frequency of monocytes.         |

---

## 6. Analytics Table
Stores results of statistical analyses (e.g., t-tests) for comparisons between groups.

| Column Name   | Data Type | Description                              |
|---------------|-----------|------------------------------------------|
| `analysis_id` | INT (PK)  | Unique identifier for the analysis.      |
| `project_id`  | INT (FK)  | Foreign key linking to the Projects table. |
| `population`  | VARCHAR   | Cell population analyzed (e.g., `b_cell_percentage`). |
| `statistic`   | FLOAT     | Test statistic (e.g., t-statistic).      |
| `p_value`     | FLOAT     | P-value of the test.                     |
| `comparison`  | VARCHAR   | Description of the comparison (e.g., responders vs. non-responders). |

---

### Notes:
- **Primary Key (PK)**: Uniquely identifies each record in the table.
- **Foreign Key (FK)**: Links a record in one table to a record in another table.
- This schema is designed to scale for hundreds of projects, thousands of samples, and various types of analyses.
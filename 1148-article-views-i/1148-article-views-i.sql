# Write your MySQL query statement below
SELECT DISTINCT author_id AS 'id'
FROM Views
Where author_id = Viewer_id
ORDER BY author_id ASC

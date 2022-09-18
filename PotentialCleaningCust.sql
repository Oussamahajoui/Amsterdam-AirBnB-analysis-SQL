-- Gathering list of listings with mentions of 'dirty' more than three times in their reviews
-- These will be good potential customers to target for a cleaning service business

SELECT host_id, host_url, host_name, COUNT(*) AS num_dirty_reviews FROM reviews INNER JOIN listings ON reviews.listing_id = listings.id
WHERE comments LIKE "%dirty%"
GROUP BY host_id, host_url, host_name 
Having num_dirty_reviews > 3
ORDER BY num_dirty_reviews DESC;
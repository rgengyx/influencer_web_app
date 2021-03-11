USE influencer;

SELECT id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
FROM latin_product_review
INNER JOIN latin_product_map
ON latin_product_review.review_order = latin_product_map.review_order
WHERE id = 1;

SELECT id, product1, product2, product3, product4, product5, product6, product7, product8, product9, product10
FROM latin_product_review
INNER JOIN latin_product
ON latin_product_review.product_order = latin_product.combo
WHERE id = 1;

SELECT *
FROM latin_review;
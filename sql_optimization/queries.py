"""
SQL Optimization Exercises
==========================

This module contains five SQL queries that work correctly but suffer from
serious performance and scalability problems.

Your task for each query
------------------------
1. Identify every performance issue present.
2. Rewrite the query (or the surrounding Python code) so it is correct,
   efficient, and production-ready.
3. Briefly explain *why* each change improves performance.

All queries use the schema defined in models.py.
Queries are expressed as plain Python strings — no real DB connection needed.
"""

from typing import Any, List


# ---------------------------------------------------------------------------
# Query 1 — Active users and their order count
#
# Goal: return a list of all active users together with the total number of
#       orders each user has placed, ordered by order count descending.
# ---------------------------------------------------------------------------

def query_1_get_active_users_with_orders(db: Any) -> List[dict]:
    """
    Retrieve every active user and how many orders they have placed.
    """
    active_users_query = """
        SELECT *
        FROM users
        WHERE status = 'active'
    """
    users = db.execute(active_users_query).fetchall()

    result = []
    for user in users:
        order_count_query = f"""
            SELECT COUNT(*)
            FROM orders
            WHERE user_id = {user['id']}
        """
        count = db.execute(order_count_query).fetchone()[0]
        result.append({"user": user, "order_count": count})

    result.sort(key=lambda x: x["order_count"], reverse=True)
    return result


# ---------------------------------------------------------------------------
# Query 2 — Top-selling products
#
# Goal: return the 10 products with the highest total revenue
#       (sum of quantity * unit_price across all paid orders),
#       including the product name and category name.
# ---------------------------------------------------------------------------

def query_2_top_selling_products(db: Any) -> List[dict]:
    """
    Find the 10 best-selling products by total revenue from paid orders.
    """
    query = """
        SELECT DISTINCT
            p.id,
            p.name,
            p.price,
            p.description,
            p.stock,
            c.id         AS category_id,
            c.name       AS category_name,
            c.parent_id,
            (
                SELECT SUM(oi.quantity * oi.unit_price)
                FROM order_items oi
                INNER JOIN orders o ON oi.order_id = o.id
                WHERE oi.product_id = p.id
                  AND o.status = 'paid'
            ) AS total_revenue
        FROM products p
        INNER JOIN categories c ON p.category_id = c.id
        ORDER BY total_revenue DESC
        LIMIT 10
    """
    rows = db.execute(query).fetchall()
    return [dict(row) for row in rows]


# ---------------------------------------------------------------------------
# Query 3 — Users who purchased from a specific category
#
# Goal: return the email and name of every active user who has placed at
#       least one paid order that contains a product from a given category.
# ---------------------------------------------------------------------------

def query_3_users_who_purchased_category(db: Any, category_name: str) -> List[dict]:
    """
    List active users who have bought at least one product in `category_name`.
    """
    query = f"""
        SELECT u.email, u.name
        FROM users u
        WHERE u.status = 'active'
          AND u.id IN (
              SELECT o.user_id
              FROM orders o
              WHERE o.status = 'paid'
                AND o.id IN (
                    SELECT oi.order_id
                    FROM order_items oi
                    WHERE oi.product_id IN (
                        SELECT p.id
                        FROM products p
                        WHERE p.category_id IN (
                            SELECT c.id
                            FROM categories c
                            WHERE c.name = '{category_name}'
                        )
                    )
                )
          )
    """
    rows = db.execute(query).fetchall()
    return [dict(row) for row in rows]


# ---------------------------------------------------------------------------
# Query 4 — Product keyword search
#
# Goal: return all products whose name or description contains a given
#       keyword, including their category name, sorted by price ascending.
# ---------------------------------------------------------------------------

def query_4_search_products_by_keyword(db: Any, keyword: str) -> List[dict]:
    """
    Full-text-like search for products matching a keyword in name or description.
    """
    query = f"""
        SELECT *
        FROM products p, categories c
        WHERE p.category_id = c.id
          AND (
              p.name        LIKE '%{keyword}%'
              OR p.description LIKE '%{keyword}%'
          )
        ORDER BY p.price ASC
    """
    rows = db.execute(query).fetchall()
    return [dict(row) for row in rows]


# ---------------------------------------------------------------------------
# Query 5 — Monthly revenue report
#
# Goal: return the total revenue per month for the last 12 months,
#       considering only paid orders, with month formatted as 'YYYY-MM'.
#       The result should be paginated: return page `page` with `page_size`
#       rows per page.
# ---------------------------------------------------------------------------

def query_5_monthly_revenue_report(db: Any, page: int = 1, page_size: int = 12) -> List[dict]:
    """
    Compute monthly revenue for the last 12 months with offset-based pagination.
    """
    offset = (page - 1) * page_size

    query = f"""
        SELECT
            DATE_FORMAT(o.created_at, '%Y-%m') AS month,
            SUM(o.total)                        AS revenue
        FROM orders o
        WHERE o.status = 'paid'
          AND o.created_at >= DATE_SUB(NOW(), INTERVAL 12 MONTH)
        GROUP BY DATE_FORMAT(o.created_at, '%Y-%m')
        ORDER BY month DESC
        LIMIT {page_size} OFFSET {offset}
    """
    rows = db.execute(query).fetchall()
    return [dict(row) for row in rows]

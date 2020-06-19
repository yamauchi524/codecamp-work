/*15章*/
/*1.発注に関して、customer_idとgoods_idを除く全情報を取得*/
/*order customer order_detail goods*/
SELECT order_table.order_id,order_table.order_date,customer_table.customer_name,customer_table.address,customer_table.phone_number,order_table.payment,goods_table.goods_name,goods_table.price,order_detail_table.quantity FROM order_table JOIN customer_table ON order_table.customer_id = customer_table.customer_id JOIN order_detail_table ON order_table.order_id = order_detail_table.order_id JOIN goods_table ON order_detail_table.goods_id = goods_table.goods_id;

/*2.佐藤一郎さんの発注した商品情報を取得*/
SELECT order_table.order_id,order_table.order_date,customer_table.customer_name,goods_table.goods_name,goods_table.price,order_detail_table.quantity FROM order_table JOIN customer_table ON order_table.customer_id = customer_table.customer_id JOIN order_detail_table ON order_table.order_id = order_detail_table.order_id JOIN goods_table ON order_detail_table.goods_id = goods_table.goods_id WHERE customer_table.customer_id = 1;

/*コーラの売上情報を取得*/
/*order_table order_detail_table goods_table*/
SELECT goods_table.goods_name,goods_table.price,order_detail_table.quantity,order_table.order_date FROM order_table JOIN order_detail_table ON order_table.order_id = order_detail_table.order_id JOIN goods_table ON order_detail_table.goods_id = goods_table.goods_id WHERE goods_table.goods_id = 1;

/*1回あたりの購入数が多い順に全商品の売上情報を取得*/
/*LEFT JOIN*/
SELECT goods_table.goods_name,goods_table.price,order_detail_table.quantity, order_table.order_date FROM goods_table LEFT JOIN order_detail_table ON order_detail_table.goods_id = goods_table.goods_id LEFT JOIN order_table ON order_detail_table.order_id = order_table.order_id ORDER BY order_detail_table.quantity DESC;

/*16章*/
/*顧客毎の発注回数を取得し、名前と合わせて表示してください。*/
/*COUNT*/
SELECT customer_table.customer_name, COUNT(customer_name) AS '発注回数' FROM order_table JOIN customer_table ON order_table.customer_id = customer_table.customer_id GROUP BY customer_name;

/*値段が100円の商品に関して商品毎の売上数量を取得し、商品名と合わせて表示してください。*/
/*SUM*/
SELECT goods_table.goods_name, SUM(quantity) AS '売上数量' FROM order_detail_table JOIN goods_table ON order_detail_table.goods_id = goods_table.goods_id WHERE goods_table.price = 100 GROUP BY order_detail_table.goods_id;


/*顧客毎の発注した全商品の合計金額を取得し、名前と合わせて表示してください。*/
SELECT customer_table.customer_name,SUM(goods_table.price * order_detail_table.quantity) AS '合計金額' FROM order_table JOIN customer_table ON order_table.customer_id = customer_table.customer_id JOIN order_detail_table ON order_table.order_id = order_detail_table.order_id JOIN goods_table ON order_detail_table.goods_id = goods_table.goods_id GROUP BY customer_table.customer_name;

/*メモ*/
/*全商品の売上情報*/
SELECT goods_table.price,order_detail_table.quantity, order_table.order_date FROM goods_table LEFT JOIN order_detail_table ON order_detail_table.goods_id = goods_table.goods_id LEFT JOIN order_table ON order_detail_table.order_id = order_table.order_id;

/*「単価(price) * 数量(quiantity)」により、合計金額を取得*/
SELECT
  goods_table.goods_id,
  goods_table.goods_name,
  goods_table.price,
  order_detail_table.quantity,
  goods_table.price * order_detail_table.quantity AS total
FROM
  goods_table LEFT JOIN order_detail_table
    ON order_detail_table.goods_id = goods_table.goods_id;


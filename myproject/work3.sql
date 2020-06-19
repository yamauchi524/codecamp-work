/* レコードの更新
UPDATE [テーブル名] SET [カラム名] = [設定する値] WHERE [条件];
UPDATE goods_table SET price = 300 WHERE goods_id = 3;

/* レコードの削除
DELETE FROM [テーブル名] WHERE [条件];
DELETE FROM goods_table WHERE goods_id = 2;

/* 課題3
/* emp_tableでemp_idが1のjobをCTOに変更
UPDATE emp_table SET job = 'CTO' WHERE emp_id = 1;

/* emp_tableでageが40以上のレコードを削除
DELETE FROM emp_table WHERE age >= 40;
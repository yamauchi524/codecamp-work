/*メモ
/*前方一致
WHERE column LIKE ‘abc%’
/*後方一致
WHERE column LIKE ‘%abc’
/*部分一致 or 中間一致
WHERE column LIKE ‘%abc%’
/*完全一致
WHERE column = ‘abc’

/*課題2
/*goods_tableでpriceが500以下のデータを表示
SELECT * FROM goods_table WHERE price <= 500;

/*character_tableでprefが「県」で終わるデータのcharacter_idとcharacter_nameを表示
SELECT character_id, character_name FROM character_table WHERE pref LIKE '__県';

/*emp_tableでjobがclerkのemp_idとageを表示
SELECT emp_id, age FROM emp_table WHERE job LIKE 'clerk';

/*emp_tableでjobがanalyst または ageが20以上25以下のemp_idとemp_nameを表示
SELECT emp_id, emp_name FROM emp_table WHERE job LIKE 'analyst' OR age BETWEEN 20 AND 25;

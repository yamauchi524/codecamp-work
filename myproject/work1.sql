/*goods_table
CREATE TABLE goods_table(
    goods_id INT AUTO_INCREMENT,
    goods_name VARCHAR(100),
    price INT,
    PRIMARY KEY (goods_id)
);

INSERT INTO goods_table(goods_id, goods_name, price) VALUES (1, 'コーラ', 100);
INSERT INTO goods_table(goods_id, goods_name, price) VALUES (2, 'USB', 2000);
INSERT INTO goods_table(goods_id, goods_name, price) VALUES (3, '傘', 500);
INSERT INTO goods_table(goods_id, goods_name, price) VALUES (4, 'お茶', 100);

/* good_tableのデータ検索
SELECT goods_id, goods_name FROM goods_table;

/*課題1
/*character_table
CREATE TABLE goods_table(
    character_id INT AUTO_INCREMENT,
    character_name VARCHAR(100),
    perf VARCHAR(10),
    PRIMARY KEY (character_id)
);

/*haracter_tableにデータをいれる
INSERT INTO caracter_table(character_id, character_name, perf) VALUES (1, 'ふなっしー', '千葉県');
INSERT INTO caracter_table(character_id, character_name, perf) VALUES (2, 'ひこにゃん', '滋賀県');
INSERT INTO character_table(character_id, character_name, perf) VALUES (3, 'まりもっこり', '北海道');

/* character_tableのデータ検索
SELECT * FROM character_table;

/*emp_table
CREATE TABLE emp_table(
    emp_id INT AUTO_INCREMENT,
    emp_name VARCHAR(100),
    job VARCHAR(100),
    age INT,
    PRIMARY KEY (emp_id)
);

/*emp_tableにデータをいれる
INSERT INTO emp_table(emp_id, emp_name, job, age) VALUES (1, '山田太郎', 'manager', 50);
INSERT INTO emp_table(emp_id, emp_name, job, age) VALUES (2, '伊藤静香', 'manager', 45);
INSERT INTO emp_table(emp_id, emp_name, job, age) VALUES (3, '鈴木三郎', 'analyst', 30);
INSERT INTO emp_table(emp_id, emp_name, job, age) VALUES (4, '山田花子', 'clerk', 24);

/*emp_tableのデータ検索
SELECT emp_id, emp_name FROM emp_table;

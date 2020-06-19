/*ひとこと掲示板のテーブル
CREATE TABLE bbs_table(
    bbs_id INT AUTO_INCREMENT,
    bbs_name VARCHAR(20),
    comment VARCHAR(100),
    bbs_date DATETIME,
    PRIMARY KEY(bbs_id)
);
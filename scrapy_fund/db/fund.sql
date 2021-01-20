/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost
 Source Database       : fund

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : utf-8

 Date: 01/20/2021 19:32:08 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `dim_day`
-- ----------------------------
DROP TABLE IF EXISTS `dim_day`;
CREATE TABLE `dim_day` (
  `DAY_ID` varchar(10) NOT NULL,
  `DAY_SHORT_DESC` varchar(14) DEFAULT NULL,
  `DAY_LONG_DESC` varchar(100) DEFAULT NULL,
  `WEEK_ID` varchar(100) DEFAULT NULL,
  `WEEK_LONG_DESC` varchar(100) DEFAULT NULL,
  `DAY_OF_WEEK` int DEFAULT NULL,
  `MONTH_ID` varchar(100) DEFAULT NULL,
  `MONTH_SHORT_DESC` varchar(100) DEFAULT NULL,
  `MONTH_LONG_DESC` varchar(100) DEFAULT NULL,
  `QUARTER_ID` varchar(100) DEFAULT NULL,
  `QUARTER_LONG_DESC` varchar(100) DEFAULT NULL,
  `YEAR_ID` varchar(100) DEFAULT NULL,
  `YEAR_LONG_DESC` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`DAY_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Table structure for `dingtou_rank`
-- ----------------------------
DROP TABLE IF EXISTS `dingtou_rank`;
CREATE TABLE `dingtou_rank` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(11) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `net_asset_value` double DEFAULT NULL,
  `oneyear` double DEFAULT NULL,
  `twoyear` double DEFAULT NULL,
  `threeyear` double DEFAULT NULL,
  `fiveyear` double DEFAULT NULL,
  `grade_no` int DEFAULT NULL,
  `category` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5762 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Table structure for `etf_rank`
-- ----------------------------
DROP TABLE IF EXISTS `etf_rank`;
CREATE TABLE `etf_rank` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(20) DEFAULT NULL,
  `fund_name` varchar(50) DEFAULT NULL,
  `fund_name_abbr` varchar(200) DEFAULT NULL,
  `cal_date` varchar(20) DEFAULT NULL,
  `net_asset_value` float(10,4) DEFAULT NULL,
  `accumulative` float(10,4) DEFAULT NULL,
  `oneweek` float(10,4) DEFAULT NULL,
  `onemonth` float(10,4) DEFAULT NULL,
  `threemonth` float(10,4) DEFAULT NULL,
  `sixmonth` float(10,4) DEFAULT NULL,
  `oneyear` float(10,4) DEFAULT NULL,
  `twoyear` float(10,4) DEFAULT NULL,
  `threeyear` float(10,4) DEFAULT NULL,
  `thisyear` float(10,4) DEFAULT NULL,
  `setup` float DEFAULT NULL,
  `setup_date` date DEFAULT NULL,
  `category` varchar(10) DEFAULT NULL,
  `score` double(255,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=354 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `fund_gp_percent`
-- ----------------------------
DROP TABLE IF EXISTS `fund_gp_percent`;
CREATE TABLE `fund_gp_percent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(20) DEFAULT NULL,
  `fund_name` varchar(100) DEFAULT NULL,
  `fund_scale` varchar(100) DEFAULT NULL,
  `gp_name` varchar(50) DEFAULT NULL,
  `gp_percent` varchar(100) DEFAULT NULL,
  `_timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49041 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Table structure for `fund_id`
-- ----------------------------
DROP TABLE IF EXISTS `fund_id`;
CREATE TABLE `fund_id` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(100) DEFAULT NULL,
  `fund_name` varchar(100) DEFAULT NULL,
  `info_url` varchar(100) DEFAULT NULL,
  `topic_url` varchar(100) DEFAULT NULL,
  `archive_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11634 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `fund_ids`
-- ----------------------------
DROP TABLE IF EXISTS `fund_ids`;
CREATE TABLE `fund_ids` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(100) DEFAULT NULL,
  `fund_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8192 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `fund_manager`
-- ----------------------------
DROP TABLE IF EXISTS `fund_manager`;
CREATE TABLE `fund_manager` (
  `id` int NOT NULL AUTO_INCREMENT,
  `manager_id` varchar(255) DEFAULT NULL,
  `manager_name` varchar(255) DEFAULT NULL,
  `company_id` int DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `fund_id` varchar(255) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `work_day` int DEFAULT NULL,
  `scale` varchar(255) DEFAULT NULL,
  `now_best_fund_id` varchar(255) DEFAULT NULL,
  `now_best_fund_name` varchar(255) DEFAULT NULL,
  `now_best_fund_yields` double(255,2) DEFAULT NULL,
  `his_best_fund_yields` varchar(255) DEFAULT NULL,
  `star` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15479 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Table structure for `fund_rank`
-- ----------------------------
DROP TABLE IF EXISTS `fund_rank`;
CREATE TABLE `fund_rank` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(20) DEFAULT NULL,
  `fund_name` varchar(50) DEFAULT NULL,
  `fund_name_abbr` varchar(200) DEFAULT NULL,
  `cal_date` varchar(20) DEFAULT NULL,
  `net_asset_value` float(10,4) DEFAULT NULL,
  `accumulative` float(10,4) DEFAULT NULL,
  `oneday` float(10,4) DEFAULT NULL,
  `oneweek` float(10,4) DEFAULT NULL,
  `onemonth` float(10,4) DEFAULT NULL,
  `threemonth` float(10,4) DEFAULT NULL,
  `sixmonth` float(10,4) DEFAULT NULL,
  `oneyear` float(10,4) DEFAULT NULL,
  `twoyear` float(10,4) DEFAULT NULL,
  `threeyear` float(10,4) DEFAULT NULL,
  `thisyear` float(10,4) DEFAULT NULL,
  `setup` float(10,4) DEFAULT NULL,
  `category` varchar(10) DEFAULT NULL,
  `score` double(255,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8602 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Table structure for `fund_value`
-- ----------------------------
DROP TABLE IF EXISTS `fund_value`;
CREATE TABLE `fund_value` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(255) DEFAULT NULL,
  `fsrq` varchar(255) DEFAULT NULL,
  `dwjz` double DEFAULT NULL,
  `ljjz` double DEFAULT NULL,
  `jzzzl` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=881 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
--  Procedure structure for `f_dim_day`
-- ----------------------------
DROP PROCEDURE IF EXISTS `f_dim_day`;
delimiter ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `f_dim_day`(in start_date VARCHAR(20),in date_count int)
begin  
declare i int;  
set i=0;  
DELETE from dim_day;  
while i < date_count do  
INSERT into dim_day  
(DAY_ID,DAY_SHORT_DESC,DAY_LONG_DESC,WEEK_ID,WEEK_LONG_DESC,DAY_OF_WEEK,MONTH_ID,MONTH_SHORT_DESC,MONTH_LONG_DESC,QUARTER_ID,QUARTER_LONG_DESC,YEAR_ID,YEAR_LONG_DESC)  
SELECT  
REPLACE(start_date,'-','') DAY_ID,  
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y-%m-%d') DAY_SHORT_DESC,  
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y年%m月%d日') DAY_LONG_DESC,  
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y%u') WEEK_ID,  
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y年第%u周') WEEK_LONG_DESC,  
DAYOFWEEK(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'))-1 DAY_OF_WEEK,
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y%m') MONTH_ID,  
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y-%m') MONTH_SHORT_DESC,  
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y年第%m月') MONTH_LONG_DESC,  
CONCAT(DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y'),quarter(STR_TO_DATE( start_date,'%Y-%m-%d %H:%i:%s'))) QUARTER_ID,  
CONCAT(DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y'),'年第',quarter(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s')),'季度') QUARTER_LONG_DESC,  
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y') YEAR_ID,  
DATE_FORMAT(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),'%Y年') YEAR_LONG_DESC  
from dual;  
set i=i+1;  
set start_date = DATE_FORMAT(date_add(STR_TO_DATE(start_date,'%Y-%m-%d %H:%i:%s'),interval 1 day),'%Y-%m-%d');  
end while;  
end
 ;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;

/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80003
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 80003
File Encoding         : 65001

Date: 2020-11-08 22:44:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for fund_info
-- ----------------------------
DROP TABLE IF EXISTS `fund_info`;
CREATE TABLE `fund_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(20) DEFAULT NULL,
  `fund_name` varchar(50) DEFAULT NULL,
  `fund_name_abbr` varchar(200) DEFAULT NULL,
  `cal_date` varchar(20) DEFAULT NULL,
  `net_asset_value` float(100,4) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=8239 DEFAULT CHARSET=utf8;

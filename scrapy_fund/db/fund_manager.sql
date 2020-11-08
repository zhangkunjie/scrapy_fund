/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80003
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 80003
File Encoding         : 65001

Date: 2020-11-08 22:44:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for fund_manager
-- ----------------------------
DROP TABLE IF EXISTS `fund_manager`;
CREATE TABLE `fund_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` varchar(255) DEFAULT NULL,
  `manager_name` varchar(255) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `fund_id` varchar(255) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `work_day` int(11) DEFAULT NULL,
  `scale` varchar(255) DEFAULT NULL,
  `now_best_fund_id` varchar(255) DEFAULT NULL,
  `now_best_fund_name` varchar(255) DEFAULT NULL,
  `now_best_fund_yields` varchar(255) DEFAULT NULL,
  `his_best_fund_yields` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14817 DEFAULT CHARSET=utf8;

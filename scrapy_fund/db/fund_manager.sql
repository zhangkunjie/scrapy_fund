/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost
 Source Database       : test

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : utf-8

 Date: 11/06/2020 10:13:50 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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
  `now_best_fund_yields` varchar(255) DEFAULT NULL,
  `his_best_fund_yields` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14807 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

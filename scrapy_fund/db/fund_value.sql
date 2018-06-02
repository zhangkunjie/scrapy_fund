/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50709
 Source Host           : localhost
 Source Database       : test

 Target Server Type    : MySQL
 Target Server Version : 50709
 File Encoding         : utf-8

 Date: 08/04/2017 08:25:58 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `fund_value`
-- ----------------------------
DROP TABLE IF EXISTS `fund_value`;
CREATE TABLE `fund_value` (
  `fund_id` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `netvalue_date` varchar(20) DEFAULT NULL,
  `netvalue` varchar(20) DEFAULT NULL,
  `cumulativevalue` varchar(20) DEFAULT NULL,
  `daily_growth_rate` varchar(50) DEFAULT NULL,
  `apply_status` varchar(50) DEFAULT NULL,
  `redeem_status` varchar(50) DEFAULT NULL,
  `bonus` varchar(200) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `index_fund_value_fund_id` (`fund_id`),
  KEY `index_fund_value_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

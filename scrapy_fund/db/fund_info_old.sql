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

 Date: 08/04/2017 08:25:43 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `fund_info`
-- ----------------------------
DROP TABLE IF EXISTS `fund_info`;
CREATE TABLE `fund_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(10) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `scale` varchar(50) DEFAULT NULL,
  `manager` varchar(20) DEFAULT NULL,
  `setup_date` varchar(20) DEFAULT NULL,
  `admin` varchar(100) DEFAULT NULL,
  `grade` varchar(20) DEFAULT NULL,
  `trade_first_status` varchar(20) DEFAULT NULL,
  `trade_sencond_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13124 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

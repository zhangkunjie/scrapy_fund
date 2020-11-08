/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80003
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 80003
File Encoding         : 65001

Date: 2020-11-08 22:44:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dingtou_rank
-- ----------------------------
DROP TABLE IF EXISTS `dingtou_rank`;
CREATE TABLE `dingtou_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(11) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `net_asset_value` double DEFAULT NULL,
  `oneyear` double DEFAULT NULL,
  `twoyear` double DEFAULT NULL,
  `threeyear` double DEFAULT NULL,
  `fiveyear` double DEFAULT NULL,
  `grade_no` int(11) DEFAULT NULL,
  `category` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5742 DEFAULT CHARSET=utf8;

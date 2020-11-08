/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80003
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 80003
File Encoding         : 65001

Date: 2020-11-08 22:44:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for fund_rank
-- ----------------------------
DROP TABLE IF EXISTS `fund_rank`;
CREATE TABLE `fund_rank` (
  `fund_id` varchar(11) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `ca_oneweek_rank` int(11) DEFAULT NULL,
  `ca_onemonth_rank` int(11) DEFAULT NULL,
  `ca_threemonth_rank` int(11) DEFAULT NULL,
  `ca_sixmonth_rank` int(11) DEFAULT NULL,
  `ca_oneyear_rank` int(11) DEFAULT NULL,
  `ca_thisyear_rank` int(11) DEFAULT NULL,
  `ca_weighted_rank` double DEFAULT NULL,
  `ca_score_weighted_rank` int(11) DEFAULT NULL,
  `oneweek_rank` int(11) DEFAULT NULL,
  `onemonth_rank` int(11) DEFAULT NULL,
  `threemonth_rank` int(11) DEFAULT NULL,
  `sixmonth_rank` int(11) DEFAULT NULL,
  `oneyear_rank` int(11) DEFAULT NULL,
  `thisyear_rank` int(11) DEFAULT NULL,
  `total_weighted_rank` int(11) DEFAULT NULL,
  `total_score_weighted_rank` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

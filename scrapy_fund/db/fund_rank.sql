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

 Date: 11/06/2020 10:13:56 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `fund_rank`
-- ----------------------------
DROP TABLE IF EXISTS `fund_rank`;
CREATE TABLE `fund_rank` (
  `fund_id` varchar(11) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `ca_oneweek_rank` int DEFAULT NULL,
  `ca_onemonth_rank` int DEFAULT NULL,
  `ca_threemonth_rank` int DEFAULT NULL,
  `ca_sixmonth_rank` int DEFAULT NULL,
  `ca_oneyear_rank` int DEFAULT NULL,
  `ca_thisyear_rank` int DEFAULT NULL,
  `ca_weighted_rank` double DEFAULT NULL,
  `ca_score_weighted_rank` int DEFAULT NULL,
  `oneweek_rank` int DEFAULT NULL,
  `onemonth_rank` int DEFAULT NULL,
  `threemonth_rank` int DEFAULT NULL,
  `sixmonth_rank` int DEFAULT NULL,
  `oneyear_rank` int DEFAULT NULL,
  `thisyear_rank` int DEFAULT NULL,
  `total_weighted_rank` int DEFAULT NULL,
  `total_score_weighted_rank` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

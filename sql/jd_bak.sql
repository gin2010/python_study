-- MySQL dump 10.13  Distrib 8.0.11, for macos10.13 (x86_64)
--
-- Host: localhost    Database: jd
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `address` (
  `name` varchar(20) DEFAULT NULL,
  KEY `address_index` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES ('one'),('three'),('two');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `goods` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `cate_id` int(10) unsigned NOT NULL,
  `brand_id` int(10) unsigned NOT NULL,
  `price` decimal(10,3) NOT NULL DEFAULT '0.000',
  `is_show` bit(1) NOT NULL DEFAULT b'1',
  `is_saleoff` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`id`),
  KEY `cate_id` (`cate_id`),
  KEY `brand_id` (`brand_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (1,'r510vn 15.6寸笔记本',1,1,3399.000,'','\0'),(2,'y400n 14.0寸笔记本',1,2,4999.000,'','\0'),(3,'g150th 15.6寸笔记本',2,3,8499.000,'','\0'),(4,'x550cc 15.6寸笔记本',1,1,2799.000,'','\0'),(5,'x240 超级本',1,2,4880.000,'','\0'),(6,'u330p 13.3寸笔记本',1,2,4299.000,'','\0'),(7,'svvp13226 触控超级本',3,4,7999.000,'','\0'),(8,'ipad air 9.7平板电脑',4,5,3388.000,'','\0'),(9,'ipad mini retina屏',4,5,2788.000,'','\0'),(10,'ideacentre c340 20寸一体机',5,2,3499.000,'','\0'),(11,'vostro 3800-r1206 台式电脑',5,6,2899.000,'','\0'),(12,'benteng 服务器',6,6,12899.000,'\0','\0');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_brands`
--

DROP TABLE IF EXISTS `goods_brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `goods_brands` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_brands`
--

LOCK TABLES `goods_brands` WRITE;
/*!40000 ALTER TABLE `goods_brands` DISABLE KEYS */;
INSERT INTO `goods_brands` VALUES (1,'华硕'),(2,'联想'),(3,'雷神'),(4,'索尼'),(5,'苹果'),(6,'戴尔');
/*!40000 ALTER TABLE `goods_brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_cates`
--

DROP TABLE IF EXISTS `goods_cates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `goods_cates` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cate_index` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_cates`
--

LOCK TABLES `goods_cates` WRITE;
/*!40000 ALTER TABLE `goods_cates` DISABLE KEYS */;
INSERT INTO `goods_cates` VALUES (10,'交换机'),(5,'台式机'),(4,'平板电脑'),(6,'服务器'),(2,'游戏本'),(1,'笔记本'),(9,'网卡'),(3,'超级本'),(8,'路由器');
/*!40000 ALTER TABLE `goods_cates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v_goods_info`
--

DROP TABLE IF EXISTS `v_goods_info`;
/*!50001 DROP VIEW IF EXISTS `v_goods_info`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_goods_info` AS SELECT 
 1 AS `id`,
 1 AS `name`,
 1 AS `cate_id`,
 1 AS `brand_id`,
 1 AS `price`,
 1 AS `is_show`,
 1 AS `is_saleoff`,
 1 AS `cate_name`,
 1 AS `brand_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_goods_info`
--

/*!50001 DROP VIEW IF EXISTS `v_goods_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_goods_info` AS select `g`.`id` AS `id`,`g`.`name` AS `name`,`g`.`cate_id` AS `cate_id`,`g`.`brand_id` AS `brand_id`,`g`.`price` AS `price`,`g`.`is_show` AS `is_show`,`g`.`is_saleoff` AS `is_saleoff`,`c`.`name` AS `cate_name`,`b`.`name` AS `brand_name` from ((`goods` `g` left join `goods_cates` `c` on((`g`.`cate_id` = `c`.`id`))) left join `goods_brands` `b` on((`g`.`brand_id` = `b`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-29 10:57:20

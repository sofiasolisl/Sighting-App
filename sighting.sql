CREATE DATABASE  IF NOT EXISTS `exam3` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `exam3`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: exam3
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sightings`
--

DROP TABLE IF EXISTS `sightings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sightings` (
  `id` int NOT NULL,
  `location` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `description` mediumtext,
  `quantity` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_reporter_id` int NOT NULL,
  PRIMARY KEY (`id`,`user_reporter_id`),
  KEY `fk_sightings_users_idx` (`user_reporter_id`),
  CONSTRAINT `fk_sightings_users` FOREIGN KEY (`user_reporter_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sightings`
--

LOCK TABLES `sightings` WRITE;
/*!40000 ALTER TABLE `sightings` DISABLE KEYS */;
INSERT INTO `sightings` VALUES (1,'USA','2023-10-21',' viwhg;aowurhnsx',1,'2023-10-21 12:19:48','2023-10-21 12:19:48',1),(2,'USA','2023-10-21',' srgsgwrgwege gsxv',1,'2023-10-21 12:20:46','2023-10-21 12:20:46',1),(3,'USA','2023-10-10',' svvxsjdzh.lknasc',2,'2023-10-21 13:58:46','2023-10-21 13:58:46',2),(4,'USA','2023-10-04',' bzsfdgbsege',2,'2023-10-21 13:59:03','2023-10-21 13:59:03',2);
/*!40000 ALTER TABLE `sightings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skeptics`
--

DROP TABLE IF EXISTS `skeptics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skeptics` (
  `user_id` int NOT NULL,
  `sighting_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`sighting_id`),
  KEY `fk_skeptics_sightings1_idx` (`sighting_id`),
  CONSTRAINT `fk_skeptics_sightings1` FOREIGN KEY (`sighting_id`) REFERENCES `sightings` (`id`),
  CONSTRAINT `fk_skeptics_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skeptics`
--

LOCK TABLES `skeptics` WRITE;
/*!40000 ALTER TABLE `skeptics` DISABLE KEYS */;
INSERT INTO `skeptics` VALUES (2,2),(1,3);
/*!40000 ALTER TABLE `skeptics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Sofia','Solis','sofis64@gmail.com','$2b$12$8fCmQu/9Bh.AiLA6y.kB.eaniQNkXBKYdcUrCb961kB7f2m.asaj6','2023-10-21 12:16:10','2023-10-21 12:16:10'),(2,'Pablo','Fallas','palule@gmail.com','$2b$12$iALWha6eAjbx89wjf3Bbm.7kXv49Q.ZsUzUO6bn07qaYezyi7kTKO','2023-10-21 12:34:30','2023-10-21 12:34:30');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-21 14:00:33

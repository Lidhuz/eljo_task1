/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.32-MariaDB : Database - task
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`task` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `task`;

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dep_id` int(11) NOT NULL AUTO_INCREMENT,
  `dep_name` varchar(150) NOT NULL,
  PRIMARY KEY (`dep_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `department` */

insert  into `department`(`dep_id`,`dep_name`) values (1,'Software'),(2,'IT'),(3,'Hardware');

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) NOT NULL,
  `dep_id` int(11) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `contact` decimal(10,0) NOT NULL,
  `photo` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `employee` */

insert  into `employee`(`employee_id`,`login_id`,`dep_id`,`firstname`,`lastname`,`contact`,`photo`) values (1,3,1,'Abijith','A J',8798877665,'static/uploads/5562b8f0-5695-4e0e-9ab2-59415f08cb72istockphoto-1354898581-612x612.jpg'),(2,5,3,'Abhinav','A',7867567455,'static/uploads/95cfcb84-12b0-42ec-a85e-a5b3725c83f5pexels-andrea-piacquadio-927022.jpg'),(3,4,2,'Abhina','Joseph',8897477488,'static/uploads/158a3101-eb1f-4bd0-b7d5-a0bd78d58772download.jfif'),(4,6,1,'Abuna','K S',6080679423,'static/uploads/47941144-c3a4-4acc-b032-ef80330a3441download12.jfif');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `login` */

insert  into `login`(`login_id`,`email`,`password`,`usertype`) values (1,'master@gmail.com','master','admin'),(3,'abijith@gmail.com','1234','employee'),(4,'abhina@gmail.com','1234','employee'),(5,'abhinav@gmail.com','1234','employee'),(6,'abuna@gmail.com','1234','employee');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour m164_guillaume_henchoz_db
DROP DATABASE IF EXISTS `m164_guillaume_henchoz_db`;
CREATE DATABASE IF NOT EXISTS `m164_guillaume_henchoz_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `m164_guillaume_henchoz_db`;

-- Listage de la structure de table m164_guillaume_henchoz_db. t_compte
DROP TABLE IF EXISTS `t_compte`;
CREATE TABLE IF NOT EXISTS `t_compte` (
  `ID_compte` int NOT NULL AUTO_INCREMENT,
  `FK_statut_compte` int NOT NULL,
  `Identifiant_compte` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Mot_de_passe` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `mail` varchar(320) NOT NULL,
  `num_tel` INT(20) DEFAULT NULL,
  `date_creation` timestamp NULL NOT NULL,
  PRIMARY KEY (`ID_compte`),
  KEY `FK_statut_compte` (`FK_statut_compte`),
  CONSTRAINT `FK_statut_compte` FOREIGN KEY (`FK_statut_compte`) REFERENCES `t_statut_compte` (`ID_statut_compte`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table m164_guillaume_henchoz_db.t_compte : ~10 rows (environ)
INSERT INTO `t_compte` (`ID_compte`, `FK_statut_compte`, `Identifiant_compte`, `Mot_de_passe`, `nom`, `prenom`, `mail`, `num_tel`, `date_creation`) VALUES
	(1, 1, '1111', '123Soleil!', 'Henchoz', 'Alexandra', 'alexandra.henchoz@patnioire-echallens.ch', '076.254.26.26', '2024-02-21 09:26:23'),
	(2, 2, '1112', 'Bonjour123!', 'Einstein', 'Didier', 'didier.Einstein@gmail.com', '078.542.12.48', '2024-02-21 09:28:07'),
	(3, 2, '1113', 'yohlo!01', 'Cuche', 'Albert', 'albert.cuche@gmail.com', '079.154.21.96', '2024-02-21 09:29:18'),
	(4, 1, '1114', 'Blablabla!0', 'Mermier', 'Nathalie', 'nathalie.mermier@patinoire-echallens.ch', '076.541.45.82', '2024-02-21 09:31:00'),
	(5, 2, '1115', 'Bisous!to1', 'Barber', 'Caroline', 'caroline.barber@gmail.com', NULL, '2024-02-21 09:32:20'),
	(6, 2, '1116', 'tour$france22', 'Amstrong', 'Nils', 'nils.amstrong@gmail.com', NULL, '2024-02-21 09:33:54'),
	(7, 1, '1110', 'lapatinoire!1', 'patnoire', 'echellens', 'admin@patinoire-echallens.ch', '075.555.10.40', '2024-02-21 10:10:59'),
	(8, 2, '1117', 'bahrain243', 'Grosjean', 'Romain', 'romain.grosjean@gmail.com', NULL, '2024-02-28 09:49:39'),
	(9, 2, '1118', 'imstupide', 'Leclerc', 'Charles', 'charles.leclerc@gmail.com', '078.456.12.32', '2024-02-28 09:51:30'),
	(10, 2, '1119', 'itsfridaythen', 'Norris', 'Lando', 'lando.norris@f1.com', NULL, '2024-02-28 09:53:18');

-- Listage de la structure de table m164_guillaume_henchoz_db. t_heure
DROP TABLE IF EXISTS `t_heure`;
CREATE TABLE IF NOT EXISTS `t_heure` (
  `ID_heure` int NOT NULL AUTO_INCREMENT,
  `heure_debut` time DEFAULT NULL,
  `heure_fin` time DEFAULT NULL,
  PRIMARY KEY (`ID_heure`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table m164_guillaume_henchoz_db.t_heure : ~0 rows (environ)
INSERT INTO `t_heure` (`ID_heure`, `heure_debut`, `heure_fin`) VALUES
	(1, '08:00:00', '09:45:00'),
	(2, '10:00:00', '11:45:00'),
	(3, '13:00:00', '14:45:00'),
	(4, '15:00:00', '16:45:00');

-- Listage de la structure de table m164_guillaume_henchoz_db. t_reservation
DROP TABLE IF EXISTS `t_reservation`;
CREATE TABLE IF NOT EXISTS `t_reservation` (
  `ID_reservation` int NOT NULL AUTO_INCREMENT,
  `FK_statut_res` int DEFAULT NULL,
  `FK_compte` int DEFAULT NULL,
  `FK_heure` int DEFAULT NULL,
  `date` date NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `date_creation` timestamp NULL NOT NULL,
  PRIMARY KEY (`ID_reservation`),
  KEY `FK_statut_res` (`FK_statut_res`),
  KEY `FK_compte` (`FK_compte`),
  KEY `FK_heure` (`FK_heure`),
  CONSTRAINT `FK_compte` FOREIGN KEY (`FK_compte`) REFERENCES `t_compte` (`ID_compte`),
  CONSTRAINT `FK_heure` FOREIGN KEY (`FK_heure`) REFERENCES `t_heure` (`ID_heure`),
  CONSTRAINT `FK_statut_res` FOREIGN KEY (`FK_statut_res`) REFERENCES `t_statut_res` (`ID_statut_res`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table m164_guillaume_henchoz_db.t_reservation : ~9 rows (environ)
INSERT INTO `t_reservation` (`ID_reservation`, `FK_statut_res`, `FK_compte`, `FK_heure`, `date`, `nombre`, `date_creation`) VALUES
	(3, 1, 2, 1, '2024-02-21', '23', '2024-02-21 09:59:05'),
	(4, 2, 6, 1, '2024-02-21', '19', '2024-02-21 09:59:48'),
	(5, 2, 6, 1, '2024-02-21', '20', '2024-02-21 10:01:13'),
	(6, 1, 5, 2, '2024-02-22', '17', '2024-02-21 10:04:35'),
	(7, 3, NULL, 3, '2024-02-22', NULL, NULL),
	(8, 3, NULL, 2, '2024-02-22', NULL, NULL),
	(9, 1, 9, 3, '2024-02-23', '24', '2024-02-28 09:55:15'),
	(10, 2, 10, 2, '2024-02-23', '25', '2024-02-28 09:56:04'),
	(11, 3, NULL, 1, '2024-02-23', NULL, NULL);

-- Listage de la structure de table m164_guillaume_henchoz_db. t_statut_compte
DROP TABLE IF EXISTS `t_statut_compte`;
CREATE TABLE IF NOT EXISTS `t_statut_compte` (
  `ID_statut_compte` int NOT NULL AUTO_INCREMENT,
  `designation` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_statut_compte`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table m164_guillaume_henchoz_db.t_statut_compte : ~2 rows (environ)
INSERT INTO `t_statut_compte` (`ID_statut_compte`, `designation`) VALUES
	(1, 'Admin'),
	(2, 'Client');

-- Listage de la structure de table m164_guillaume_henchoz_db. t_statut_res
DROP TABLE IF EXISTS `t_statut_res`;
CREATE TABLE IF NOT EXISTS `t_statut_res` (
  `ID_statut_res` int NOT NULL AUTO_INCREMENT,
  `etat` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_statut_res`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table m164_guillaume_henchoz_db.t_statut_res : ~3 rows (environ)
INSERT INTO `t_statut_res` (`ID_statut_res`, `etat`) VALUES
	(1, 'En attente'),
	(2, 'réservé'),
	(3, 'libre');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

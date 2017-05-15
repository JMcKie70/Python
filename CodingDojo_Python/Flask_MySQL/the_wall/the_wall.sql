-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema the_wall
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema_wall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `the_wall` DEFAULT CHARACTER SET utf8 ;
USE `the_wall` ;

-- -----------------------------------------------------
-- Table `the_wall`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `added` DATETIME NULL,
  `edited` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `the_wall`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `message` TEXT NULL,
  `added` DATETIME NULL,
  `edited` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id_idx` (`user_id` ASC),
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `the_wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- 08:45:46	CREATE TABLE IF NOT EXISTS `the_wall`.`comments` (   `id` INT NOT NULL AUTO_INCREMENT,   `message_id` INT NOT NULL,   `user_id` INT NOT NULL,   `comment` TEXT NULL,   `added` DATETIME NULL,   `edited` DATETIME NULL,   PRIMARY KEY (`id`),   INDEX `message_id_idx` (`message_id` ASC),   INDEX `user_id_idx` (`user_id` ASC),   CONSTRAINT `message_id`     FOREIGN KEY (`message_id`)     REFERENCES `the_wall`.`messages` (`id`)     ON DELETE NO ACTION     ON UPDATE NO ACTION,   CONSTRAINT `user_id`     FOREIGN KEY (`user_id`)     REFERENCES `the_wall`.`users` (`id`)     ON DELETE NO ACTION     ON UPDATE NO ACTION) ENGINE = InnoDB	Error Code: 1022. Can't write; duplicate key in table 'comments'	0.015 sec
-- 
-- -----------------------------------------------------
-- Table `the_wall`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `message_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `comment` TEXT NULL,
  `added` DATETIME NULL,
  `edited` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `message_id_idx` (`message_id` ASC),
  INDEX `user_id_idx` (`user_id` ASC),
  CONSTRAINT `message_id`
    FOREIGN KEY (`comment_message_id`)
    REFERENCES `the_wall`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `user_id`
    FOREIGN KEY (`comment_user_id`)
    REFERENCES `the_wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- 08:54:40	CREATE TABLE IF NOT EXISTS `the_wall`.`comments` (   `id` INT NOT NULL AUTO_INCREMENT,   `message_id` INT NOT NULL,   `user_id` INT NOT NULL,   `comment` TEXT NULL,   `added` DATETIME NULL,   `edited` DATETIME NULL,   PRIMARY KEY (`id`),   INDEX `message_id_idx` (`message_id` ASC),   INDEX `user_id_idx` (`user_id` ASC),   CONSTRAINT `message_id`     FOREIGN KEY (`comment_message_id`)     REFERENCES `the_wall`.`messages` (`id`)     ON DELETE NO ACTION     ON UPDATE NO ACTION,   CONSTRAINT `user_id`     FOREIGN KEY (`comment_user_id`)     REFERENCES `the_wall`.`users` (`id`)     ON DELETE NO ACTION     ON UPDATE NO ACTION) ENGINE = InnoDB	Error Code: 1072. Key column 'comment_message_id' doesn't exist in table	0.00058 sec


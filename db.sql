-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema fuzzy_yellow_balls
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema fuzzy_yellow_balls
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `fuzzy_yellow_balls` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `fuzzy_yellow_balls` ;

-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`match_meta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`match_meta` (
  `match_id` VARCHAR(100) NOT NULL,
  `Player_1` VARCHAR(27) NOT NULL,
  `Player_2` VARCHAR(27) NOT NULL,
  `Pl_1_hand` VARCHAR(2) NOT NULL,
  `Pl_2_hand` VARCHAR(2) NOT NULL,
  `Gender` VARCHAR(1) NOT NULL,
  `Date` DATE NOT NULL,
  `Tournament` VARCHAR(45) NOT NULL,
  `Round` VARCHAR(4) NOT NULL,
  `Time` VARCHAR(14) NULL DEFAULT NULL,
  `Court` VARCHAR(60) NULL DEFAULT NULL,
  `Surface` VARCHAR(14) NULL DEFAULT NULL,
  `Umpire` VARCHAR(33) NULL DEFAULT NULL,
  `Best_of` INT NOT NULL,
  `Final_TB` VARCHAR(2) NULL DEFAULT NULL,
  `Charted_by` VARCHAR(17) NOT NULL,
  PRIMARY KEY (`match_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`match_overview`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`match_overview` (
  `overview_id` INT NOT NULL AUTO_INCREMENT,
  `match_id` VARCHAR(100) NOT NULL,
  `player` INT NOT NULL,
  `set` VARCHAR(5) NOT NULL,
  `serve_pts` INT NOT NULL,
  `aces` INT NOT NULL,
  `dfs` INT NOT NULL,
  `first_in` INT NOT NULL,
  `first_won` INT NOT NULL,
  `second_in` INT NOT NULL,
  `second_won` INT NOT NULL,
  `bk_pts` INT NOT NULL,
  `bp_saved` INT NOT NULL,
  `return_pts` INT NOT NULL,
  `return_pts_won` INT NOT NULL,
  `winners` INT NOT NULL,
  `winners_fh` INT NOT NULL,
  `winners_bh` INT NOT NULL,
  `unforced` INT NOT NULL,
  `unforced_fh` INT NOT NULL,
  `unforced_bh` INT NOT NULL,
  PRIMARY KEY (`overview_id`, `match_id`),
  INDEX `fk_match_overview_match_meta1_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_match_overview_match_meta1`
    FOREIGN KEY (`match_id`)
    REFERENCES `fuzzy_yellow_balls`.`match_meta` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`netpoint`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`netpoint` (
  `netpoint_id` INT NOT NULL AUTO_INCREMENT,
  `match_id` VARCHAR(100) NOT NULL,
  `player` INT NOT NULL,
  `row` VARCHAR(16) NOT NULL,
  `net_pts` INT NOT NULL,
  `pts_won` INT NOT NULL,
  `net_winner` INT NOT NULL,
  `induced_forced` INT NOT NULL,
  `net_unforced` INT NOT NULL,
  `passed_at_net` INT NOT NULL,
  `passing_shot_induced_forced` INT NOT NULL,
  `total_shots` INT NOT NULL,
  PRIMARY KEY (`netpoint_id`, `match_id`),
  INDEX `fk_netpoint_match_meta1_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_netpoint_match_meta1`
    FOREIGN KEY (`match_id`)
    REFERENCES `fuzzy_yellow_balls`.`match_meta` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`return_depth`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`return_depth` (
  `return_depth_id` INT NOT NULL AUTO_INCREMENT,
  `match_id` VARCHAR(100) NOT NULL,
  `player` INT NOT NULL,
  `row` VARCHAR(5) NOT NULL,
  `returnable` INT NOT NULL,
  `shallow` INT NOT NULL,
  `deep` INT NOT NULL,
  `very_deep` INT NOT NULL,
  `unforced` INT NOT NULL,
  `err_net` INT NOT NULL,
  `err_deep` INT NOT NULL,
  `err_wide` INT NOT NULL,
  `err_wide_deep` INT NOT NULL,
  PRIMARY KEY (`return_depth_id`, `match_id`),
  INDEX `fk_return_depth_match_meta1_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_return_depth_match_meta1`
    FOREIGN KEY (`match_id`)
    REFERENCES `fuzzy_yellow_balls`.`match_meta` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`return_outcome`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`return_outcome` (
  `return_outcome_id` INT NOT NULL AUTO_INCREMENT,
  `match_id` VARCHAR(100) NOT NULL,
  `player` INT NOT NULL,
  `row` VARCHAR(5) NOT NULL,
  `pts` INT NOT NULL,
  `pts_won` INT NOT NULL,
  `returnable` INT NOT NULL,
  `returnable_won` INT NOT NULL,
  `in_play` INT NOT NULL,
  `in_play_won` INT NOT NULL,
  `winners` INT NOT NULL,
  `total_shots` INT NOT NULL,
  PRIMARY KEY (`return_outcome_id`, `match_id`),
  INDEX `fk_return_outcome_match_meta1_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_return_outcome_match_meta1`
    FOREIGN KEY (`match_id`)
    REFERENCES `fuzzy_yellow_balls`.`match_meta` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`serve_basic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`serve_basic` (
  `serve_basic_id` INT NOT NULL AUTO_INCREMENT,
  `match_id` VARCHAR(100) NOT NULL,
  `player` INT NOT NULL,
  `set` VARCHAR(5) NOT NULL,
  `pts` INT NOT NULL,
  `pts_won` INT NOT NULL,
  `aces` INT NOT NULL,
  `unret` INT NOT NULL,
  `forced_err` INT NOT NULL,
  `pts_won_lte_3_shots` INT NOT NULL,
  `wide` INT NOT NULL,
  `body` INT NOT NULL,
  `t` INT NOT NULL,
  PRIMARY KEY (`serve_basic_id`, `match_id`),
  INDEX `fk_serve_basic_match_meta_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_serve_basic_match_meta`
    FOREIGN KEY (`match_id`)
    REFERENCES `fuzzy_yellow_balls`.`match_meta` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`serve_influence`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`serve_influence` (
  `serve_influence_id` INT NOT NULL AUTO_INCREMENT,
  `match_id` VARCHAR(100) NOT NULL,
  `player` INT NOT NULL,
  `serve` INT NOT NULL,
  `pts` INT NOT NULL,
  `won_1` DECIMAL(6,2) NOT NULL,
  `won_2` DECIMAL(6,2) NOT NULL,
  `won_3` DECIMAL(6,2) NOT NULL,
  `won_4` DECIMAL(6,2) NOT NULL,
  `won_5` DECIMAL(6,2) NOT NULL,
  `won_6` DECIMAL(6,2) NOT NULL,
  `won_7` DECIMAL(6,2) NOT NULL,
  `won_8` DECIMAL(6,2) NOT NULL,
  `won_9` DECIMAL(6,2) NOT NULL,
  `won_10` DECIMAL(6,2) NOT NULL,
  PRIMARY KEY (`serve_influence_id`, `match_id`),
  INDEX `fk_serve_influence_match_meta1_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_serve_influence_match_meta1`
    FOREIGN KEY (`match_id`)
    REFERENCES `fuzzy_yellow_balls`.`match_meta` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`shot_direction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`shot_direction` (
  `shot_direction_id` INT NOT NULL AUTO_INCREMENT,
  `match_id` VARCHAR(100) NOT NULL,
  `player` INT NOT NULL,
  `row` VARCHAR(8) NOT NULL,
  `crosscourt` INT NOT NULL,
  `down_middle` INT NOT NULL,
  `down_the_line` INT NOT NULL,
  `inside_out` INT NOT NULL,
  `inside_in` INT NOT NULL,
  PRIMARY KEY (`shot_direction_id`, `match_id`),
  INDEX `fk_shot_direction_match_meta1_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_shot_direction_match_meta1`
    FOREIGN KEY (`match_id`)
    REFERENCES `fuzzy_yellow_balls`.`match_meta` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `fuzzy_yellow_balls`.`shotdir_outcome`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fuzzy_yellow_balls`.`shotdir_outcome` (
  `shotdir_outcome_id` INT NOT NULL AUTO_INCREMENT,
  `match_id` VARCHAR(100) NOT NULL,
  `player` INT NOT NULL,
  `hand` VARCHAR(8) NOT NULL,
  `direction` VARCHAR(15) NOT NULL,
  `shots` INT NOT NULL,
  `pt_ending` INT NOT NULL,
  `winners` INT NOT NULL,
  `induced_forced` INT NOT NULL,
  `unforced` INT NOT NULL,
  `shots_in_pts_won` INT NOT NULL,
  `shots_in_pts_lost` INT NOT NULL,
  PRIMARY KEY (`shotdir_outcome_id`, `match_id`),
  INDEX `fk_shotdir_outcome_match_meta1_idx` (`match_id` ASC) VISIBLE,
  CONSTRAINT `fk_shotdir_outcome_match_meta1`
    FOREIGN KEY (`match_id`)
    REFERENCES `fuzzy_yellow_balls`.`match_meta` (`match_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

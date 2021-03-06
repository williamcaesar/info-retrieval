CREATE TABLE IF NOT EXISTS `ri_probabilistic`.`documents` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `text` MEDIUMTEXT NULL DEFAULT NULL,
  `tokens` JSON NULL DEFAULT NULL,
  `qtStopwords` INT(11) NULL DEFAULT '0',
  `qtStopwordsTotal` INT(11) NULL DEFAULT '0',
  `qtAdverbios` INT(11) NULL DEFAULT '0',
  `qtAdverbiosTotal` INT(11) NULL DEFAULT '0',
  `qtToken` INT(11) NULL DEFAULT '0',
  `qtTokenTotal` INT(11) NULL DEFAULT '0',
  `tf` JSON NULL DEFAULT NULL,
  `max` INT(11) NULL DEFAULT '0',
  `logNormalization` JSON NULL DEFAULT NULL,
  `doubleNormalization` JSON NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 164
DEFAULT CHARACTER SET = utf8

CREATE TABLE IF NOT EXISTS `ri_probabilistic`.`global` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `words` JSON NULL DEFAULT NULL,
  `qtStopwords` INT(11) NULL DEFAULT '0',
  `qtAdverbios` INT(11) NULL DEFAULT '0',
  `qtTokens` INT(11) NULL DEFAULT '0',
  `qtDocument` JSON NULL DEFAULT NULL,
  `idf` JSON NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8
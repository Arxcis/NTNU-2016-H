-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 31, 2016 at 12:55 PM
-- Server version: 5.6.28
-- PHP Version: 7.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `oblig_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogginnlegg`
--

CREATE TABLE `blogginnlegg` (
  `ID` int(10) NOT NULL,
  `Tittel` varchar(255) NOT NULL,
  `Innhold` text NOT NULL,
  `ForfatterNavn` varchar(255) NOT NULL,
  `ForfatterEpost` varchar(255) NOT NULL,
  `PubTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `EditTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `blogginnlegg`
--

INSERT INTO `blogginnlegg` (`ID`, `Tittel`, `Innhold`, `ForfatterNavn`, `ForfatterEpost`, `PubTime`, `EditTime`) VALUES
(1, 'Første post', 'Dette er den første posten. \r\n\r\nVi kjører denne posten for å teste om noe kan gå galt.\r\n\r\n<i>Lorem Ipsum epsilon </i>\r\n\r\nav jonas J. Solsvik\r\n\r\n<img width="100" height="100" src="http://i.imgur.com/VdPuvBD.png"/>', 'Jonas J. Solsvik', 'jonas.solsvik@gmail.com', '2016-08-28 23:07:07', '0000-00-00 00:00:00'),
(2, 'I love code', '\r\n<img style="margin:auto;" width="300px" height="300px" src="https://timbrosnan.files.wordpress.com/2014/11/what-a-wonderful-world.jpg"/>\r\n\r\nI see skyes so blue, red roses too....', 'Jonas J. Solsvik', 'jonas.solsvik@gmail.com', '2016-08-29 21:57:56', '0000-00-00 00:00:00'),
(7, 'blablabla', 'gøy på baserom', 'Jonas J. Solsvik', 'jonas.solsvik@gmail.com', '2016-08-30 16:28:20', '0000-00-00 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blogginnlegg`
--
ALTER TABLE `blogginnlegg`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blogginnlegg`
--
ALTER TABLE `blogginnlegg`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
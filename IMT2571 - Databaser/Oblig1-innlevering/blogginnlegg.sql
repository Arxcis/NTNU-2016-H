-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 25, 2016 at 04:41 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 7.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `oblig_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogginnlegg`
--

CREATE TABLE `blogginnlegg` (
  `ID` int(10) NOT NULL,
  `TIttel` varchar(255) NOT NULL,
  `Innhold` text NOT NULL,
  `ForfatterNavn` varchar(255) NOT NULL,
  `ForfatterEpost` varchar(255) NOT NULL,
  `PubTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `EditTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `blogginnlegg`
--

INSERT INTO `blogginnlegg` (`ID`, `TIttel`, `Innhold`, `ForfatterNavn`, `ForfatterEpost`, `PubTime`, `EditTime`) VALUES
(1, 'Hierarchy Representation in OpenCV', 'So each contour has its own information regarding what hierarchy it is, who is its child, who is its parent etc. OpenCV represents it as an array of four values : [Next, Previous, First_Child, Parent]\r\n\r\n*"Next denotes next contour at the same hierarchical level."*\r\nFor eg, take contour-0 in our picture. Who is next contour in its same level ? It is contour-1. So simply put Next = 1. Similarly for Contour-1, next is contour-2. So Next = 2.\r\n\r\nWhat about contour-2? There is no next contour in the same level. So simply, put Next = -1. What about contour-4? It is in same level with contour-5. So its next contour is contour-5, so Next = 5.\r\n\r\n*"Previous denotes previous contour at the same hierarchical level."*\r\nIt is same as above. Previous contour of contour-1 is contour-0 in the same level. Similarly for contour-2, it is contour-1. And for contour-0, there is no previous, so put it as -1.\r\n\r\n*"First_Child denotes its first child contour."*\r\nThere is no need of any explanation. For contour-2, child is contour-2a. So it gets the corresponding index value of contour-2a. What about contour-3a? It has two children. But we take only first child. And it is contour-4. So First_Child = 4 for contour-3a.\r\n\r\n*"Parent denotes index of its parent contour."*\r\nIt is just opposite of First_Child. Both for contour-4 and contour-5, parent contour is contour-3a. For contour-3a, it is contour-3 and so on.', 'Jonas', 'jonas.solsvik@gmail.com', '2016-08-25 14:40:39', '0000-00-00 00:00:00'),
(2, 'Contour Retrieval Mode\r\n\r\n', '1. RETR_LIST\r\n\r\nThis is the simplest of the four flags (from explanation point of view). It simply retrieves all the contours, but doesn''t create any parent-child relationship. Parents and kids are equal under this rule, and they are just contours. ie they all belongs to same hierarchy level.\r\n\r\nSo here, 3rd and 4th term in hierarchy array is always -1. But obviously, Next and Previous terms will have their corresponding values. Just check it yourself and verify it.\r\n\r\nBelow is the result I got, and each row is hierarchy details of corresponding contour. For eg, first row corresponds to contour 0. Next contour is contour 1. So Next = 1. There is no previous contour, so Previous = 0. And the remaining two, as told before, it is -1.\r\n\r\n    1 >>> hierarchy\r\n    2 array([[[ 1, -1, -1, -1],\r\n    3         [ 2,  0, -1, -1],\r\n    4         [ 3,  1, -1, -1],\r\n    5         [ 4,  2, -1, -1],\r\n    6         [ 5,  3, -1, -1],\r\n    7         [ 6,  4, -1, -1],\r\n    8         [ 7,  5, -1, -1],\r\n    9         [-1,  6, -1, -1]]])\r\nThis is the good choice to use in your code, if you are not using any hierarchy features.\r\n\r\n2. RETR_EXTERNAL\r\n\r\nIf you use this flag, it returns only extreme outer flags. All child contours are left behind. We can say, under this law, Only the eldest in every family is taken care of. It doesn''t care about other members of the family :).\r\n\r\nSo, in our image, how many extreme outer contours are there? ie at hierarchy-0 level?. Only 3, ie contours 0,1,2, right? Now try to find the contours using this flag. Here also, values given to each element is same as above. Compare it with above result. Below is what I got :\r\n\r\n    1 >>> hierarchy\r\n    2 array([[[ 1, -1, -1, -1],\r\n    3         [ 2,  0, -1, -1],\r\n    4         [-1,  1, -1, -1]]])\r\nYou can use this flag if you want to extract only the outer contours. It might be useful in some cases.\r\n\r\n', 'Jonas', 'jonas.solsvik@gmail.com', '2016-08-25 14:40:39', '0000-00-00 00:00:00');

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
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

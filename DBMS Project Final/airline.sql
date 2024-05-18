-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2023 at 12:09 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `airline`
--

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `AP_NAME` varchar(100) NOT NULL,
  `CITY` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`AP_NAME`, `CITY`) VALUES
('Chandigarh International Airport', 'Chandigarh'),
('Chhatrapati Shivaji International Airport', 'Mumbai'),
('Dallas/Fort Worth International Airport', 'Fort Worth'),
('Frankfurt Airport', 'Frankfurt'),
('George Bush Intercontinental Airport', 'Houston'),
('Indira GandhiInternational Airport', 'Delhi'),
('John F. Kennedy International Airport', 'New York City'),
('Louisville International Airport', 'Louisville'),
('San Francisco International Airport', 'San Francisco'),
('Tampa International Airport', 'Tampa');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `PID` int(11) NOT NULL,
  `TICKET_NUMBER` int(11) NOT NULL,
  `DATE_OF_BOOKING` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`PID`, `TICKET_NUMBER`, `DATE_OF_BOOKING`) VALUES
(18, 16, '2023-04-16');

-- --------------------------------------------------------

--
-- Table structure for table `cancels`
--

CREATE TABLE `cancels` (
  `PID` int(11) NOT NULL,
  `TICKET_NUMBER` int(11) NOT NULL,
  `DATE_OF_CANCELLATION` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cancels`
--

INSERT INTO `cancels` (`PID`, `TICKET_NUMBER`, `DATE_OF_CANCELLATION`) VALUES
(17, 15, '2023-04-16');

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `FLIGHT_CODE` varchar(20) NOT NULL,
  `AP_NAME` varchar(100) NOT NULL,
  `SOURCE` varchar(20) NOT NULL,
  `DESTINATION` varchar(20) NOT NULL,
  `DEPARTURE` time NOT NULL,
  `DURATION` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`FLIGHT_CODE`, `AP_NAME`, `SOURCE`, `DESTINATION`, `DEPARTURE`, `DURATION`) VALUES
('9W2334', 'George Bush Intercontinental Airport', 'Houston', 'Delhi', '23:00:00', '23hrs'),
('AI101', 'Chandigarh International Airport', 'Chandigarh', 'Delhi', '06:00:00', '1h 10m'),
('AI102', 'Indira GandhiInternational Airport', 'Delhi', 'Chandigarh', '07:30:00', '1h 10m'),
('AI201', 'Chhatrapati Shivaji International Airport', 'Mumbai', 'Delhi', '09:00:00', '2h 30m'),
('AI202', 'Indira GandhiInternational Airport', 'Delhi', 'Mumbai', '12:00:00', '2h 30m'),
('AI301', 'John F. Kennedy International Airport', 'New York City', 'Frankfurt', '13:00:00', '8h 0m'),
('AI302', 'Frankfurt Airport', 'Frankfurt', 'New York City', '22:00:00', '8h 0m'),
('AI401', 'George Bush Intercontinental Airport', 'Houston', 'San Francisco', '08:00:00', '3h 45m'),
('AI402', 'San Francisco International Airport', 'San Francisco', 'Houston', '14:00:00', '3h 45m'),
('AI501', 'Dallas/Fort Worth International Airport', 'Fort Worth', 'Louisville', '10:00:00', '2h 0m'),
('AI502', 'Louisville International Airport', 'Louisville', 'Fort Worth', '13:00:00', '2h 0m'),
('AI601', 'Tampa International Airport', 'Tampa', 'Houston', '09:00:00', '2h 45m'),
('AI602', 'George Bush Intercontinental Airport', 'Houston', 'Tampa', '13:00:00', '2h 45m');

-- --------------------------------------------------------

--
-- Table structure for table `passenger`
--

CREATE TABLE `passenger` (
  `PID` int(11) NOT NULL,
  `FLIGHT_CODE` varchar(20) NOT NULL,
  `FULL_NAME` varchar(100) NOT NULL,
  `ADDRESS` varchar(200) NOT NULL,
  `PHONE` varchar(20) NOT NULL,
  `AGE` int(200) NOT NULL,
  `SEX` varchar(10) NOT NULL,
  `PASSPORTNO` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `passenger`
--

INSERT INTO `passenger` (`PID`, `FLIGHT_CODE`, `FULL_NAME`, `ADDRESS`, `PHONE`, `AGE`, `SEX`, `PASSPORTNO`) VALUES
(18, 'AI201', 'Sam', 'Rs, 110023', '8765483647', 34, 'Male', 'ABCD383');

-- --------------------------------------------------------

--
-- Table structure for table `ticket1`
--

CREATE TABLE `ticket1` (
  `TICKET_NUMBER` int(11) NOT NULL,
  `SOURCE` varchar(20) NOT NULL,
  `DESTINATION` varchar(20) NOT NULL,
  `DATE_OF_TRAVEL` date NOT NULL,
  `SEAT_NO` int(11) NOT NULL,
  `PID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ticket1`
--

INSERT INTO `ticket1` (`TICKET_NUMBER`, `SOURCE`, `DESTINATION`, `DATE_OF_TRAVEL`, `SEAT_NO`, `PID`) VALUES
(16, 'Mumbai', 'Delhi', '2023-06-23', 19, 18);

--
-- Triggers `ticket1`
--
DELIMITER $$
CREATE TRIGGER `cancels_data` BEFORE DELETE ON `ticket1` FOR EACH ROW BEGIN
    INSERT INTO cancels (PID, ticket_number,date_of_cancellation)
    VALUES (OLD.PID, OLD.ticket_number, CURDATE());
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `copy_ticket_info_and_insert_books` AFTER INSERT ON `ticket1` FOR EACH ROW BEGIN
    INSERT INTO books (pid, ticket_number, date_of_booking)
    VALUES (NEW.pid, NEW.ticket_number, NOW());
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `seat_no_pid_trigger` BEFORE INSERT ON `ticket1` FOR EACH ROW BEGIN
    DECLARE latest_seat_no INT;
    DECLARE latest_pid INT;
    SELECT SEAT_NO INTO latest_seat_no FROM ticket2 ORDER BY SEAT_NO DESC LIMIT 1;
    SELECT PID INTO latest_pid FROM passenger ORDER BY PID DESC LIMIT 1;
    SET NEW.SEAT_NO = latest_seat_no;
    SET NEW.PID = latest_pid;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `ticket2`
--

CREATE TABLE `ticket2` (
  `SEAT_NO` int(11) NOT NULL,
  `CLASS` varchar(11) NOT NULL,
  `PRICE` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ticket2`
--

INSERT INTO `ticket2` (`SEAT_NO`, `CLASS`, `PRICE`) VALUES
(19, 'Business', 112900);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`AP_NAME`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`PID`,`TICKET_NUMBER`),
  ADD KEY `books_ibfk_2` (`TICKET_NUMBER`);

--
-- Indexes for table `cancels`
--
ALTER TABLE `cancels`
  ADD PRIMARY KEY (`PID`,`TICKET_NUMBER`),
  ADD KEY `cancels_ibfk_2` (`TICKET_NUMBER`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`FLIGHT_CODE`),
  ADD KEY `AP_NAME` (`AP_NAME`);

--
-- Indexes for table `passenger`
--
ALTER TABLE `passenger`
  ADD PRIMARY KEY (`PID`),
  ADD KEY `passenger_ibfk_1` (`FLIGHT_CODE`);

--
-- Indexes for table `ticket1`
--
ALTER TABLE `ticket1`
  ADD PRIMARY KEY (`TICKET_NUMBER`),
  ADD KEY `PID` (`PID`),
  ADD KEY `SEAT_NO` (`SEAT_NO`);

--
-- Indexes for table `ticket2`
--
ALTER TABLE `ticket2`
  ADD PRIMARY KEY (`SEAT_NO`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `passenger`
--
ALTER TABLE `passenger`
  MODIFY `PID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `ticket1`
--
ALTER TABLE `ticket1`
  MODIFY `TICKET_NUMBER` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `ticket2`
--
ALTER TABLE `ticket2`
  MODIFY `SEAT_NO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `passenger` (`PID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `books_ibfk_2` FOREIGN KEY (`TICKET_NUMBER`) REFERENCES `ticket1` (`TICKET_NUMBER`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`AP_NAME`) REFERENCES `airport` (`AP_NAME`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `passenger`
--
ALTER TABLE `passenger`
  ADD CONSTRAINT `passenger_ibfk_1` FOREIGN KEY (`FLIGHT_CODE`) REFERENCES `flight` (`FLIGHT_CODE`);

--
-- Constraints for table `ticket1`
--
ALTER TABLE `ticket1`
  ADD CONSTRAINT `ticket1_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `passenger` (`PID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ticket1_ibfk_2` FOREIGN KEY (`SEAT_NO`) REFERENCES `ticket2` (`SEAT_NO`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

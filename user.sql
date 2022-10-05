-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 05, 2022 at 03:37 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dlt_transcation`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(60) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `key` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `username`, `email`, `password`, `date_created`, `key`) VALUES
(1, 'Rohit Singh', 'rohit_6174', 'rohit224455@gmail.com', '$2b$12$dttt/cFPQVk2y/JWR6ITm.qZdpz0Bw3qs1tSXB3RD6RDtqW8GibLy', '2022-10-04 18:19:03', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0HKKwVpj+EEw6kmvKtVu\nTnLNn1mwG6CeAI1iFHgxTuIY1P4Lpb56iSn9WbU62OQVad1W1JF8aZ96XCXT+B5g\noWsNtLLj2Qe17rBz2KFb6aUr37pSbfJtvZQKUtI5Cr2u0qifSh5N6shpmFj9afCg\n/PZZRP2p2n68lbz6/bZK6f+eUqwxpu2yIRr1WFJDvyijrhSy+QKUQnZ7oFaMrk6t\nKPNO5nz7qmqHr9fgxJg1uQdprtGR1TO7soumSde9R155+AuVvdJT9mgY21OLtpSW\nVlW1rFYYIoQdWslzt5WS8okAJcyzzmuf+naKRXqRstRt+Fw5A/vzNaTVRm4XZjuQ\nTwIDAQAB\n-----END PUBLIC KEY-----'),
(4, 'Rohan Shahabaje', 'rohan', 'rohan@gmail.com', '$2b$12$DViMj/TtrJSCqM1VnJRNYOK9nGG8XU3AHA8njlKMkedUPBBHqPbuG', '2022-10-04 23:29:26', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr2tj8c+0NZZepwr1lk+6\nxN5isbYrtKBi00+LB7OP5G0pCqeh1Q5O23VVmyFg3gHz0KQZJKKboXD5TmqtV/Ln\n27vgzYsgNR6kFr2vGbqMG/N6b/HWZxpd9z+tI1YqdqXRZipqrqzI4VGm4bONYtXL\nBRpgTgjGtbMYd+Fn+oJKm0BMDMV9Jpey0B10WciiV8a4CT37Bp5bgHPK4CVt/SFS\nJvc4cWzMHsu6micBiV96AzG5sWIhU3zAo8uVQ31q7ToguT8y16Hc8JKmQziWnyJP\n/vY0n0rNTTD6XiqNXBYbf7oE0V9rU00lSiDnqTsrxDHqxoiooRqhZleUIbc5ZjRu\nfQIDAQAB\n-----END PUBLIC KEY-----'),
(5, 'Vrushabh', 'vrushab', 'vrushab@gmail.com', '$2b$12$Sn7.j/c6FPuSUCR1t4709uqICyvP9nuuYQuvnmhT./6WHhx5JhWhy', '2022-10-05 01:35:48', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr+znTwzGUMEx4iO2jzr3\nibOSoVdj6aaZnmZzORdwWGE7BBj2++whmePkeEuAA3sqBRqUt53RC/1TAPIqMolm\ni44Bg3F47wyLWhzGxy70C5IPZTYHa4BCbxMRH4CQUMxNfEX1epHy7G13/dKFD8Nq\nTaqlXOJCU626UiN+n636/uvmtNAKnaHpisDP7vDgcsV4+QOUXi9m8NIq9duemmF3\nkwwNlaB8oFMD+/1+6Zk4xrj7uXE7qNFznKTU39/zodNy7eiRpTsClvkiwhMlWamw\n3uuWM+kGoDEABXaw9yJOt9DrgT8/+x0ONDVYYN8z5KSK0v4QwnR+sGStVrUcP6Yp\nCwIDAQAB\n-----END PUBLIC KEY-----');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `key` (`key`) USING HASH;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
